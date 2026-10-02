/**
 * MEMOUR Studio - Next-Gen 3D Interactive Scrapbook Engine 360°
 * Photorealistic Three.js Materials, Full 2D/3D Color Synchronization,
 * Smooth Camera Cinematics, Tactile 3D Embossed Relief & Dynamic Bindings
 */

let scene, camera, renderer, controls;
let bookGroup, pageMesh, leftPageMesh, leftCoverPivot, spineMesh, ringsGroup, stickers3DGroup;
let canvasTexture = null;
let paperGrainTexture = null;
let currentFrontCoverTexture = null;
let currentBackCoverTexture = null;
let innerCraftSpreadMat = null;
let pageEdgeMat = null;
let frontCoverMat = null;
let backCoverMat = null;
let is3dInitialized = false;
let isAutoRotate = false;

// Book Folding State
let isBookClosed = false;
let isAnimatingFold = false;
let foldProgress = 0.0; // 0.0 = Open Spread (180° flat), 1.0 = Closed Book
let bookAspectRatio = 0.7062; // Default A5 Portrait

// Page Flip State
let isFlippingPage = false;
let cameraAnimFrame = null;

// ================= PROCEDURAL PAPER & LEATHER TEXTURES =================
function createPaperGrainTexture() {
  const size = 512;
  const canvasElem = document.createElement('canvas');
  canvasElem.width = size;
  canvasElem.height = size;
  const ctx = canvasElem.getContext('2d');
  
  // Warm Kraft Paper Base Tone
  ctx.fillStyle = '#f8f4ed';
  ctx.fillRect(0, 0, size, size);
  
  // Organic noise grain
  const imgData = ctx.getImageData(0, 0, size, size);
  const data = imgData.data;
  for (let i = 0; i < data.length; i += 4) {
    const noise = (Math.random() - 0.5) * 16;
    data[i] = Math.min(255, Math.max(0, data[i] + noise));
    data[i + 1] = Math.min(255, Math.max(0, data[i + 1] + noise));
    data[i + 2] = Math.min(255, Math.max(0, data[i + 2] + noise));
  }
  ctx.putImageData(imgData, 0, 0);

  // Subtle organic craft fibers
  ctx.strokeStyle = 'rgba(120, 53, 15, 0.04)';
  ctx.lineWidth = 1;
  for (let i = 0; i < 40; i++) {
    ctx.beginPath();
    const x = Math.random() * size;
    const y = Math.random() * size;
    ctx.moveTo(x, y);
    ctx.lineTo(x + (Math.random() - 0.5) * 28, y + (Math.random() - 0.5) * 28);
    ctx.stroke();
  }

  const texture = new THREE.CanvasTexture(canvasElem);
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.repeat.set(3, 3);
  return texture;
}

function createProceduralCoverTexture(colorHex, title = "MEMOUR SCRAPBOOK", isFront = true) {
  const size = 1024;
  const canvasElem = document.createElement('canvas');
  canvasElem.width = size;
  canvasElem.height = size;
  const ctx = canvasElem.getContext('2d');

  // Rich base background color
  ctx.fillStyle = colorHex || '#1a0b2e';
  ctx.fillRect(0, 0, size, size);

  // Tactile leather / kraft fine grain noise
  const imgData = ctx.getImageData(0, 0, size, size);
  const data = imgData.data;
  for (let i = 0; i < data.length; i += 4) {
    const noise = (Math.random() - 0.5) * 20;
    data[i] = Math.min(255, Math.max(0, data[i] + noise));
    data[i + 1] = Math.min(255, Math.max(0, data[i + 1] + noise));
    data[i + 2] = Math.min(255, Math.max(0, data[i + 2] + noise));
  }
  ctx.putImageData(imgData, 0, 0);

  // Luxurious embossed gold foil borders
  ctx.strokeStyle = '#d4af37';
  ctx.lineWidth = 10;
  ctx.strokeRect(40, 40, size - 80, size - 80);

  ctx.lineWidth = 3.5;
  ctx.strokeRect(58, 58, size - 116, size - 116);

  // Corner Ornaments
  const corners = [
    [70, 70], [size - 70, 70], [70, size - 70], [size - 70, size - 70]
  ];
  ctx.fillStyle = '#facc15';
  corners.forEach(([cx, cy]) => {
    ctx.beginPath();
    ctx.arc(cx, cy, 9, 0, Math.PI * 2);
    ctx.fill();
  });

  if (isFront) {
    // Embossed Gold Title & Brand Emblem
    ctx.textAlign = 'center';
    ctx.shadowColor = 'rgba(0,0,0,0.55)';
    ctx.shadowBlur = 10;
    ctx.shadowOffsetX = 3;
    ctx.shadowOffsetY = 4;

    ctx.fillStyle = '#fde047';
    ctx.font = '900 48px "Playfair Display", "Times New Roman", serif';
    ctx.fillText(title.toUpperCase(), size / 2, size / 2 - 25);

    ctx.font = 'italic 700 26px "Patrick Hand", cursive';
    ctx.fillStyle = '#fef08a';
    ctx.fillText('✦ Every memory has a story ✦', size / 2, size / 2 + 30);

    ctx.font = 'bold 20px "Plus Jakarta Sans", sans-serif';
    ctx.fillStyle = '#e2e8f0';
    ctx.fillText('MEMOUR STUDIO CRAFT 2026', size / 2, size / 2 + 75);
  } else {
    // Back Cover: Brand mark & credits
    ctx.textAlign = 'center';
    ctx.fillStyle = '#fde047';
    ctx.font = 'italic 600 26px "Patrick Hand", cursive';
    ctx.fillText('Handcrafted with love by MEMOUR Studio', size / 2, size - 95);
    ctx.font = 'bold 18px monospace';
    ctx.fillText('memourscrapbook.com', size / 2, size - 65);
  }

  const texture = new THREE.CanvasTexture(canvasElem);
  texture.anisotropy = 16;
  return texture;
}

