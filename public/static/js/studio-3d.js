/**
 * ScrapCraft / MEMOUR Studio 2.0 - Three.js 3D Interactive Engine 360°
 * Distinct Front & Back Covers, 4 Distinct Metal Ring Styles per Book SKU,
 * Natural Upward-Arched 3D Page Flipping (y > 0), Grounded 0.4mm Solid Relief
 */

let scene, camera, renderer, controls;
let bookGroup, pageMesh, leftPageMesh, leftCoverPivot, spineMesh, ringsGroup, stickers3DGroup;
let canvasTexture = null;
let paperGrainTexture = null;
let currentFrontCoverTexture = null;
let currentBackCoverTexture = null;
let is3dInitialized = false;
let isAutoRotate = false;

// Book Folding State
let isBookClosed = false;
let isAnimatingFold = false;
let foldProgress = 0.0; // 0.0 = Open Spread (180° flat), 1.0 = Closed Book
let bookAspectRatio = 1.0;

// Page Flip State
let isFlippingPage = false;

function createPaperGrainTexture() {
  const size = 512;
  const canvasElem = document.createElement('canvas');
  canvasElem.width = size;
  canvasElem.height = size;
  const ctx = canvasElem.getContext('2d');
  
  // Warm Kraft Paper Base Tone
  ctx.fillStyle = '#f4ede2';
  ctx.fillRect(0, 0, size, size);
  
  // Organic noise grain
  const imgData = ctx.getImageData(0, 0, size, size);
  const data = imgData.data;
  for (let i = 0; i < data.length; i += 4) {
    const noise = (Math.random() - 0.5) * 14;
    data[i] = Math.min(255, Math.max(0, data[i] + noise));
    data[i + 1] = Math.min(255, Math.max(0, data[i + 1] + noise));
    data[i + 2] = Math.min(255, Math.max(0, data[i + 2] + noise));
  }
  ctx.putImageData(imgData, 0, 0);

  // Subtle paper fibers
  ctx.strokeStyle = 'rgba(120, 53, 15, 0.05)';
  ctx.lineWidth = 1;
  for (let i = 0; i < 30; i++) {
    ctx.beginPath();
    const x = Math.random() * size;
    const y = Math.random() * size;
    ctx.moveTo(x, y);
    ctx.lineTo(x + (Math.random() - 0.5) * 25, y + (Math.random() - 0.5) * 25);
    ctx.stroke();
  }

  const texture = new THREE.CanvasTexture(canvasElem);
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.repeat.set(3, 3);
  return texture;
}