// ================= 3D INITIALIZATION =================
function init3DViewer() {
  const container = document.getElementById('threejs-container');
  if (!container || is3dInitialized) return;

  const width = container.clientWidth || 600;
  const height = container.clientHeight || 500;

  // 1. Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color('#f9f6f0');

  // 2. Camera (Hero 3/4 perspective)
  camera = new THREE.PerspectiveCamera(42, width / height, 0.1, 1000);
  camera.position.set(2.8, 3.8, 4.2);

  // 3. Renderer (with true sRGB Color fidelity)
  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputEncoding = THREE.sRGBEncoding; // Critical for 2D/3D color match
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;

  container.appendChild(renderer.domElement);

  // 4. Orbit Controls
  controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
  controls.maxDistance = 12;
  controls.minDistance = 1.8;
  controls.maxPolarAngle = Math.PI / 2 + 0.08; // Prevent looking from directly underneath
  controls.autoRotate = isAutoRotate;
  controls.autoRotateSpeed = 1.0;
  controls.target.set(0.3, 0, 0);

  // 5. Studio Multi-Point Lighting Rig
  // Ambient bounce
  const ambientLight = new THREE.AmbientLight(0xfffbeb, 0.85);
  scene.add(ambientLight);

  // Key light: Warm directional with soft shadow
  const keyLight = new THREE.DirectionalLight(0xfff7ed, 1.4);
  keyLight.position.set(4.0, 7.0, 4.5);
  keyLight.castShadow = true;
  keyLight.shadow.mapSize.width = 2048;
  keyLight.shadow.mapSize.height = 2048;
  keyLight.shadow.bias = -0.0002;
  keyLight.shadow.camera.near = 0.5;
  keyLight.shadow.camera.far = 25;
  keyLight.shadow.camera.left = -4;
  keyLight.shadow.camera.right = 4;
  keyLight.shadow.camera.top = 4;
  keyLight.shadow.camera.bottom = -4;
  scene.add(keyLight);

  // Fill light: Soft warm-tinted fill from front-left
  const fillLight = new THREE.DirectionalLight(0xfef3c7, 0.45);
  fillLight.position.set(-4.5, 3.5, 3.0);
  scene.add(fillLight);

  // Rim / Specular light: Cool rim light from upper rear to highlight rings & page bevels
  const rimLight = new THREE.DirectionalLight(0xecfeff, 0.6);
  rimLight.position.set(0, 5.5, -5.5);
  scene.add(rimLight);

  // 6. Studio Floor Contact Shadow
  const groundGeo = new THREE.PlaneGeometry(30, 30);
  const groundMat = new THREE.ShadowMaterial({ opacity: 0.18 });
  const ground = new THREE.Mesh(groundGeo, groundMat);
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -0.07;
  ground.receiveShadow = true;
  scene.add(ground);

  // 7. Build Model
  build3DScrapbookModel();

  // 8. Resize Listener
  window.addEventListener('resize', onWindowResize);

  is3dInitialized = true;
  animate3D();

  // Initial Sync from 2D
  setTimeout(syncTo3DViewer, 80);
}

// ================= BUILD 3D SCRAPBOOK MODEL =================
function build3DScrapbookModel() {
  if (bookGroup) scene.remove(bookGroup);

  bookGroup = new THREE.Group();
  paperGrainTexture = createPaperGrainTexture();

  // 2D Fabric Canvas Texture
  const fabricCanvasElem = document.getElementById('scrapbook-fabric-canvas');
  if (fabricCanvasElem) {
    canvasTexture = new THREE.CanvasTexture(fabricCanvasElem);
    canvasTexture.anisotropy = 16;
    canvasTexture.generateMipmaps = true;
    canvasTexture.encoding = THREE.sRGBEncoding;
  }

  // Load Initial Front & Back Cover Textures
  loadInitialCoverTextures();

  // Initial Materials
  frontCoverMat = new THREE.MeshStandardMaterial({
    map: currentFrontCoverTexture,
    bumpMap: paperGrainTexture,
    bumpScale: 0.005,
    roughness: 0.85,
    metalness: 0.05
  });

  backCoverMat = new THREE.MeshStandardMaterial({
    map: currentBackCoverTexture,
    bumpMap: paperGrainTexture,
    bumpScale: 0.005,
    roughness: 0.85,
    metalness: 0.05
  });

  // Inside Left Page Material (Color Synchronized dynamically)
  innerCraftSpreadMat = new THREE.MeshStandardMaterial({
    color: 0xe8d8c3,
    bumpMap: paperGrainTexture,
    bumpScale: 0.004,
    roughness: 0.95,
    metalness: 0.0
  });

  // Paper Block Edge Material
  pageEdgeMat = new THREE.MeshStandardMaterial({
    color: 0xecdcc8,
    bumpMap: paperGrainTexture,
    bumpScale: 0.003,
    roughness: 0.95,
    metalness: 0.0
  });

  // Active Canvas Material (Right Page)
  const activeCanvasMat = new THREE.MeshStandardMaterial({
    map: canvasTexture || null,
    bumpMap: paperGrainTexture,
    bumpScale: 0.003,
    color: 0xffffff,
    roughness: 0.92,
    metalness: 0.0
  });

  const pageW = 2.4;
  const pageH = 2.4 / bookAspectRatio;
  const pageThickness = 0.07;

  // ---------------- RIGHT PAGE (ACTIVE 2D CANVAS) ----------------
  const rightPageGeo = new THREE.BoxGeometry(pageW, pageThickness, pageH, 20, 2, 20);
  const posAttr = rightPageGeo.attributes.position;
  for (let i = 0; i < posAttr.count; i++) {
    const x = posAttr.getX(i);
    const y = posAttr.getY(i);
    const spineDist = (x + pageW / 2) / pageW;
    posAttr.setY(i, y + Math.sin(spineDist * Math.PI) * 0.015);
  }
  rightPageGeo.computeVertexNormals();

  pageMesh = new THREE.Mesh(rightPageGeo, [
    pageEdgeMat,       // +x right
    pageEdgeMat,       // -x spine
    activeCanvasMat,   // +y TOP (Inside Active Spread)
    backCoverMat,      // -y BOTTOM (Outside Back Cover)
    pageEdgeMat,       // +z front
    pageEdgeMat        // -z back
  ]);
  pageMesh.position.set(pageW / 2 + 0.05, 0, 0);
  pageMesh.castShadow = true;
  pageMesh.receiveShadow = true;
  bookGroup.add(pageMesh);

  // ---------------- LEFT COVER / PAGE PIVOT ----------------
  leftCoverPivot = new THREE.Group();
  leftCoverPivot.position.set(0, 0, 0);

  const leftPageGeo = new THREE.BoxGeometry(pageW, pageThickness, pageH, 20, 2, 20);
  const leftPosAttr = leftPageGeo.attributes.position;
  for (let i = 0; i < leftPosAttr.count; i++) {
    const x = leftPosAttr.getX(i);
    const y = leftPosAttr.getY(i);
    const spineDist = (pageW / 2 - x) / pageW;
    leftPosAttr.setY(i, y + Math.sin(spineDist * Math.PI) * 0.015);
  }
  leftPageGeo.computeVertexNormals();

  leftPageMesh = new THREE.Mesh(leftPageGeo, [
    pageEdgeMat,          // +x spine
    pageEdgeMat,          // -x left
    innerCraftSpreadMat,  // +y TOP (Inside Left Spread Sheet)
    frontCoverMat,        // -y BOTTOM (Outside Front Cover)
    pageEdgeMat,          // +z front
    pageEdgeMat           // -z back
  ]);
  leftPageMesh.position.set(-(pageW / 2 + 0.05), 0, 0);
  leftPageMesh.castShadow = true;
  leftPageMesh.receiveShadow = true;
  leftCoverPivot.add(leftPageMesh);

  bookGroup.add(leftCoverPivot);

  // ---------------- DYNAMIC RINGS & SPINE BINDING ----------------
  build3DRingsForSku(currentBookSku || 'SCR-001', pageH);

  // ---------------- 3D PHYSICAL SOLID STICKERS RELIEF ----------------
  stickers3DGroup = new THREE.Group();
  bookGroup.add(stickers3DGroup);

  scene.add(bookGroup);
}

function loadInitialCoverTextures() {
  const textureLoader = new THREE.TextureLoader();
  const skuKey = (currentBookSku || 'SCR-001').toLowerCase().replace('-', '_');

  currentFrontCoverTexture = textureLoader.load(
    `/static/assets/books/${skuKey}_front.svg`,
    (tex) => {
      tex.encoding = THREE.sRGBEncoding;
      tex.anisotropy = 8;
      tex.center.set(0.5, 0.5);
      tex.rotation = Math.PI;
    },
    undefined,
    () => {
      // Fallback procedural
      currentFrontCoverTexture = createProceduralCoverTexture('#1a0b2e', 'MEMOUR SCRAPBOOK', true);
      if (frontCoverMat) frontCoverMat.map = currentFrontCoverTexture;
    }
  );

  currentBackCoverTexture = textureLoader.load(
    `/static/assets/books/${skuKey}_back.svg`,
    (tex) => {
      tex.encoding = THREE.sRGBEncoding;
      tex.anisotropy = 8;
      tex.center.set(0.5, 0.5);
      tex.rotation = 0;
    },
    undefined,
    () => {
      currentBackCoverTexture = createProceduralCoverTexture('#1a0b2e', 'MEMOUR SCRAPBOOK', false);
      if (backCoverMat) backCoverMat.map = currentBackCoverTexture;
    }
  );
}