function init3DViewer() {
  const container = document.getElementById('threejs-container');
  if (!container || is3dInitialized) return;

  const width = container.clientWidth || 500;
  const height = container.clientHeight || 500;

  // 1. Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color('#fdfbf7');

  // 2. Camera
  camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
  camera.position.set(0, 4.2, 6.2);

  // 3. Renderer
  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;

  container.appendChild(renderer.domElement);

  // 4. Orbit Controls
  controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.06;
  controls.maxDistance = 14;
  controls.minDistance = 2.0;
  controls.maxPolarAngle = Math.PI / 2 + 0.15;
  controls.autoRotate = isAutoRotate;
  controls.autoRotateSpeed = 1.2;

  // 5. Lighting Setup
  const ambientLight = new THREE.AmbientLight(0xfffbeb, 0.95);
  scene.add(ambientLight);

  const mainLight = new THREE.DirectionalLight(0xfff7ed, 1.45);
  mainLight.position.set(3.5, 7.5, 4.5);
  mainLight.castShadow = true;
  mainLight.shadow.mapSize.width = 2048;
  mainLight.shadow.mapSize.height = 2048;
  mainLight.shadow.bias = -0.0003;
  scene.add(mainLight);

  const fillLight = new THREE.DirectionalLight(0xf5ebe0, 0.65);
  fillLight.position.set(-4.5, 4.5, -3.5);
  scene.add(fillLight);

  // 6. Ground Shadow Receiver Plane
  const groundGeo = new THREE.PlaneGeometry(28, 28);
  const groundMat = new THREE.ShadowMaterial({ opacity: 0.15 });
  const ground = new THREE.Mesh(groundGeo, groundMat);
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -0.55;
  ground.receiveShadow = true;
  scene.add(ground);

  // 7. Build Model
  build3DScrapbookModel();

  // 8. Resize Listener
  window.addEventListener('resize', onWindowResize);

  is3dInitialized = true;
  animate3D();
}

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
  }

  // Load DISTINCT Front & Back Cover Textures
  const textureLoader = new THREE.TextureLoader();
  const skuKey = (currentBookSku || 'scr_001').toLowerCase().replace('-', '_');
  
  currentFrontCoverTexture = textureLoader.load(`/static/assets/books/${skuKey}_front.svg`);
  currentFrontCoverTexture.anisotropy = 8;
  currentFrontCoverTexture.center.set(0.5, 0.5);
  currentFrontCoverTexture.rotation = Math.PI;

  currentBackCoverTexture = textureLoader.load(`/static/assets/books/${skuKey}_back.svg`);
  currentBackCoverTexture.anisotropy = 8;
  currentBackCoverTexture.center.set(0.5, 0.5);
  currentBackCoverTexture.rotation = 0;

  // ---------------- MATERIALS ----------------
  const frontCoverMat = new THREE.MeshStandardMaterial({
    map: currentFrontCoverTexture,
    bumpMap: paperGrainTexture,
    bumpScale: 0.005,
    roughness: 0.9,
    metalness: 0.0
  });

  const backCoverMat = new THREE.MeshStandardMaterial({
    map: currentBackCoverTexture,
    bumpMap: paperGrainTexture,
    bumpScale: 0.005,
    roughness: 0.9,
    metalness: 0.0
  });

  const innerCraftSpreadMat = new THREE.MeshStandardMaterial({
    color: 0xe8d8c3,
    bumpMap: paperGrainTexture,
    bumpScale: 0.004,
    roughness: 0.96,
    metalness: 0.0
  });

  const pageEdgeMat = new THREE.MeshStandardMaterial({
    color: 0xecdcc8,
    bumpMap: paperGrainTexture,
    bumpScale: 0.003,
    roughness: 0.95,
    metalness: 0.0
  });

  const activeCanvasMat = new THREE.MeshStandardMaterial({
    map: canvasTexture || null,
    bumpMap: paperGrainTexture,
    bumpScale: 0.003,
    color: 0xffffff,
    roughness: 0.95,
    metalness: 0.0
  });

  const pageW = 2.4;
  const pageH = 2.4 / bookAspectRatio;
  const pageThickness = 0.07;

  // ---------------- RIGHT WING ----------------
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
    backCoverMat,      // -y BOTTOM (OUTSIDE BACK COVER)
    pageEdgeMat,       // +z front
    pageEdgeMat        // -z back
  ]);
  pageMesh.position.set(pageW / 2 + 0.05, 0, 0);
  pageMesh.castShadow = true;
  pageMesh.receiveShadow = true;
  bookGroup.add(pageMesh);

  // ---------------- LEFT WING PIVOT ----------------
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
    innerCraftSpreadMat,  // +y TOP (Inside Clean Craft Sheet)
    frontCoverMat,        // -y BOTTOM (OUTSIDE FRONT COVER EXTERIOR)
    pageEdgeMat,          // +z front
    pageEdgeMat           // -z back
  ]);
  leftPageMesh.position.set(-(pageW / 2 + 0.05), 0, 0);
  leftPageMesh.castShadow = true;
  leftPageMesh.receiveShadow = true;
  leftCoverPivot.add(leftPageMesh);

  bookGroup.add(leftCoverPivot);

  // ---------------- DYNAMIC METAL RINGS & SPINAL BINDING PER SKU ----------------
  build3DRingsForSku(currentBookSku || 'SCR-001', pageH);

  // ---------------- 3D PHYSICAL UNIFIED SOLID STICKERS (0.4mm GROUNDED RELIEF) ----------------
  stickers3DGroup = new THREE.Group();
  bookGroup.add(stickers3DGroup);

  scene.add(bookGroup);

  syncPhysical3DStickers();
}