// ================= DYNAMIC METAL RINGS & BINDINGS PER SKU =================
function build3DRingsForSku(bookSku, pageH) {
  if (ringsGroup) bookGroup.remove(ringsGroup);
  if (spineMesh) bookGroup.remove(spineMesh);

  ringsGroup = new THREE.Group();
  const skuUpper = (bookSku || 'SCR-001').toUpperCase();
  const halfH = pageH / 2 - 0.2;

  let ringColor, ringRoughness, ringMetalness;

  if (skuUpper === 'SCR-002' || skuUpper === 'SCR-TT-001') {
    // Twin Spiral Wire Silver Chrome
    ringColor = 0xf1f5f9;
    ringRoughness = 0.12;
    ringMetalness = 0.98;
    const ringGeo = new THREE.TorusGeometry(0.17, 0.016, 16, 32);
    const ringMat = new THREE.MeshStandardMaterial({
      color: ringColor,
      roughness: ringRoughness,
      metalness: ringMetalness
    });
    const step = 0.22;
    for (let z = -halfH; z <= halfH; z += step) {
      const ring1 = new THREE.Mesh(ringGeo, ringMat);
      ring1.rotation.y = Math.PI / 2;
      ring1.position.set(0, 0.088, z - 0.04);
      ring1.castShadow = true;
      ringsGroup.add(ring1);

      const ring2 = new THREE.Mesh(ringGeo, ringMat);
      ring2.rotation.y = Math.PI / 2;
      ring2.position.set(0, 0.088, z + 0.04);
      ring2.castShadow = true;
      ringsGroup.add(ring2);
    }
  } else if (skuUpper === 'SCR-003' || skuUpper === 'SCR-HW-001') {
    // Gunmetal Black / Deep Purple Matte Rings
    ringColor = 0x27272a;
    ringRoughness = 0.35;
    ringMetalness = 0.88;
    const boxRingGeo = new THREE.BoxGeometry(0.04, 0.22, 0.07);
    const ringMat = new THREE.MeshStandardMaterial({
      color: ringColor,
      roughness: ringRoughness,
      metalness: ringMetalness
    });
    const step = 0.32;
    for (let z = -halfH; z <= halfH; z += step) {
      const ring = new THREE.Mesh(boxRingGeo, ringMat);
      ring.position.set(0, 0.085, z);
      ring.castShadow = true;
      ringsGroup.add(ring);
    }
  } else if (skuUpper === 'SCR-HW-002' || skuUpper === 'SCR-HW-003') {
    // Emerald / Antique Witchcraft Gold Torus
    ringColor = 0xeab308;
    ringRoughness = 0.22;
    ringMetalness = 0.92;
    const ringGeo = new THREE.TorusGeometry(0.18, 0.024, 16, 32);
    const ringMat = new THREE.MeshStandardMaterial({
      color: ringColor,
      roughness: ringRoughness,
      metalness: ringMetalness
    });
    const step = 0.28;
    for (let z = -halfH; z <= halfH; z += step) {
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.rotation.y = Math.PI / 2;
      ring.position.set(0, 0.09, z);
      ring.castShadow = true;
      ringsGroup.add(ring);
    }
  } else {
    // SCR-001 (Kraft Classic FSC): Vintage Brushed Antique Brass Gold
    ringColor = 0xd4af37;
    ringRoughness = 0.25;
    ringMetalness = 0.92;
    const ringGeo = new THREE.TorusGeometry(0.18, 0.024, 16, 32);
    const ringMat = new THREE.MeshStandardMaterial({
      color: ringColor,
      roughness: ringRoughness,
      metalness: ringMetalness
    });
    const step = 0.28;
    for (let z = -halfH; z <= halfH; z += step) {
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.rotation.y = Math.PI / 2;
      ring.position.set(0, 0.09, z);
      ring.castShadow = true;
      ringsGroup.add(ring);
    }
  }

  bookGroup.add(ringsGroup);

  // Central Spine Cylinder
  const spineMat = new THREE.MeshStandardMaterial({
    color: ringColor,
    roughness: ringRoughness,
    metalness: ringMetalness
  });
  const spineGeo = new THREE.CylinderGeometry(0.035, 0.035, pageH, 16);
  spineMesh = new THREE.Mesh(spineGeo, spineMat);
  spineMesh.rotation.x = Math.PI / 2;
  spineMesh.position.set(0, 0.015, 0);
  bookGroup.add(spineMesh);
}

// ================= REAL-TIME 2D/3D COLOR & ASSET SYNCHRONIZATION =================
function syncTo3DViewer() {
  if (!is3dInitialized) return;

  // 1. Update 2D Canvas Texture on Right Page
  if (canvasTexture) {
    canvasTexture.needsUpdate = true;
  }

  // 2. Synchronize Left Page Color & Spread Aesthetics
  let currentBgColor = '#e8d8c3';
  let currentBgPattern = null;

  if (typeof canvas !== 'undefined' && canvas) {
    if (typeof canvas.backgroundColor === 'string' && canvas.backgroundColor) {
      currentBgColor = canvas.backgroundColor;
    }
    if (canvas.backgroundImage && canvas.backgroundImage._element && canvas.backgroundImage._element.src) {
      currentBgPattern = canvas.backgroundImage._element.src;
    }
  }

  if (leftPageMesh && Array.isArray(leftPageMesh.material)) {
    const leftMat = leftPageMesh.material[2];
    if (leftMat) {
      // Check if previous page has a rendered snapshot
      const prevPageIdx = (typeof activePageIndex !== 'undefined') ? activePageIndex - 1 : -1;
      if (prevPageIdx >= 0 && window.pageSnapshots && window.pageSnapshots.has(prevPageIdx)) {
        const snapUrl = window.pageSnapshots.get(prevPageIdx);
        if (snapUrl) {
          const snapLoader = new THREE.TextureLoader();
          snapLoader.load(snapUrl, (snapTex) => {
            snapTex.encoding = THREE.sRGBEncoding;
            snapTex.anisotropy = 8;
            leftMat.map = snapTex;
            leftMat.color.set(0xffffff);
            leftMat.needsUpdate = true;
          });
        }
      } else {
        // Cohesive spread: match exact background color & pattern of right page
        leftMat.map = null;
        try {
          leftMat.color.setStyle(currentBgColor);
        } catch (e) {
          leftMat.color.set(0xe8d8c3);
        }
        leftMat.needsUpdate = true;
      }
    }
  }

  // 3. Harmonize Paper Edge Block Colors
  if (pageMesh && Array.isArray(pageMesh.material)) {
    const isDark = isDarkHexColor(currentBgColor);
    const edgeColor = isDark ? 0x27272a : 0xecdcc8;
    [0, 1, 4, 5].forEach(idx => {
      if (pageMesh.material[idx]) {
        pageMesh.material[idx].color.set(edgeColor);
      }
    });
  }

  // 4. Update Physical 3D Tactile Relief
  syncPhysical3DStickers();
}

function isDarkHexColor(hex) {
  if (!hex || typeof hex !== 'string') return false;
  let c = hex.replace('#', '');
  if (c.length === 3) c = c.split('').map(x => x + x).join('');
  const num = parseInt(c, 16);
  if (isNaN(num)) return false;
  const r = (num >> 16) & 255;
  const g = (num >> 8) & 255;
  const b = num & 255;
  // Perceived luminance
  const luminance = (0.299 * r + 0.587 * g + 0.114 * b);
  return luminance < 128;
}

// ================= 3D GROUNDED PHYSICAL TACTILE RELIEF (0.4MM EMBOSSED) =================
function syncPhysical3DStickers() {
  if (!stickers3DGroup || typeof canvas === 'undefined' || !canvas) return;

  while (stickers3DGroup.children.length > 0) {
    const child = stickers3DGroup.children[0];
    if (child.geometry) child.geometry.dispose();
    if (child.material) {
      if (Array.isArray(child.material)) child.material.forEach(m => m.dispose());
      else child.material.dispose();
    }
    stickers3DGroup.remove(child);
  }

  if (isBookClosed && foldProgress > 0.85) return;

  const objects = canvas.getObjects();
  const textureLoader = new THREE.TextureLoader();
  const cW = canvas.width || 500;
  const cH = canvas.height || 708;

  objects.forEach((obj, idx) => {
    if (!obj) return;

    if (obj.type === 'image' || obj.sku || obj._element || obj.type === 'i-text' || obj.type === 'text') {
      const scaledW = obj.getScaledWidth() || 120;
      const scaledH = obj.getScaledHeight() || 120;
      const objW3D = (scaledW / cW) * 2.3;
      const objH3D = (scaledH / cH) * (2.3 / bookAspectRatio);
      
      const posX = 1.25 + ((obj.left - cW / 2) / (cW / 2)) * 1.15;
      const posZ = ((obj.top - cH / 2) / (cH / 2)) * (1.15 / bookAspectRatio);
      const rotY = -obj.angle * (Math.PI / 180);
      
      const isSticker = (obj.itemCategory === 'sticker' || (obj.sku && obj.sku.startsWith('STK')));
      
      const baseElevation = 0.036 + (idx * 0.0008);
      const reliefThickness = isSticker ? 0.016 : 0.009;

      let srcUrl = null;
      if (obj._element && obj._element.src) {
        srcUrl = obj._element.src;
      } else if (obj.getSrc && typeof obj.getSrc === 'function') {
        srcUrl = obj.getSrc();
      }

      if (!srcUrl) return;

      const stickerTexture = textureLoader.load(srcUrl);
      stickerTexture.encoding = THREE.sRGBEncoding;
      stickerTexture.anisotropy = 8;
      stickerTexture.generateMipmaps = true;

      // 1. Top Relief Face (Clearcoat Resin / Vinyl Gloss)
      const solidGeo = new THREE.PlaneGeometry(objW3D, objH3D);
      const solidMat = new THREE.MeshPhysicalMaterial({
        map: stickerTexture,
        transparent: true,
        alphaTest: 0.05,
        depthWrite: true,
        roughness: isSticker ? 0.16 : 0.38,
        metalness: isSticker ? 0.20 : 0.0,
        clearcoat: isSticker ? 0.95 : 0.3,
        clearcoatRoughness: 0.08,
        reflectivity: 0.65,
        side: THREE.DoubleSide
      });

      const solidMesh = new THREE.Mesh(solidGeo, solidMat);
      solidMesh.rotation.x = -Math.PI / 2;
      solidMesh.rotation.z = rotY;
      solidMesh.position.set(posX, baseElevation + reliefThickness, posZ);
      solidMesh.castShadow = true;

      stickers3DGroup.add(solidMesh);

      // 2. Direct Flush Contact Shadow on Paper Substrate
      const shadowMat = new THREE.MeshBasicMaterial({
        map: stickerTexture,
        transparent: true,
        color: 0x221308,
        opacity: isSticker ? 0.36 : 0.22,
        alphaTest: 0.05,
        depthWrite: false,
        side: THREE.DoubleSide
      });

      const shadowMesh = new THREE.Mesh(solidGeo, shadowMat);
      shadowMesh.rotation.x = -Math.PI / 2;
      shadowMesh.rotation.z = rotY;
      shadowMesh.position.set(posX + 0.006, baseElevation + 0.0008, posZ + 0.008);

      stickers3DGroup.add(shadowMesh);
    }
  });
}