function build3DRingsForSku(bookSku, pageH) {
  if (ringsGroup) bookGroup.remove(ringsGroup);
  if (spineMesh) bookGroup.remove(spineMesh);

  ringsGroup = new THREE.Group();
  const skuUpper = (bookSku || 'SCR-001').toUpperCase();
  const halfH = pageH / 2 - 0.2;

  if (skuUpper === 'SCR-002') {
    // PASTEL HOLOGRAM: Twin Spiral Wire Silver Chrome (Lò xo xoắn kép bạc sáng)
    const ringGeo = new THREE.TorusGeometry(0.17, 0.016, 16, 32);
    const ringMat = new THREE.MeshStandardMaterial({
      color: 0xe2e8f0,
      roughness: 0.12,
      metalness: 0.98
    });
    const step = 0.22;
    for (let z = -halfH; z <= halfH; z += step) {
      // Double coil pair
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
  } else if (skuUpper === 'SCR-003') {
    // VELVET DARK: Square / Flat Gunmetal Black Rings (Còng vuông súng đen)
    const boxRingGeo = new THREE.BoxGeometry(0.04, 0.22, 0.07);
    const ringMat = new THREE.MeshStandardMaterial({
      color: 0x27272a,
      roughness: 0.38,
      metalness: 0.88
    });
    const step = 0.32;
    for (let z = -halfH; z <= halfH; z += step) {
      const ring = new THREE.Mesh(boxRingGeo, ringMat);
      ring.position.set(0, 0.085, z);
      ring.castShadow = true;
      ringsGroup.add(ring);
    }
  } else if (skuUpper === 'SCR-004') {
    // VINTAGE LINEN: Antique Bronze Rivets & Rings (Cúc bấm khuyên đồng đỏ)
    const ringGeo = new THREE.TorusGeometry(0.19, 0.028, 16, 32);
    const ringMat = new THREE.MeshStandardMaterial({
      color: 0xb45309,
      roughness: 0.3,
      metalness: 0.88
    });
    const step = 0.30;
    for (let z = -halfH; z <= halfH; z += step) {
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.rotation.y = Math.PI / 2;
      ring.position.set(0, 0.092, z);
      ring.castShadow = true;
      ringsGroup.add(ring);
    }
  } else {
    // SCR-001 (Kraft FSC): Vintage Antique Brass Gold Torus (Đồng thau cổ điển)
    const ringGeo = new THREE.TorusGeometry(0.18, 0.024, 16, 32);
    const ringMat = new THREE.MeshStandardMaterial({
      color: 0xd4af37,
      roughness: 0.25,
      metalness: 0.92
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

  // Spine Central Rod
  const spineMat = new THREE.MeshStandardMaterial({
    color: (skuUpper === 'SCR-002') ? 0xe2e8f0 : (skuUpper === 'SCR-003') ? 0x27272a : (skuUpper === 'SCR-004') ? 0xb45309 : 0xd4af37,
    roughness: 0.25,
    metalness: 0.9
  });
  const spineGeo = new THREE.CylinderGeometry(0.035, 0.035, pageH, 16);
  spineMesh = new THREE.Mesh(spineGeo, spineMat);
  spineMesh.rotation.x = Math.PI / 2;
  spineMesh.position.set(0, 0.015, 0);
  bookGroup.add(spineMesh);
}

// ================= 3D GROUNDED SOLID RELIEF (0.4MM EMBOSSED ON PAPER) =================
function syncTo3DViewer() {
  if (canvasTexture) {
    canvasTexture.needsUpdate = true;
  }
  syncPhysical3DStickers();
}

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
  const cW = canvas.width || 600;
  const cH = canvas.height || 600;

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
      
      // Grounded 0.4mm solid relief attached flush on paper surface (y=0.035)
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
        metalness: isSticker ? 0.22 : 0.0,
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
        color: 0x2d1808,
        opacity: isSticker ? 0.38 : 0.24,
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
  const duration = 800;

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
        set3DViewAngle('front');
        showToast('Đã mở sổ • Trải rộng 2 trang thiết kế!', 'info');
      }
    }
  }

  requestAnimationFrame(animateFoldStep);
}