// ================= DYNAMIC 3D COVER DESIGN =================
function change3DCoverDesign(bookSku, imageUrl, colorHex) {
  currentBookSku = bookSku;
  const textureLoader = new THREE.TextureLoader();
  const skuKey = bookSku.toLowerCase().replace('-', '_');

  const frontUrl = imageUrl || `/static/assets/books/${skuKey}_front.svg`;
  const backUrl = `/static/assets/books/${skuKey}_back.svg`;

  textureLoader.load(
    frontUrl,
    (frontTex) => {
      frontTex.encoding = THREE.sRGBEncoding;
      frontTex.anisotropy = 8;
      frontTex.center.set(0.5, 0.5);
      frontTex.rotation = Math.PI;
      currentFrontCoverTexture = frontTex;

      if (leftPageMesh && Array.isArray(leftPageMesh.material)) {
        leftPageMesh.material[3].map = frontTex;
        leftPageMesh.material[3].needsUpdate = true;
      }
    },
    undefined,
    () => {
      // Fallback procedural luxury foil cover
      const fallbackTex = createProceduralCoverTexture(colorHex || '#1a0b2e', bookSku, true);
      currentFrontCoverTexture = fallbackTex;
      if (leftPageMesh && Array.isArray(leftPageMesh.material)) {
        leftPageMesh.material[3].map = fallbackTex;
        leftPageMesh.material[3].needsUpdate = true;
      }
    }
  );

  textureLoader.load(
    backUrl,
    (backTex) => {
      backTex.encoding = THREE.sRGBEncoding;
      backTex.anisotropy = 8;
      backTex.center.set(0.5, 0.5);
      backTex.rotation = 0;
      currentBackCoverTexture = backTex;

      if (pageMesh && Array.isArray(pageMesh.material)) {
        pageMesh.material[3].map = backTex;
        pageMesh.material[3].needsUpdate = true;
      }
    },
    undefined,
    () => {
      const fallbackTex = createProceduralCoverTexture(colorHex || '#1a0b2e', bookSku, false);
      currentBackCoverTexture = fallbackTex;
      if (pageMesh && Array.isArray(pageMesh.material)) {
        pageMesh.material[3].map = fallbackTex;
        pageMesh.material[3].needsUpdate = true;
      }
    }
  );

  // Update Rings according to selected Book SKU
  const pageH = 2.4 / bookAspectRatio;
  build3DRingsForSku(bookSku, pageH);
}

function update3DBookDimensions(aspectRatio) {
  bookAspectRatio = aspectRatio || 0.7062;
  if (is3dInitialized) {
    build3DScrapbookModel();
    syncTo3DViewer();
  }
}

// ================= BOOK FOLDING / CLOSING MECHANICS =================
function toggleFoldBook() {
  if (isAnimatingFold) return;

  isBookClosed = !isBookClosed;
  isAnimatingFold = true;

  const btn = document.getElementById('btn-toggle-fold');
  if (btn) {
    btn.innerHTML = isBookClosed
      ? '<span>📖 Mở Sổ Thiết Kế</span>'
      : '<span>📕 Gấp Sổ Lại</span>';
  }

  const targetProgress = isBookClosed ? 1.0 : 0.0;
  const startProgress = foldProgress;
  const startTime = performance.now();
  const duration = 750;

  function animateFoldStep(now) {
    const elapsed = now - startTime;
    const t = Math.min(1.0, elapsed / duration);
    const ease = t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1;

    foldProgress = startProgress + (targetProgress - startProgress) * ease;

    if (leftCoverPivot) {
      leftCoverPivot.rotation.z = -foldProgress * Math.PI;
      leftCoverPivot.position.y = foldProgress * 0.075;
    }

    if (t < 1.0) {
      requestAnimationFrame(animateFoldStep);
    } else {
      isAnimatingFold = false;
      syncPhysical3DStickers();
      if (isBookClosed) {
        set3DViewAngle('cover');
        showToast('Đã gấp sổ • Bìa trước ngay ngắn ở trên, bìa sau ở dưới!', 'info');
      } else {
        set3DViewAngle('spread');
        showToast('Đã mở sổ • Trải rộng 2 trang thiết kế!', 'info');
      }
    }
  }

  requestAnimationFrame(animateFoldStep);
}

// ================= 3D PAGE FLIP: UPWARD ARCH IN THE AIR =================
function flipPage3D(direction = 1) {
  if (isFlippingPage) return;

  if (!studioPages || studioPages.length <= 1) {
    showToast('Cuốn sổ hiện chỉ có 1 trang, hãy bấm "+ Thêm Trang" ở thanh dưới để mở rộng!', 'info');
    return;
  }

  const targetIdx = activePageIndex + direction;

  if (targetIdx < 0) {
    showToast('✦ Bạn đang ở Trang 1 (Trang đầu tiên của cuốn sổ)', 'info');
    return;
  }

  if (targetIdx >= studioPages.length) {
    showToast(`✦ Đã đến Trang ${studioPages.length} (Trang cuối cùng)! Bấm "+ Thêm Trang" để tạo thêm trang mới`, 'info');
    return;
  }

  isFlippingPage = true;

  if (typeof saveCurrentPageData === 'function') saveCurrentPageData();

  const pageW = 2.4;
  const pageH = 2.4 / bookAspectRatio;

  const turningGeo = new THREE.PlaneGeometry(pageW, pageH, 24, 4);
  const posAttr = turningGeo.attributes.position;
  for (let i = 0; i < posAttr.count; i++) {
    const x = posAttr.getX(i);
    const normX = (x + pageW / 2) / pageW;
    posAttr.setZ(i, Math.sin(normX * Math.PI) * 0.04);
  }
  turningGeo.computeVertexNormals();

  const turningPivot = new THREE.Group();
  turningPivot.position.set(0, 0.082, 0);

  const pageMatFront = new THREE.MeshStandardMaterial({
    map: canvasTexture || null,
    bumpMap: paperGrainTexture,
    bumpScale: 0.003,
    roughness: 0.95,
    side: THREE.FrontSide
  });

  const pageMatBack = new THREE.MeshStandardMaterial({
    color: 0xfdfbf7,
    bumpMap: paperGrainTexture,
    bumpScale: 0.004,
    roughness: 0.95,
    side: THREE.BackSide
  });

  const frontMesh = new THREE.Mesh(turningGeo, pageMatFront);
  frontMesh.rotation.x = -Math.PI / 2;
  frontMesh.position.set(pageW / 2, 0, 0);

  const backMesh = new THREE.Mesh(turningGeo, pageMatBack);
  backMesh.rotation.x = -Math.PI / 2;
  backMesh.position.set(pageW / 2, 0, 0);

  turningPivot.add(frontMesh);
  turningPivot.add(backMesh);
  bookGroup.add(turningPivot);

  const startTime = performance.now();
  const duration = 650;

  function animateFlip(now) {
    const elapsed = now - startTime;
    const t = Math.min(1.0, elapsed / duration);
    const ease = t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;

    if (direction > 0) {
      turningPivot.rotation.z = ease * Math.PI;
    } else {
      turningPivot.rotation.z = (1.0 - ease) * Math.PI;
    }

    if (t < 1.0) {
      requestAnimationFrame(animateFlip);
    } else {
      bookGroup.remove(turningPivot);
      turningGeo.dispose();
      pageMatFront.dispose();
      pageMatBack.dispose();
      isFlippingPage = false;
      if (typeof switchPage === 'function') switchPage(targetIdx);
    }
  }

  requestAnimationFrame(animateFlip);
}

// ================= SMOOTH CAMERA CINEMATICS =================
function animateCameraTo(targetPos, targetLookAt, duration = 600) {
  if (!camera || !controls) return;
  if (cameraAnimFrame) cancelAnimationFrame(cameraAnimFrame);

  const startPos = camera.position.clone();
  const startLookAt = controls.target.clone();
  const startTime = performance.now();

  function step(now) {
    const elapsed = now - startTime;
    const t = Math.min(1.0, elapsed / duration);
    const ease = t < 0.5 ? 4 * t * t * t : (t - 1) * (2 * t - 2) * (2 * t - 2) + 1;

    camera.position.lerpVectors(startPos, targetPos, ease);
    controls.target.lerpVectors(startLookAt, targetLookAt, ease);
    controls.update();

    if (t < 1.0) {
      cameraAnimFrame = requestAnimationFrame(step);
    }
  }
  cameraAnimFrame = requestAnimationFrame(step);
}