// ================= 3D PAGE FLIP: UPWARD ARCH IN THE AIR (y > 0) =================
function flipPage3D(direction = 1) {
  if (isFlippingPage) return;

  if (!studioPages || studioPages.length <= 1) {
    showToast('Cuốn sổ hiện chỉ có 1 trang, hãy bấm "+ Thêm Trang" ở thanh dưới để mở rộng!', 'info');
    return;
  }

  const targetIdx = activePageIndex + direction;

  // Boundary guards: NO infinite looping!
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

  // Pre-curved page leaf geometry
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

  // Dual-sided leaf
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

    // ROTATE UPWARD INTO THE AIR (y > 0):
    // Next Page (direction > 0): Angle goes from 0 to +Math.PI (swings from right up over spine to left)
    // Prev Page (direction < 0): Angle goes from +Math.PI to 0 (swings from left up over spine to right)
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

// ================= DYNAMIC 3D COVER & RING DESIGN =================
function change3DCoverDesign(bookSku) {
  currentBookSku = bookSku;
  const textureLoader = new THREE.TextureLoader();
  const skuKey = bookSku.toLowerCase().replace('-', '_');

  const frontCoverUrl = `/static/assets/books/${skuKey}_front.svg`;
  const backCoverUrl = `/static/assets/books/${skuKey}_back.svg`;

  textureLoader.load(frontCoverUrl, (frontTex) => {
    frontTex.anisotropy = 8;
    frontTex.center.set(0.5, 0.5);
    frontTex.rotation = Math.PI;
    currentFrontCoverTexture = frontTex;

    if (leftPageMesh && Array.isArray(leftPageMesh.material)) {
      leftPageMesh.material[3].map = frontTex;
      leftPageMesh.material[3].needsUpdate = true;
    }
  });

  textureLoader.load(backCoverUrl, (backTex) => {
    backTex.anisotropy = 8;
    backTex.center.set(0.5, 0.5);
    backTex.rotation = 0;
    currentBackCoverTexture = backTex;

    if (pageMesh && Array.isArray(pageMesh.material)) {
      pageMesh.material[3].map = backTex;
      pageMesh.material[3].needsUpdate = true;
    }
  });

  // Update Rings according to selected Book SKU
  const pageH = 2.4 / bookAspectRatio;
  build3DRingsForSku(bookSku, pageH);
}

function update3DBookDimensions(aspectRatio) {
  bookAspectRatio = aspectRatio || 1.0;
  if (is3dInitialized) {
    build3DScrapbookModel();
  }
}

// ================= CAMERA & VIEW ANGLES =================
function toggle3DAutoRotate() {
  isAutoRotate = !isAutoRotate;
  if (controls) controls.autoRotate = isAutoRotate;
  const btn = document.getElementById('btn-toggle-rotate');
  if (btn) {
    btn.innerText = isAutoRotate ? 'Dừng xoay' : 'Tự động xoay 360°';
  }
}

function set3DViewAngle(angleType) {
  if (!camera || !controls) return;
  controls.autoRotate = false;

  if (angleType === 'front') {
    camera.position.set(0.6, 4.2, 3.2);
    controls.target.set(0.6, 0, 0);
  } else if (angleType === 'cover') {
    if (!isBookClosed) {
      camera.position.set(-1.25, 4.5, 2.5);
      controls.target.set(-1.25, 0, 0);
    } else {
      camera.position.set(1.25, 4.0, 1.8);
      controls.target.set(1.25, 0.08, 0);
    }
  } else if (angleType === 'back') {
    camera.position.set(1.25, -4.0, -1.8);
    controls.target.set(1.25, 0, 0);
  } else if (angleType === 'iso') {
    camera.position.set(3.4, 3.6, 4.5);
    controls.target.set(0.6, 0, 0);
  } else if (angleType === 'top') {
    camera.position.set(0.6, 6.2, 0.01);
    controls.target.set(0.6, 0, 0);
  }
  controls.update();
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