function set3DViewAngle(angleType) {
  if (!camera || !controls) return;
  controls.autoRotate = false;

  let targetPos, targetLookAt;

  if (angleType === 'hero' || angleType === 'iso') {
    // 🌟 Góc 3/4 Nghệ Thuật
    targetPos = new THREE.Vector3(2.8, 3.6, 4.2);
    targetLookAt = new THREE.Vector3(0.3, 0, 0);
  } else if (angleType === 'spread' || angleType === 'front') {
    // 📖 Mặt Trong Trải Phẳng Trực Diện
    targetPos = new THREE.Vector3(0.0, 4.6, 2.8);
    targetLookAt = new THREE.Vector3(0.0, 0, 0);
  } else if (angleType === 'cover') {
    // 📕 Bìa Trước
    if (isBookClosed) {
      targetPos = new THREE.Vector3(0.0, 3.8, 2.0);
      targetLookAt = new THREE.Vector3(0.0, 0.06, 0);
    } else {
      targetPos = new THREE.Vector3(-1.3, 4.0, 2.2);
      targetLookAt = new THREE.Vector3(-1.3, 0, 0);
    }
  } else if (angleType === 'back') {
    // 📘 Bìa Sau
    if (isBookClosed) {
      targetPos = new THREE.Vector3(0.0, -3.8, -2.0);
      targetLookAt = new THREE.Vector3(0.0, 0, 0);
    } else {
      targetPos = new THREE.Vector3(1.3, -4.0, -2.0);
      targetLookAt = new THREE.Vector3(1.3, 0, 0);
    }
  } else if (angleType === 'macro') {
    // 🔍 Cận Cảnh Chi Tiết
    targetPos = new THREE.Vector3(1.1, 1.4, 1.6);
    targetLookAt = new THREE.Vector3(1.1, 0.05, 0.1);
  } else if (angleType === 'top') {
    targetPos = new THREE.Vector3(0.0, 6.0, 0.05);
    targetLookAt = new THREE.Vector3(0.0, 0, 0);
  }

  if (targetPos && targetLookAt) {
    animateCameraTo(targetPos, targetLookAt, 650);
  }
}

function toggle3DAutoRotate() {
  isAutoRotate = !isAutoRotate;
  if (controls) controls.autoRotate = isAutoRotate;
  const btn = document.getElementById('btn-toggle-rotate');
  if (btn) {
    btn.innerHTML = isAutoRotate ? '<span>⏸ Dừng xoay</span>' : '<span>🔄 Tự động xoay 360°</span>';
  }
}

function onWindowResize() {
  const container = document.getElementById('threejs-container');
  if (!container || !camera || !renderer) return;

  const width = container.clientWidth;
  const height = container.clientHeight;

  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
}

function animate3D() {
  requestAnimationFrame(animate3D);

  const container = document.getElementById('threejs-container');
  if (document.hidden || !container || container.offsetParent === null) return;

  if (controls) controls.update();
  if (renderer && scene && camera) {
    renderer.render(scene, camera);
  }
}

// ================= VIEW SWITCHER =================
function switchStudioView(mode) {
  const mode2D = document.getElementById('studio-2d-panel');
  const mode3D = document.getElementById('studio-3d-panel');
  const btn2D = document.getElementById('tab-btn-2d');
  const btn3D = document.getElementById('tab-btn-3d');

  if (mode === '3d') {
    if (mode2D) mode2D.classList.add('hidden');
    if (mode3D) mode3D.classList.remove('hidden');
    if (btn2D) btn2D.className = 'flex-1 sm:flex-none px-3 sm:px-5 py-1.5 rounded-xl font-heading font-black text-[11px] sm:text-xs border-2 border-black bg-white text-stone-900 hover:bg-stone-100 transition-all';
    if (btn3D) btn3D.className = 'flex-1 sm:flex-none px-3 sm:px-5 py-1.5 rounded-xl font-heading font-black text-[11px] sm:text-xs border-2 border-black bg-rose-800 text-white shadow-neo transition-all flex items-center justify-center gap-1.5';

    if (!is3dInitialized) {
      setTimeout(init3DViewer, 50);
    } else {
      setTimeout(onWindowResize, 50);
      syncTo3DViewer();
    }
  } else {
    if (mode2D) mode2D.classList.remove('hidden');
    if (mode3D) mode3D.classList.add('hidden');
    if (btn2D) btn2D.className = 'flex-1 sm:flex-none px-3 sm:px-5 py-1.5 rounded-xl font-heading font-black text-[11px] sm:text-xs border-2 border-black bg-rose-800 text-white shadow-neo transition-all';
    if (btn3D) btn3D.className = 'flex-1 sm:flex-none px-3 sm:px-5 py-1.5 rounded-xl font-heading font-black text-[11px] sm:text-xs border-2 border-black bg-white text-stone-900 hover:bg-amber-100 transition-all flex items-center justify-center gap-1.5';
  }
}

// Global Exports
window.init3DViewer = init3DViewer;
window.syncTo3DViewer = syncTo3DViewer;
window.change3DCoverDesign = change3DCoverDesign;
window.update3DBookDimensions = update3DBookDimensions;
window.toggleFoldBook = toggleFoldBook;
window.flipPage3D = flipPage3D;
window.set3DViewAngle = set3DViewAngle;
window.toggle3DAutoRotate = toggle3DAutoRotate;
window.switchStudioView = switchStudioView;
