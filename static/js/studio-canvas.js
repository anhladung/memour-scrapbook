var pageSnapshots = window.pageSnapshots || new Map(); window.pageSnapshots = pageSnapshots;
/**
 * ScrapCraft Studio 2.0 - Advanced 2D Canvas Engine (Powered by Fabric.js)
 * Multi-Page, Rich Text, Design Shortcuts, Custom Size, Templates, Photo Upload & Real-time 3D Sync
 */

let canvas = null;
let currentBookSku = 'SCR-001';
let currentUsedSkus = new Map(); // SKU -> { sku, name, price, image, count }

// Multi-Page Management
let studioPages = [
  { id: 1, name: 'Trang 1', json: null, bg: '#e8d8c3', bgPattern: null }
];
let activePageIndex = 0;

// Canvas Size Configuration
const CANVAS_SIZES = {
  a5_portrait: { width: 500, height: 708, label: 'A5 Đứng (15x21 cm) - Chuẩn Xưởng', ratio: 0.7062 },
  square: { width: 600, height: 600, label: 'Vuông (20x20 cm)', ratio: 1.0 },
  a4_landscape: { width: 708, height: 500, label: 'A4 Ngang (21x15 cm)', ratio: 1.416 },
  mini_pocket: { width: 450, height: 600, label: 'Mini (10x15 cm)', ratio: 0.75 }
};
let currentSizeKey = 'a5_portrait';
let isSafeZoneEnabled = true; // Khung an toàn 1cm mặc định BẬT

// Undo / Redo History Stack
let canvasHistory = [];
let historyIndex = -1;
let isHistoryLocked = false;

// Clipboard for Copy / Paste
let clipboardObject = null;

// ================= INITIALIZATION =================
function initStudioCanvas() {
  const canvasElem = document.getElementById('scrapbook-fabric-canvas');
  if (!canvasElem) return;

  const initialSize = CANVAS_SIZES[currentSizeKey];

  canvas = new fabric.Canvas('scrapbook-fabric-canvas', {
    width: initialSize.width,
    height: initialSize.height,
    backgroundColor: '#e8d8c3',
    selectionColor: 'rgba(136, 19, 55, 0.15)',
    selectionBorderColor: '#881337',
    selectionLineWidth: 2,
    preserveObjectStacking: true
  });

  // Custom Selection Controls (Artistic Craft Aesthetic)
  fabric.Object.prototype.set({
    transparentCorners: false,
    cornerColor: '#881337',
    cornerStrokeColor: '#ffffff',
    borderColor: '#881337',
    cornerSize: 10,
    cornerStyle: 'circle',
    padding: 6
  });

  // Event Listeners for State & History
    canvas.on('object:modified', () => {
    scheduleSnapshotUpdate();
    saveCanvasState();
    updateCanvasStats();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  });

  canvas.on('object:added', () => {
    scheduleSnapshotUpdate();
    saveCanvasState();
    updateCanvasStats();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  });

  canvas.on('object:removed', () => {
    scheduleSnapshotUpdate();
    saveCanvasState();
    updateCanvasStats();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  });

  // Keyboard Shortcuts Binding
  bindStudioKeyboardShortcuts();

  // Load Preset or Initial Starter
  if (window.STUDIO_PRESET_DATA) {
    loadCanvasPreset(window.STUDIO_PRESET_DATA);
  } else {
    addDefaultStarterElements();
  }

  // Active Product direct add
  if (window.STUDIO_ACTIVE_PRODUCT) {
    setTimeout(() => {
      const prod = window.STUDIO_ACTIVE_PRODUCT;
      if (prod.category === 'layout') {
        addLayoutToCanvas(prod.sku, prod.name, prod.image, prod.price);
      } else if (prod.category === 'sticker') {
        addStickerToCanvas(prod.sku, prod.name, prod.image, prod.price);
      } else if (prod.category === 'scrapbook') {
        setScrapbookCover(prod.sku, prod.name, prod.image, prod.price, prod.specs ? prod.specs.color : '#d97706');
      }
    }, 300);
  }

  renderPageTabs();
  saveCanvasState();
  
  // Auto-restore draft on page load
  const hasRestored = loadStudioDraftFromStorage();
  if (!hasRestored) {
    // Initial safe zone & default 3D sync
    renderSafeZoneGuide();
    if (typeof syncTo3DViewer === 'function') setTimeout(syncTo3DViewer, 100);
  }
  setTimeout(() => { if (typeof applyBackgroundPattern === 'function') applyBackgroundPattern('PAT-001', 'Nền Giấy Mỹ Thuật Sợi Tự Nhiên', '/static/assets/patterns/pat_001.webp', 3000); }, 200);
}

// ================= KEYBOARD & MOUSE SHORTCUTS =================
function bindStudioKeyboardShortcuts() {
  window.addEventListener('keydown', (e) => {
    // Ignore shortcuts when user is typing in input or textarea
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.isContentEditable) {
      return;
    }

    const isCtrl = e.ctrlKey || e.metaKey;
    const key = e.key.toLowerCase();

    // 1. Delete / Backspace
    if (e.key === 'Delete' || e.key === 'Backspace') {
      const activeObj = canvas.getActiveObject();
      if (activeObj && !activeObj.isEditing) {
        e.preventDefault();
        deleteSelectedObject();
      }
    }

    // 2. Copy (Ctrl+C)
    else if (isCtrl && key === 'c') {
      e.preventDefault();
      copyActiveObject();
    }

    // 3. Paste (Ctrl+V)
    else if (isCtrl && key === 'v') {
      e.preventDefault();
      pasteObject();
    }

    // 4. Duplicate (Ctrl+D)
    else if (isCtrl && key === 'd') {
      e.preventDefault();
      duplicateActiveObject();
    }

    // 5. Undo (Ctrl+Z)
    else if (isCtrl && key === 'z' && !e.shiftKey) {
      e.preventDefault();
      undoCanvas();
    }

    // 6. Redo (Ctrl+Y or Ctrl+Shift+Z)
    else if ((isCtrl && key === 'y') || (isCtrl && e.shiftKey && key === 'z')) {
      e.preventDefault();
      redoCanvas();
    }

    // 7. Layering: Send Backward ([) / Bring Forward (])
    else if (key === '[') {
      e.preventDefault();
      if (e.shiftKey) sendToBack(); else sendBackward();
    }
    else if (key === ']') {
      e.preventDefault();
      if (e.shiftKey) bringToFront(); else bringForward();
    }

    // 8. Nudge (Arrow Keys)
    else if (['arrowup', 'arrowdown', 'arrowleft', 'arrowright'].includes(key)) {
      const activeObj = canvas.getActiveObject();
      if (activeObj && !activeObj.isEditing) {
        e.preventDefault();
        const step = e.shiftKey ? 10 : 2;
        if (key === 'arrowup') activeObj.top -= step;
        if (key === 'arrowdown') activeObj.top += step;
        if (key === 'arrowleft') activeObj.left -= step;
        if (key === 'arrowright') activeObj.left += step;
        activeObj.setCoords();
        canvas.renderAll();
        if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
      }
    }
  });
}

// ================= COPY / PASTE / DUPLICATE =================
function copyActiveObject() {
  if (!canvas) return;
  const activeObj = canvas.getActiveObject();
  if (!activeObj) return;

  activeObj.clone((cloned) => {
    clipboardObject = cloned;
    showToast('Đã sao chép phần tử', 'info');
  });
}

function pasteObject() {
  if (!canvas || !clipboardObject) return;

  clipboardObject.clone((clonedObj) => {
    canvas.discardActiveObject();
    clonedObj.set({
      left: clonedObj.left + 25,
      top: clonedObj.top + 25,
      evented: true
    });

    if (clonedObj.type === 'activeSelection') {
      clonedObj.canvas = canvas;
      clonedObj.forEachObject((obj) => canvas.add(obj));
      clonedObj.setCoords();
    } else {
      canvas.add(clonedObj);
    }

    clipboardObject.top += 25;
    clipboardObject.left += 25;
    canvas.setActiveObject(clonedObj);
    canvas.renderAll();
    showToast('Đã dán phần tử lên trang', 'success');
  });
}

function duplicateActiveObject() {
  if (!canvas) return;
  const activeObj = canvas.getActiveObject();
  if (!activeObj) {
    showToast('Vui lòng chọn phần tử cần nhân bản', 'info');
    return;
  }

  activeObj.clone((cloned) => {
    cloned.set({
      left: activeObj.left + 30,
      top: activeObj.top + 30,
      evented: true
    });
    canvas.add(cloned);
    canvas.setActiveObject(cloned);
    canvas.renderAll();
    showToast('Đã nhân bản phần tử (Ctrl+D)', 'success');
  });
}

// ================= UNDO / REDO HISTORY =================
function saveCanvasState() {
  if (isHistoryLocked || !canvas) return;
  saveStudioDraftToStorage(false);

  const json = JSON.stringify(canvas.toJSON(['sku', 'itemName', 'itemPrice', 'itemCategory', 'src']));
  
  if (historyIndex < canvasHistory.length - 1) {
    canvasHistory = canvasHistory.slice(0, historyIndex + 1);
  }

  canvasHistory.push(json);
  if (canvasHistory.length > 30) {
    canvasHistory.shift();
  } else {
    historyIndex++;
  }
}

function undoCanvas() {
  if (!canvas || historyIndex <= 0) {
    showToast('Không còn thao tác trước để hoàn tác', 'info');
    return;
  }

  isHistoryLocked = true;
  historyIndex--;
  const prevState = canvasHistory[historyIndex];

  canvas.loadFromJSON(prevState, () => {
    canvas.renderAll();
    isHistoryLocked = false;
    updateCanvasStats();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
    showToast('Hoàn tác (Undo)', 'info');
  });
}

function redoCanvas() {
  if (!canvas || historyIndex >= canvasHistory.length - 1) {
    showToast('Không còn thao tác sau để làm lại', 'info');
    return;
  }

  isHistoryLocked = true;
  historyIndex++;
  const nextState = canvasHistory[historyIndex];

  canvas.loadFromJSON(nextState, () => {
    canvas.renderAll();
    isHistoryLocked = false;
    updateCanvasStats();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
    showToast('Làm lại (Redo)', 'info');
  });
}

// ================= LAYERING (Z-INDEX) =================
function bringForward() {
  const active = canvas ? canvas.getActiveObject() : null;
  if (active) {
    canvas.bringForward(active);
    canvas.renderAll();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
    showToast('Đã đưa lên 1 lớp', 'info');
  }
}

function sendBackward() {
  const active = canvas ? canvas.getActiveObject() : null;
  if (active) {
    canvas.sendBackwards(active);
    canvas.renderAll();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
    showToast('Đã hạ xuống 1 lớp', 'info');
  }
}

function bringToFront() {
  const active = canvas ? canvas.getActiveObject() : null;
  if (active) {
    canvas.bringToFront(active);
    canvas.renderAll();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
    showToast('Đã đưa lên trên cùng', 'info');
  }
}

function sendToBack() {
  const active = canvas ? canvas.getActiveObject() : null;
  if (active) {
    canvas.sendToBack(active);
    canvas.renderAll();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
    showToast('Đã hạ xuống dưới cùng', 'info');
  }
}

function centerActiveObject() {
  const active = canvas ? canvas.getActiveObject() : null;
  if (active) {
    canvas.centerObject(active);
    active.setCoords();
    canvas.renderAll();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
    showToast('Đã căn giữa trang', 'info');
  }
}

// ================= USER PHOTO UPLOAD (DIRECT PHOTO INSERTION INTO LAYOUT FRAME) =================
function handleUserPhotoUpload(event) {
  const file = event.target.files && event.target.files[0];
  if (!file || !canvas) return;

  const validTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/svg+xml'];
  if (!validTypes.includes(file.type)) {
    showToast('Vui lòng chọn ảnh định dạng JPG, PNG hoặc WEBP', 'info');
    return;
  }

  const reader = new FileReader();
  reader.onload = function(f) {
    const dataUrl = f.target.result;

    fabric.Image.fromURL(dataUrl, (userPhoto) => {
      if (!userPhoto) return;

      const activeObj = canvas.getActiveObject();
      const targetFrame = (activeObj && activeObj.itemCategory === 'layout') ? activeObj : null;

      if (pendingLayoutForPhoto) {
        // User clicked "📷 Chèn Ảnh" from layout card
        const layConfig = pendingLayoutForPhoto;
        pendingLayoutForPhoto = null;

        fabric.Image.fromURL(layConfig.imageUrl, (frameImg) => {
          const targetDim = 280;
          const scale = targetDim / Math.max(frameImg.width || 320, frameImg.height || 300);
          const cCenter = canvas.getCenter();

          // 1. Position photo behind the frame's transparent window
          const pScale = (targetDim * 0.75) / Math.max(userPhoto.width || 300, userPhoto.height || 300);
          userPhoto.set({
            originX: 'center',
            originY: 'center',
            left: cCenter.left,
            top: cCenter.top,
            scaleX: pScale,
            scaleY: pScale,
            itemCategory: 'user_photo',
            itemName: `Ảnh trong khung (${file.name})`
          });

          frameImg.set({
            originX: 'center',
            originY: 'center',
            left: cCenter.left,
            top: cCenter.top,
            scaleX: scale,
            scaleY: scale,
            sku: layConfig.sku,
            itemName: layConfig.name,
            itemPrice: layConfig.price || 1000,
            itemCategory: 'layout',
            shadow: new fabric.Shadow({ color: 'rgba(0,0,0,0.25)', blur: 10, offsetX: 3, offsetY: 5 })
          });

          // Create combined group
          const framedGroup = new fabric.Group([userPhoto, frameImg], {
            originX: 'center',
            originY: 'center',
            left: cCenter.left,
            top: cCenter.top,
            sku: layConfig.sku,
            itemName: `${layConfig.name} (Đã lồng ảnh)`,
            itemPrice: layConfig.price || 1000,
            itemCategory: 'layout'
          });

          canvas.add(framedGroup);
          canvas.setActiveObject(framedGroup);
          canvas.renderAll();
          showToast(`Đã lồng ảnh "${file.name}" vào khung "${layConfig.name}" thành công!`, 'success');
          if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
        }, { crossOrigin: 'anonymous' });

      } else if (targetFrame) {
        // User selected an existing frame on canvas and uploaded a photo
        const fCenter = targetFrame.getCenterPoint();
        const fScale = targetFrame.scaleX || 1;
        const pScale = (targetFrame.width * fScale * 0.75) / Math.max(userPhoto.width || 300, userPhoto.height || 300);

        userPhoto.set({
          originX: 'center',
          originY: 'center',
          left: fCenter.x,
          top: fCenter.y,
          scaleX: pScale,
          scaleY: pScale,
          angle: targetFrame.angle || 0,
          itemCategory: 'user_photo',
          itemName: `Ảnh lồng khung (${file.name})`
        });

        // Group together
        canvas.remove(targetFrame);
        const framedGroup = new fabric.Group([userPhoto, targetFrame], {
          originX: 'center',
          originY: 'center',
          left: fCenter.x,
          top: fCenter.y,
          angle: targetFrame.angle || 0,
          sku: targetFrame.sku,
          itemName: `${targetFrame.itemName} (Đã lồng ảnh)`,
          itemPrice: targetFrame.itemPrice,
          itemCategory: 'layout'
        });

        canvas.add(framedGroup);
        canvas.setActiveObject(framedGroup);
        canvas.renderAll();
        showToast(`Đã lồng ảnh vào khung "${targetFrame.itemName}"!`, 'success');
        if (typeof syncTo3DViewer === 'function') syncTo3DViewer();

      } else {
        // Standard standalone photo with stylish white border
        const maxDim = 220;
        const scale = Math.min(maxDim / (userPhoto.width || 300), maxDim / (userPhoto.height || 300));
        const cCenter = canvas.getCenter();

        userPhoto.set({
          originX: 'center',
          originY: 'center',
          left: cCenter.left + (Math.random() * 30 - 15),
          top: cCenter.top + (Math.random() * 30 - 15),
          scaleX: scale,
          scaleY: scale,
          angle: (Math.random() * 8) - 4,
          stroke: '#ffffff',
          strokeWidth: 6,
          itemCategory: 'user_photo',
          itemName: file.name || 'Ảnh Kỷ Niệm Cá Nhân',
          shadow: new fabric.Shadow({
            color: 'rgba(0, 0, 0, 0.3)',
            blur: 12,
            offsetX: 4,
            offsetY: 6
          })
        });

        canvas.add(userPhoto);
        canvas.setActiveObject(userPhoto);
        canvas.renderAll();
        showToast(`Đã tải ảnh "${file.name}" lên trang sổ!`, 'success');
        if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
      }
    });
  };

  reader.readAsDataURL(file);
  event.target.value = '';
}

// ================= INTERACTIVE PHOTO LAYOUTS WITH DIRECT PHOTO INSERTION =================
let pendingLayoutForPhoto = null;

const LAYOUT_WINDOW_PRESETS = {
  'LAY-001': { xRatio: 0.065, yRatio: 0.055, wRatio: 0.87, hRatio: 0.75 }, // Polaroid Heart
  'LAY-002': { xRatio: 0.106, yRatio: 0.375, wRatio: 0.45, hRatio: 0.49 }, // Canon Digicam
  'LAY-003': { xRatio: 0.065, yRatio: 0.191, wRatio: 0.87, hRatio: 0.595 }, // Instagram Post
  'LAY-004': { xRatio: 0.152, yRatio: 0.130, wRatio: 0.82, hRatio: 0.50 },  // Cozy Knit Frame
  'LAY-VN-001': { xRatio: 0.12, yRatio: 0.22, wRatio: 0.76, hRatio: 0.52 }, // Hoa Sen & Cờ Đỏ
  'LAY-VN-002': { xRatio: 0.08, yRatio: 0.08, wRatio: 0.84, hRatio: 0.84 }, // Kỷ Hà Hoàng Gia
  'LAY-VN-003': { xRatio: 0.10, yRatio: 0.16, wRatio: 0.80, hRatio: 0.65 }, // Trống Đồng Đông Sơn
  'LAY-VN-004': { xRatio: 0.10, yRatio: 0.15, wRatio: 0.80, hRatio: 0.68 }  // Cờ Tổ Quốc & Rồng Thiêng
};

function addLayoutFrameToCanvas(sku, name, imageUrl, price) {
  if (!canvas) return;

  fabric.Image.fromURL(imageUrl, (frameImg) => {
    if (!frameImg) return;

    const targetDim = 280;
    const origW = frameImg.width || 320;
    const origH = frameImg.height || 300;
    const scale = targetDim / Math.max(origW, origH);
    const cCenter = canvas.getCenter();

    frameImg.set({
      originX: 'center',
      originY: 'center',
      left: cCenter.left + (Math.random() * 30 - 15),
      top: cCenter.top + (Math.random() * 30 - 15),
      scaleX: scale,
      scaleY: scale,
      angle: (Math.random() * 6) - 3,
      sku: sku,
      itemName: name,
      itemPrice: price || 1000,
      itemCategory: 'layout',
      isPhotoFrame: true,
      shadow: new fabric.Shadow({
        color: 'rgba(0, 0, 0, 0.25)',
        blur: 10,
        offsetX: 3,
        offsetY: 5
      })
    });

    canvas.add(frameImg);
    canvas.setActiveObject(frameImg);
    canvas.renderAll();
    showToast(`Đã thêm khung "${name}"! (Nhấp đúp vào khung để lồng ảnh của bạn)`, 'success');
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  }, { crossOrigin: 'anonymous' });
}

function promptPhotoForLayout(sku, name, imageUrl, price) {
  pendingLayoutForPhoto = { sku, name, imageUrl, price };
  const uploadInput = document.getElementById('user-photo-upload');
  if (uploadInput) {
    uploadInput.click();
  }
}

// Double click to insert photo into active layout frame
if (typeof canvas !== 'undefined' && canvas) {
  canvas.on('mouse:dblclick', (opt) => {
    const target = opt.target;
    if (target && target.itemCategory === 'layout') {
      const uploadInput = document.getElementById('user-photo-upload');
      if (uploadInput) {
        showToast(`Chọn ảnh từ máy tính để lồng vào khung "${target.itemName}"...`, 'info');
        uploadInput.click();
      }
    }
  });
}


// ================= RICH TEXT TOOL =================
function openTextModal() {
  const modal = document.getElementById('text-tool-modal');
  if (modal) {
    modal.classList.remove('hidden');
    document.getElementById('text-input-field').focus();
  } else {
    // Direct add text if modal is not present
    addCustomTextToCanvas();
  }
}

function closeTextModal() {
  const modal = document.getElementById('text-tool-modal');
  if (modal) modal.classList.add('hidden');
}

function addCustomTextToCanvas(customText = null, customFont = null, customColor = null, customSize = null) {
  if (!canvas) return;

  const textInput = document.getElementById('text-input-field');
  const fontSelect = document.getElementById('text-font-select');
  const sizeInput = document.getElementById('text-size-input');
  const colorInput = document.getElementById('text-color-input');

  const textContent = customText || (textInput ? textInput.value.trim() : '') || 'Kỷ Niệm ✦ 2026';
  const fontFamily = customFont || (fontSelect ? fontSelect.value : 'Patrick Hand');
  const fontSize = customSize || (sizeInput ? parseInt(sizeInput.value, 10) : 32);
  const fill = customColor || (colorInput ? colorInput.value : '#78350f');

  const cCenter = canvas.getCenter();

  const textObj = new fabric.IText(textContent, {
    originX: 'center',
    originY: 'center',
    left: cCenter.left + (Math.random() * 40 - 20),
    top: cCenter.top + (Math.random() * 40 - 20),
    fontFamily: fontFamily,
    fontSize: fontSize,
    fill: fill,
    angle: (Math.random() * 6) - 3,
    itemCategory: 'text',
    itemName: `Chữ: "${textContent.substring(0, 15)}..."`,
    shadow: new fabric.Shadow({
      color: 'rgba(0,0,0,0.18)',
      blur: 4,
      offsetX: 2,
      offsetY: 2
    })
  });

  canvas.add(textObj);
  canvas.setActiveObject(textObj);
  canvas.renderAll();
  closeTextModal();
  showToast('Đã thêm chữ (Nhấp đúp để sửa chữ trực tiếp)', 'success');
  if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
}

function addTextToCanvas() {
  addCustomTextToCanvas();
}

// Quick Font / Color change for active text object
function updateActiveTextStyle(property, value) {
  if (!canvas) return;
  const activeObj = canvas.getActiveObject();
  if (activeObj && (activeObj.type === 'i-text' || activeObj.type === 'text')) {
    activeObj.set(property, value);
    canvas.renderAll();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  }
}

// ================= MULTI-PAGE SYSTEM =================
function saveCurrentPageData() {
  if (!canvas) return;
  const page = studioPages[activePageIndex];
  if (page) {
    page.json = canvas.toJSON(['sku', 'itemName', 'itemPrice', 'itemCategory', 'src']);
    page.bg = canvas.backgroundColor;
    try {
      if (pageSnapshots) {
        const liveSnapshot = canvas.toDataURL({ format: 'png', quality: 1.0, multiplier: 2.0 });
        pageSnapshots.set(activePageIndex, liveSnapshot);
      }
    } catch(e) {}
  }
}

function renderPageTabs() {
  const container = document.getElementById('studio-page-tabs');
  if (!container) return;

  container.innerHTML = '';

  studioPages.forEach((page, idx) => {
    const tabBtn = document.createElement('button');
    const isActive = (idx === activePageIndex);
    
    tabBtn.className = isActive
      ? 'px-3.5 py-1.5 rounded-xl text-xs font-black bg-rose-800 text-white border-2 border-black shadow-neo flex items-center gap-1.5 transition-all'
      : 'px-3.5 py-1.5 rounded-xl text-xs font-bold bg-white hover:bg-amber-100 text-stone-900 border border-stone-300 transition-all flex items-center gap-1.5';

    tabBtn.innerHTML = `
      <span>${page.name}</span>
      ${studioPages.length > 1 ? `<span onclick="event.stopPropagation(); deletePage(${idx})" class="text-stone-300 hover:text-white ml-1 text-xs font-bold" title="Xóa trang">×</span>` : ''}
    `;
    tabBtn.onclick = () => switchPage(idx);
    container.appendChild(tabBtn);
  });

  if (typeof update3DSpreadLabels === 'function') {
    update3DSpreadLabels();
  }
}

function addNewPage() {
  saveCurrentPageData();
  const newIndex = studioPages.length;
  const newPageNumber = newIndex + 1;

  studioPages.push({
    id: Date.now(),
    name: `Trang ${newPageNumber}`,
    json: null,
    bg: '#e8d8c3',
    bgPattern: null
  });

  switchPage(newIndex);
  showToast(`Đã tạo Trang ${newPageNumber} mới!`, 'success');
}

function switchPage(targetIndex, skip3DSync = false) {
  if (!canvas || targetIndex === activePageIndex || targetIndex < 0 || targetIndex >= studioPages.length) return;

  saveCurrentPageData();
  activePageIndex = targetIndex;
  renderPageTabs();

  const targetPage = studioPages[activePageIndex];
  if (targetPage.json) {
    canvas.loadFromJSON(targetPage.json, () => {
      canvas.renderAll();
      updateCanvasStats();
      renderSafeZoneGuide();
      if (!skip3DSync && typeof syncTo3DViewer === 'function') {
        syncTo3DViewer();
      }
      if (typeof update3DSpreadLabels === 'function') update3DSpreadLabels();
      showToast(`Đang mở ${targetPage.name}`, 'info');
    });
  } else {
    canvas.clear();
    canvas.setBackgroundColor(targetPage.bg || '#e8d8c3', () => {
      canvas.renderAll();
      updateCanvasStats();
      renderSafeZoneGuide();
      if (!skip3DSync && typeof syncTo3DViewer === 'function') {
        syncTo3DViewer();
      }
      if (typeof update3DSpreadLabels === 'function') update3DSpreadLabels();
      showToast(`Đang mở ${targetPage.name}`, 'info');
    });
  }
}






function duplicatePage(index) {
  saveCurrentPageData();
  const sourcePage = studioPages[index || activePageIndex];
  const newIndex = studioPages.length;

  studioPages.push({
    id: Date.now(),
    name: `${sourcePage.name} (Bản sao)`,
    json: JSON.parse(JSON.stringify(sourcePage.json || canvas.toJSON(['sku', 'itemName', 'itemPrice', 'itemCategory', 'src']))),
    bg: sourcePage.bg,
    bgPattern: sourcePage.bgPattern
  });

  switchPage(newIndex);
  showToast(`Đã nhân bản ${sourcePage.name}!`, 'success');
}

function deletePage(index) {
  if (studioPages.length <= 1) {
    showToast('Phải giữ lại ít nhất 1 trang trong cuốn sổ', 'info');
    return;
  }

  if (confirm(`Bạn có chắc muốn xóa ${studioPages[index].name}?`)) {
    studioPages.splice(index, 1);
    if (activePageIndex >= studioPages.length) {
      activePageIndex = studioPages.length - 1;
    }
    renderPageTabs();
    const targetPage = studioPages[activePageIndex];
    if (targetPage.json) {
      canvas.loadFromJSON(targetPage.json, () => {
        canvas.renderAll();
        updateCanvasStats();
        if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
      });
    } else {
      canvas.clear();
      const patUrl = targetPage.bgPattern || '/static/assets/patterns/pat_001.webp';
      applyBackgroundPattern('PAT-001', 'Nền Giấy Mỹ Thuật', patUrl, 500);
    }
    showToast('Đã xóa trang', 'info');
  }
}

// ================= CANVAS SIZE & DIMENSIONS =================
function changeCanvasSize(sizeKey) {
  if (!canvas || !CANVAS_SIZES[sizeKey]) return;

  const oldWidth = canvas.getWidth() || 600;
  const oldHeight = canvas.getHeight() || 600;

  currentSizeKey = sizeKey;
  const cfg = CANVAS_SIZES[sizeKey];
  const newWidth = cfg.width;
  const newHeight = cfg.height;

  const scaleRatioX = newWidth / oldWidth;
  const scaleRatioY = newHeight / oldHeight;
  const uniformScale = Math.min(scaleRatioX, scaleRatioY);

  // Proportional transformation of ALL elements so nothing is clipped
  const objects = canvas.getObjects();
  objects.forEach(obj => {
    obj.set({
      left: obj.left * scaleRatioX,
      top: obj.top * scaleRatioY,
      scaleX: (obj.scaleX || 1) * uniformScale,
      scaleY: (obj.scaleY || 1) * uniformScale
    });
    obj.setCoords();
  });

  canvas.setWidth(newWidth);
  canvas.setHeight(newHeight);
  canvas.calcOffset();
  canvas.renderAll();

  // Highlight active size button
  document.querySelectorAll('.btn-canvas-size').forEach(btn => {
    if (btn.getAttribute('data-size') === sizeKey) {
      btn.className = 'btn-canvas-size text-xs px-3 py-1.5 rounded-xl font-heading font-black bg-rose-800 text-white border-2 border-black shadow-sm transition-all';
    } else {
      btn.className = 'btn-canvas-size text-xs px-3 py-1.5 rounded-xl font-bold bg-stone-100 hover:bg-amber-100 text-stone-800 border border-stone-300 transition-all';
    }
  });

  if (typeof update3DBookDimensions === 'function') {
    update3DBookDimensions(cfg.ratio);
  }

  if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  showToast(`Đã chuyển kích cỡ sổ: ${cfg.label}! (Các chi tiết tự động căn chỉnh tỷ lệ)`, 'success');
}

// ================= TEMPLATE PRESETS LIBRARY (6 TEMPLATES) =================
const TEMPLATE_PRESETS = {};
const OLD_TEMPLATE_PRESETS = {
  dalat_vintage: {
    name: 'Chuyến Đi Đà Lạt Hoài Niệm',
    bg: '#e8d8c3',
    items: [
      { sku: 'LAY-001', type: 'layout', image: '/static/assets/layouts/lay_001.svg', name: 'Khung Polaroid Vintage Film', left: 240, top: 220, scale: 0.85, angle: -4 },
      { sku: 'STK-CMP-025', type: 'sticker', image: '/static/assets/stickers/stk_cmp_025.webp', name: 'Máy Ảnh Polaroid Vintage', left: 120, top: 110, scale: 0.7, angle: -12 },
      { sku: 'STK-TRV-014', type: 'sticker', image: '/static/assets/stickers/stk_trv_014.webp', name: 'Tem Bưu Chính Xe Vespa', left: 460, top: 130, scale: 0.75, angle: 15 },
      { sku: 'STK-VN-008', type: 'sticker', image: '/static/assets/stickers/stk_vn_008.webp', name: 'Ly Cà Phê Phin Nhỏ Giọt', left: 240, top: 75, scale: 0.8, angle: 2 },
      { type: 'text', text: 'Đà Lạt ✦ Mùa Hoa Dã Quỳ', fontFamily: 'Patrick Hand', fontSize: 34, fill: '#78350f', left: 300, top: 480, angle: -2 }
    ]
  },
  y2k_besties: {
    name: 'Kỷ Yếu Phượt Bạn Thân',
    bg: '#fdf2f8',
    pattern: '/static/assets/patterns/pat_gingham_pink.svg',
    items: [
      { sku: 'LAY-002', type: 'layout', image: '/static/assets/layouts/lay_002.svg', name: 'Layout Khung Kép Bạn Thân', left: 300, top: 240, scale: 0.88, angle: 3 },
      { sku: 'STK-TRV-001', type: 'sticker', image: '/static/assets/stickers/stk_trv_001.webp', name: 'Cung Đường Phượt Road Trip', left: 130, top: 120, scale: 0.75, angle: -18 },
      { sku: 'STK-CMP-023', type: 'sticker', image: '/static/assets/stickers/stk_cmp_023.webp', name: 'Xe Van VW Camper Xanh Mint', left: 470, top: 380, scale: 0.8, angle: 12 },
      { sku: 'STK-TRV-007', type: 'sticker', image: '/static/assets/stickers/stk_trv_007.webp', name: 'Vé Máy Bay Boarding Pass', left: 460, top: 110, scale: 0.7, angle: 20 },
      { type: 'text', text: 'Best Friends Forever ✦', fontFamily: 'Patrick Hand', fontSize: 36, fill: '#db2777', left: 300, top: 490, angle: 0 }
    ]
  },
  sweet_love: {
    name: 'Kỷ Niệm Du Lịch Cùng Người Yêu',
    bg: '#fbf8f2',
    pattern: '/static/assets/patterns/pat_dotgrid.svg',
    items: [
      { sku: 'LAY-003', type: 'layout', image: '/static/assets/layouts/lay_003.svg', name: 'Khung Polaroid Viền Đỏ Rượu', left: 260, top: 230, scale: 0.82, angle: -5 },
      { sku: 'STK-TRV-004', type: 'sticker', image: '/static/assets/stickers/stk_trv_004.webp', name: 'Máy Bay Du Lịch Quốc Tế', left: 450, top: 160, scale: 0.75, angle: 14 },
      { sku: 'STK-TRV-028', type: 'sticker', image: '/static/assets/stickers/stk_trv_028.png', name: 'Chữ Viết Tay Memories', left: 110, top: 380, scale: 0.7, angle: -10 },
      { type: 'text', text: 'Every moment with you ✦', fontFamily: 'Playfair Display', fontSize: 30, fill: '#881337', left: 300, top: 480, angle: 0 }
    ]
  },
  botanical_nature: {
    name: 'Hành Trình Di Sản Việt Nam',
    bg: '#f5f0e6',
    pattern: '/static/assets/patterns/pat_botanical.svg',
    items: [
      { sku: 'LAY-004', type: 'layout', image: '/static/assets/layouts/lay_004.svg', name: 'Bố Cục 4 Ô Kỷ Yếu', left: 300, top: 250, scale: 0.8, angle: 0 },
      { sku: 'STK-VN-001', type: 'sticker', image: '/static/assets/stickers/stk_vn_001.webp', name: 'Nón Lá Việt Nam Quai Đỏ', left: 110, top: 100, scale: 0.75, angle: -15 },
      { sku: 'STK-VN-017', type: 'sticker', image: '/static/assets/stickers/stk_vn_017.webp', name: 'Chữ Nghệ Thuật VIỆT NAM 3D', left: 470, top: 420, scale: 0.7, angle: 10 },
      { type: 'text', text: 'Tự Hào Non Sông Gấm Vóc', fontFamily: 'Patrick Hand', fontSize: 32, fill: '#065f46', left: 300, top: 490, angle: 0 }
    ]
  },
  cyberpunk_dark: {
    name: 'Phiêu Lưu Khám Phá Rừng Đêm',
    bg: '#18181b',
    pattern: '/static/assets/patterns/pat_black_card.svg',
    items: [
      { sku: 'LAY-005', type: 'layout', image: '/static/assets/layouts/lay_005.svg', name: 'Layout Khung Đen Gunmetal', left: 280, top: 230, scale: 0.84, angle: 4 },
      { sku: 'STK-CMP-002', type: 'sticker', image: '/static/assets/stickers/stk_cmp_002.webp', name: 'Huy Hiệu Cắm Trại Ngàn Sao', left: 120, top: 120, scale: 0.8, angle: -15 },
      { sku: 'STK-CMP-030', type: 'sticker', image: '/static/assets/stickers/stk_cmp_030.webp', name: 'La Bàn Bỏ Túi Đồng Cổ', left: 300, top: 75, scale: 0.82, angle: -2 },
      { type: 'text', text: 'EXPLORE UNDER STARS ✦', fontFamily: 'Plus Jakarta Sans', fontSize: 32, fill: '#fbbf24', left: 300, top: 480, angle: 0 }
    ]
  },
  birthday_party: {
    name: 'Cắm Trại & Outdoor Camping',
    bg: '#fcfaf6',
    pattern: '/static/assets/patterns/pat_grid.svg',
    items: [
      { sku: 'LAY-006', type: 'layout', image: '/static/assets/layouts/lay_006.svg', name: 'Khung Ảnh Sinh Nhật Rực Rỡ', left: 270, top: 230, scale: 0.82, angle: -3 },
      { sku: 'STK-CMP-001', type: 'sticker', image: '/static/assets/stickers/stk_cmp_001.webp', name: 'Biển Gỗ Adventure Awaits', left: 460, top: 140, scale: 0.8, angle: 12 },
      { sku: 'STK-CMP-008', type: 'sticker', image: '/static/assets/stickers/stk_cmp_008.webp', name: 'Chữ Collect Moments', left: 300, top: 70, scale: 0.85, angle: 0 },
      { type: 'text', text: 'Collect moments, not things! 🌲', fontFamily: 'Patrick Hand', fontSize: 34, fill: '#b45309', left: 300, top: 480, angle: 0 }
    ]
  }
};

function applyTemplatePreset(presetKey) {
  const preset = TEMPLATE_PRESETS[presetKey];
  if (!preset || !canvas) return;

  if (confirm(`Bạn có muốn nạp mẫu sẵn "${preset.name}"? (Các phần tử cũ trên trang hiện tại sẽ được thay thế)`)) {
    canvas.clear();

    if (preset.pattern) {
      applyPaperPatternToCanvas(preset.pattern, preset.name);
    } else {
      changeCanvasBackground(preset.bg || '#e8d8c3');
    }

    preset.items.forEach((item, idx) => {
      if (item.type === 'layout') {
        setTimeout(() => {
          fabric.Image.fromURL(item.image, (img) => {
            if (!img) return;
            img.set({
              originX: 'center',
              originY: 'center',
              left: item.left,
              top: item.top,
              scaleX: item.scale,
              scaleY: item.scale,
              angle: item.angle,
              sku: item.sku,
              itemName: item.name,
              itemCategory: 'layout',
              shadow: new fabric.Shadow({ color: 'rgba(0,0,0,0.25)', blur: 8, offsetX: 3, offsetY: 4 })
            });
            canvas.add(img);
            canvas.sendToBack(img);
            canvas.renderAll();
            if (idx === preset.items.length - 1 && typeof syncTo3DViewer === 'function') syncTo3DViewer();
          }, { crossOrigin: 'anonymous' });
        }, idx * 60);
      } else if (item.type === 'sticker') {
        setTimeout(() => {
          fabric.Image.fromURL(item.image, (img) => {
            if (!img) return;
            img.set({
              originX: 'center',
              originY: 'center',
              left: item.left,
              top: item.top,
              scaleX: item.scale,
              scaleY: item.scale,
              angle: item.angle,
              sku: item.sku,
              itemName: item.name,
              itemCategory: 'sticker',
              shadow: new fabric.Shadow({ color: 'rgba(0,0,0,0.35)', blur: 10, offsetX: 4, offsetY: 6 })
            });
            canvas.add(img);
            canvas.renderAll();
            if (idx === preset.items.length - 1 && typeof syncTo3DViewer === 'function') syncTo3DViewer();
          }, { crossOrigin: 'anonymous' });
        }, idx * 60);
      } else if (item.type === 'text') {
        setTimeout(() => {
          const textObj = new fabric.IText(item.text, {
            originX: 'center',
            originY: 'center',
            left: item.left,
            top: item.top,
            fontFamily: item.fontFamily || 'Patrick Hand',
            fontSize: item.fontSize || 32,
            fill: item.fill || '#78350f',
            angle: item.angle || 0,
            itemCategory: 'text',
            itemName: `Chữ: "${item.text}"`,
            shadow: new fabric.Shadow({ color: 'rgba(0,0,0,0.15)', blur: 4, offsetX: 2, offsetY: 2 })
          });
          canvas.add(textObj);
          canvas.renderAll();
          if (idx === preset.items.length - 1 && typeof syncTo3DViewer === 'function') syncTo3DViewer();
        }, idx * 60);
      }
    });

    showToast(`Đã áp dụng mẫu "${preset.name}" thành công!`, 'success');
  }
}

// ================= STICKERS, LAYOUTS & BOOKS HANDLERS =================
function addStickerToCanvas(sku, arg2, arg3, price) {
  if (!canvas) return;

  let name = arg2;
  let imageUrl = arg3;
  if (typeof arg2 === 'string' && (arg2.startsWith('/') || arg2.startsWith('http') || arg2.includes('.svg'))) {
    imageUrl = arg2;
    name = arg3 || sku;
  }

  fabric.Image.fromURL(imageUrl, (img) => {
    if (!img) return;
    const targetDim = 130;
    const origW = img.width || 300;
    const origH = img.height || 300;
    const scale = targetDim / Math.max(origW, origH);
    const cCenter = canvas.getCenter();

    img.set({
      originX: 'center',
      originY: 'center',
      left: cCenter.left + (Math.random() * 80 - 40),
      top: cCenter.top + (Math.random() * 80 - 40),
      scaleX: scale,
      scaleY: scale,
      angle: (Math.random() * 24) - 12,
      sku: sku,
      itemName: name,
      itemPrice: price || 1000,
      itemCategory: 'sticker',
      shadow: new fabric.Shadow({
        color: 'rgba(0, 0, 0, 0.35)',
        blur: 10,
        offsetX: 4,
        offsetY: 6
      })
    });

    canvas.add(img);
    canvas.setActiveObject(img);
    canvas.renderAll();
    showToast(`Đã dán sticker ${sku} (${name}) lên trang!`, 'success');
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  }, { crossOrigin: 'anonymous' });
}

function addLayoutToCanvas(sku, arg2, arg3, price) {
  if (!canvas) return;

  let name = arg2;
  let imageUrl = arg3;
  if (typeof arg2 === 'string' && (arg2.startsWith('/') || arg2.startsWith('http') || arg2.includes('.svg'))) {
    imageUrl = arg2;
    name = arg3 || sku;
  }

  fabric.Image.fromURL(imageUrl, (img) => {
    if (!img) return;
    const targetDim = 250;
    const origW = img.width || 320;
    const origH = img.height || 300;
    const scale = targetDim / Math.max(origW, origH);
    const cCenter = canvas.getCenter();

    img.set({
      originX: 'center',
      originY: 'center',
      left: cCenter.left + (Math.random() * 40 - 20),
      top: cCenter.top + (Math.random() * 40 - 20),
      scaleX: scale,
      scaleY: scale,
      angle: (Math.random() * 6) - 3,
      sku: sku,
      itemName: name,
      itemPrice: price || 1500,
      itemCategory: 'layout',
      shadow: new fabric.Shadow({
        color: 'rgba(0, 0, 0, 0.22)',
        blur: 8,
        offsetX: 3,
        offsetY: 4
      })
    });

    canvas.add(img);
    canvas.sendToBack(img);
    canvas.setActiveObject(img);
    canvas.renderAll();
    showToast(`Đã đặt khung layout ${sku} (${name}) vào trang!`, 'success');
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  }, { crossOrigin: 'anonymous' });
}

function setScrapbookCover(sku, name, image, price, colorHex) {
  currentBookSku = sku;
  updateCanvasStats();
  if (typeof change3DCoverDesign === 'function') {
    change3DCoverDesign(sku, image, colorHex);
  }
  showToast(`Đã chọn mẫu bìa sổ ${name} (${sku})!`, 'success');
}

function changeCanvasBackground(bgColor) {
  if (!canvas) return;
  canvas.setBackgroundImage(null, () => {
    canvas.setBackgroundColor(bgColor, canvas.renderAll.bind(canvas));
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  });
}

function applyPaperPatternToCanvas(patternUrl, patternName) {
  if (!canvas) return;

  fabric.Image.fromURL(patternUrl, (img) => {
    if (!img) return;
    
    img.set({
      originX: 'left',
      originY: 'top',
      scaleX: canvas.width / (img.width || 400),
      scaleY: canvas.height / (img.height || 400)
    });

    canvas.setBackgroundImage(img, canvas.renderAll.bind(canvas));
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
    showToast(`Đã áp dụng mẫu nền: ${patternName}!`, 'success');
  }, { crossOrigin: 'anonymous' });
}

// ================= TABS SWITCHER (ACCURATE HIGHLIGHTING FOR ALL 5 TABS) =================
function switchCatalogTab(tabName) {
  const tabMapping = [
    { key: 'stickers', catalogId: 'catalog-stickers', btnId: 'tab-stk-btn' },
    { key: 'layouts', catalogId: 'catalog-layouts', btnId: 'tab-lay-btn' },
    { key: 'books', catalogId: 'catalog-books', btnId: 'tab-book-btn' },
    { key: 'patterns', catalogId: 'catalog-patterns', btnId: 'tab-pat-btn' },
    { key: 'templates', catalogId: 'catalog-templates', btnId: 'tab-templates-btn' }
  ];
  
  tabMapping.forEach(tab => {
    const el = document.getElementById(tab.catalogId);
    const btn = document.getElementById(tab.btnId) || document.getElementById(`tab-${tab.key}-btn`);
    
    if (el) {
      if (tab.key === tabName) {
        el.classList.remove('hidden');
      } else {
        el.classList.add('hidden');
      }
    }
    
    if (btn) {
      if (tab.key === tabName) {
        btn.className = 'py-1.5 px-1 rounded-lg text-[11px] font-black bg-white text-stone-950 border-2 border-black shadow-neo transition-all text-center';
      } else {
        btn.className = 'py-1.5 px-1 rounded-lg text-[11px] font-bold text-stone-600 hover:bg-white hover:text-stone-900 transition-all text-center';
      }
    }
  });
}

function addHandwritingNoteCard(type = 'lined') {
  if (!canvas) return;
  let sku = 'LAY-NOTE-LINED';
  let name = 'Khung Giấy Kẻ Dòng Viết Tay';
  let url = '/static/assets/layouts/lay_note_lined.svg';

  if (type === 'grid') {
    sku = 'LAY-NOTE-GRID';
    name = 'Khung Nhật Ký Ô Lưới Grid';
    url = '/static/assets/layouts/lay_note_grid.svg';
  } else if (type === 'kraft') {
    sku = 'LAY-NOTE-KRAFT';
    name = 'Thẻ Ghi Chú Kraft Kỷ Niệm';
    url = '/static/assets/layouts/lay_note_kraft.svg';
  }

  addLayoutToCanvas(sku, name, url, 1000);
}

// ================= DELETE & CLEAR =================
function deleteSelectedObject() {
  const active = canvas ? canvas.getActiveObject() : null;
  if (active) {
    canvas.remove(active);
    canvas.discardActiveObject();
    canvas.renderAll();
    showToast('Đã xóa phần tử (Delete)', 'info');
  } else {
    showToast('Vui lòng chọn phần tử cần xóa trước', 'info');
  }
}
function deleteActiveObject() { deleteSelectedObject(); }

function clearCanvas() {
  if (!canvas) return;
  if (confirm('Bạn có chắc muốn xóa hết toàn bộ trang hiện tại và làm lại từ đầu?')) {
    canvas.clear();
    changeCanvasBackground('#e8d8c3');
    showToast('Đã làm mới trang trắng', 'info');
  }
}
function clearCanvasAll() { clearCanvas(); }

// ================= STARTER TEMPLATES & PRESETS =================
function addDefaultStarterElements() {
  if (!canvas) return;
  canvas.clear();
  canvas.setBackgroundColor('#fdfbf7', () => {
    canvas.renderAll();
    updateCanvasStats();
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  });
}

function loadCanvasPreset(presetData) {
  if (!canvas || !presetData) return;

  canvas.clear();
  if (presetData.bg_color) {
    changeCanvasBackground(presetData.bg_color);
  }

  const items = presetData.items || [];
  if (items.length === 0) return;

  let loadedCount = 0;
  const checkFinished = () => {
    loadedCount++;
    if (loadedCount >= items.length) {
      updateCanvasStats();
      if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
    }
  };

  items.forEach((item) => {
    if (item.type === 'text') {
      const textObj = new fabric.IText(item.text || 'Memories ✦', {
        originX: 'center',
        originY: 'center',
        left: item.left || 300,
        top: item.top || 540,
        fontFamily: item.fontFamily || 'Patrick Hand',
        fontSize: item.fontSize || 34,
        fill: item.fill || '#78350f',
        angle: item.angle || 0,
        itemCategory: 'text',
        itemName: `Chữ: "${item.text}"`,
        shadow: new fabric.Shadow({ color: 'rgba(0,0,0,0.15)', blur: 4, offsetX: 2, offsetY: 2 })
      });
      canvas.add(textObj);
      canvas.renderAll();
      checkFinished();
    } else {
      fabric.Image.fromURL(item.image, (img) => {
        if (!img) {
          checkFinished();
          return;
        }
        img.set({
          originX: 'center',
          originY: 'center',
          left: item.left || 300,
          top: item.top || 300,
          scaleX: item.scale || 0.75,
          scaleY: item.scale || 0.75,
          angle: item.angle || 0,
          sku: item.sku,
          itemName: item.name || item.sku,
          itemPrice: item.price || (item.type === 'layout' ? 1000 : 300),
          itemCategory: item.type || 'sticker',
          shadow: new fabric.Shadow({
            color: item.type === 'layout' ? 'rgba(0,0,0,0.22)' : 'rgba(0,0,0,0.35)',
            blur: item.type === 'layout' ? 8 : 10,
            offsetX: 4,
            offsetY: 6
          })
        });

        canvas.add(img);
        if (item.type === 'layout') canvas.sendToBack(img);
        canvas.renderAll();
        checkFinished();
      }, { crossOrigin: 'anonymous' });
    }
  });
}

// ================= STATS & CART EXPORT =================
function updateCanvasStats() {
  if (!canvas) return;
  const objects = canvas.getObjects();
  currentUsedSkus.clear();

  // Count book base
  currentUsedSkus.set(currentBookSku, {
    sku: currentBookSku,
    name: 'Sổ Scrapbook Bìa Cứng Kraft FSC',
    price: 100000,
    category: 'scrapbook',
    count: 1
  });

  objects.forEach(obj => {
    if (obj.sku) {
      if (currentUsedSkus.has(obj.sku)) {
        const item = currentUsedSkus.get(obj.sku);
        item.count += 1;
      } else {
        currentUsedSkus.set(obj.sku, {
          sku: obj.sku,
          name: obj.itemName || obj.sku,
          price: obj.itemPrice || (obj.itemCategory === 'layout' ? 1000 : 300),
          category: obj.itemCategory || 'sticker',
          count: 1
        });
      }
    }
  });

  // Render SKU list in UI
  const listContainer = document.getElementById('used-components-list');
  const countBadge = document.getElementById('used-skus-count');
  const priceDisplay = document.getElementById('design-total-price');

  if (!listContainer) return;

  listContainer.innerHTML = '';
  let totalPrice = 0;
  let totalItemsCount = 0;

  currentUsedSkus.forEach((item) => {
    totalPrice += item.price * item.count;
    totalItemsCount += item.count;

    const chip = document.createElement('div');
    chip.className = 'inline-flex items-center gap-1.5 bg-stone-100 border border-stone-300 px-2.5 py-1 rounded-lg text-xs font-bold text-stone-800';
    chip.innerHTML = `
      <span class="font-mono font-black text-rose-800">${item.sku}</span>
      <span>${item.name}</span>
      <span class="bg-amber-300 text-black text-[10px] px-1.5 py-0.2 rounded-full font-black">x${item.count}</span>
    `;
    listContainer.appendChild(chip);
  });

  if (countBadge) countBadge.innerText = `${totalItemsCount} linh kiện (${currentUsedSkus.size} mã)`;
  if (priceDisplay) priceDisplay.innerText = new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(totalPrice);
}

function exportCanvasImage() {
  if (!canvas) return;
  const dataURL = canvas.toDataURL({
    format: 'png',
    quality: 1.0,
    multiplier: 2
  });

  const link = document.createElement('a');
  link.download = `ScrapCraft_${activePageIndex + 1}_${Date.now()}.png`;
  link.href = dataURL;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  showToast('Đã xuất ảnh trang sổ độ phân giải cao!', 'success');
}

function addDesignComponentsToCart() {
  try {
    let cart = JSON.parse(localStorage.getItem('scrapcraft_cart') || '[]');
    let addedCount = 0;

    currentUsedSkus.forEach((item) => {
      const existing = cart.find(c => c.sku === item.sku);
      if (existing) {
        existing.quantity += item.count;
      } else {
        cart.push({
          sku: item.sku,
          name: item.name,
          price: item.price,
          category: item.category,
          quantity: item.count,
          image: item.image || `/static/assets/stickers/${item.sku.toLowerCase().replace(/-/g, '_')}.png`
        });
      }
      addedCount += item.count;
    });

    localStorage.setItem('scrapcraft_cart', JSON.stringify(cart));
    if (typeof updateCartCount === 'function') updateCartCount();
    showToast(`Đã thêm ${addedCount} linh kiện thiết kế vào Giỏ Hàng!`, 'success');
  } catch (e) {
    console.error(e);
  }
}

// ================= STICKER THEME FILTER IN STUDIO =================
function filterStudioStickers(category, btnElement) {
  const cards = document.querySelectorAll('.stk-item-card');
  const buttons = document.querySelectorAll('.stk-filter-btn');

  // Update button active styles
  buttons.forEach(btn => {
    btn.className = 'stk-filter-btn px-2.5 py-1 rounded-full font-bold bg-stone-100 hover:bg-stone-200 text-stone-700 whitespace-nowrap transition-all';
  });
  if (btnElement) {
    btnElement.className = 'stk-filter-btn px-2.5 py-1 rounded-full font-black bg-stone-900 text-white whitespace-nowrap transition-all';
  }

  // Filter cards
  cards.forEach(card => {
    const cardType = card.getAttribute('data-stk-type');
    if (category === 'all' || cardType === category) {
      card.classList.remove('hidden');
    } else {
      card.classList.add('hidden');
    }
  });
}

// Robust Auto Initialization (Supports all document readiness states)
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    initStudioCanvas();
  });
} else {
  initStudioCanvas();
}


function addTextLayoutToCanvas(sku, name, imageUrl, price) {
  if (!canvas) return;

  fabric.Image.fromURL(imageUrl, (sheetImg) => {
    if (!sheetImg) return;

    const targetW = 290;
    const origW = sheetImg.width || 300;
    const origH = sheetImg.height || 420;
    const scale = targetW / origW;
    const cCenter = canvas.getCenter();

    sheetImg.set({
      originX: 'center',
      originY: 'center',
      left: cCenter.left + (Math.random() * 20 - 10),
      top: cCenter.top + (Math.random() * 20 - 10),
      scaleX: scale,
      scaleY: scale,
      angle: (Math.random() * 4) - 2,
      sku: sku,
      itemName: name,
      itemPrice: price || 2000,
      itemCategory: 'layout',
      isTextLayout: true,
      shadow: new fabric.Shadow({
        color: 'rgba(0, 0, 0, 0.25)',
        blur: 12,
        offsetX: 3,
        offsetY: 6
      })
    });

    canvas.add(sheetImg);
    canvas.setActiveObject(sheetImg);
    canvas.renderAll();

    showToast(`Đã thêm layout "${name}" vào trang sổ!`, 'success');
    if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
  }, { crossOrigin: 'anonymous' });
}

// ================= PRINT SAFE ZONE (KHUNG AN TOÀN IN ẤN 1CM) =================
let safeZoneGuide = null;

function renderSafeZoneGuide() {
  const container = document.getElementById('safe-zone-overlay');
  if (!container || !canvas) return;

  const w = canvas.getWidth();
  const h = canvas.getHeight();
  
  // 1cm scale: canvas is 500px wide for 15cm -> ~33px per cm
  const marginOuter = 33; // 1cm
  const marginSpine = 45; // 1.35cm spine punch zone

  if (!isSafeZoneEnabled) {
    container.style.display = 'none';
    return;
  }

  container.style.display = 'block';
  container.style.width = w + 'px';
  container.style.height = h + 'px';

  const activePageNum = (typeof activePageIndex !== 'undefined') ? (activePageIndex + 1) : 1;
  const isLeftPage = (activePageNum % 2 === 0); // Trang 2, Trang 4,... là trang bên TRÁI 3D (gáy lò xo ở mép PHẢI)

  const punchCount = 8;
  const punchStep = (h - 80) / (punchCount - 1);
  let punchHolesHtml = '';
  for (let i = 0; i < punchCount; i++) {
    const punchY = 40 + i * punchStep;
    const holePosClass = isLeftPage ? 'right-3' : 'left-3';
    punchHolesHtml += `<div class="absolute ${holePosClass} w-3.5 h-3.5 rounded-full border border-stone-400/80 bg-stone-200/50 shadow-inner flex items-center justify-center pointer-events-none" style="top: ${punchY - 7}px;">
      <span class="w-1 h-1 rounded-full bg-stone-500/60"></span>
    </div>`;
  }

  const spineBorderClass = isLeftPage ? 'border-l' : 'border-r';
  const spinePosStyle = isLeftPage ? `right: 0; width: ${marginSpine}px;` : `left: 0; width: ${marginSpine}px;`;
  const safeBoxStyle = isLeftPage 
    ? `top: ${marginOuter}px; bottom: ${marginOuter}px; left: ${marginOuter}px; right: ${marginSpine}px;`
    : `top: ${marginOuter}px; bottom: ${marginOuter}px; left: ${marginSpine}px; right: ${marginOuter}px;`;

  container.innerHTML = `
    <!-- Spine Punch Margin Guide -->
    <div class="absolute top-0 bottom-0 pointer-events-none ${spineBorderClass} border-dashed border-amber-800/30 bg-amber-500/5 transition-all" style="${spinePosStyle}">
      <div class="absolute top-2 ${isLeftPage ? 'right-1.5' : 'left-1.5'} text-[8px] font-bold text-amber-900/70 tracking-tighter uppercase [writing-mode:vertical-lr] rotate-180">
        Gáy lò xo (${isLeftPage ? 'Mép Phải' : 'Mép Trái'})
      </div>
      ${punchHolesHtml}
    </div>

    <!-- Safe Print Boundary Rectangle (1cm Safe Box) -->
    <div class="absolute pointer-events-none rounded-xl border-2 border-dashed border-rose-600/40 bg-rose-500/[0.02] shadow-sm transition-all"
         style="${safeBoxStyle}">
      <!-- Corner Safe Badges -->
      <span class="absolute -top-3 ${isLeftPage ? 'right-3' : 'left-3'} bg-rose-800 text-white text-[9px] font-black px-1.5 py-0.5 rounded shadow-sm flex items-center gap-1">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
        Khung An Toàn (Trang ${activePageNum} - ${isLeftPage ? 'Bên Trái 3D' : 'Bên Phải 3D'})
      </span>
      <span class="absolute -bottom-2.5 ${isLeftPage ? 'left-3' : 'right-3'} bg-stone-900/80 text-stone-200 text-[8px] font-mono font-bold px-1.5 py-0.5 rounded">
        Giới hạn an toàn lề
      </span>
    </div>
  `;
}

function toggleSafeZone() {
  isSafeZoneEnabled = !isSafeZoneEnabled;
  renderSafeZoneGuide();
  const btn = document.getElementById('btn-toggle-safe-zone');
  if (btn) {
    if (isSafeZoneEnabled) {
      btn.classList.add('bg-rose-100', 'text-rose-900', 'border-rose-300');
      btn.classList.remove('bg-stone-100', 'text-stone-600', 'border-stone-200');
      btn.innerHTML = '📐 Khung An Toàn: <span class="text-rose-800 font-black">BẬT (1cm)</span>';
      showToast('✦ Đã BẬT Khung An Toàn in ấn 1cm!', 'info');
    } else {
      btn.classList.remove('bg-rose-100', 'text-rose-900', 'border-rose-300');
      btn.classList.add('bg-stone-100', 'text-stone-600', 'border-stone-200');
      btn.innerHTML = '📐 Khung An Toàn: <span class="text-stone-500 font-bold">TẮT</span>';
      showToast('✦ Đã TẮT Khung An Toàn.', 'info');
    }
  }
}


// ================= PAPER PATTERN BACKGROUND SYSTEM =================


// ================= PAPER PATTERN BACKGROUND SYNCHRONIZER (2D & 3D) =================
let currentPaperPatternUrl = null;

function applyBackgroundPattern(sku, name, imageUrl, price) {
  if (!canvas) return;

  const patternUrl = imageUrl || '/static/assets/patterns/pat_001.webp';
  currentPaperPatternUrl = patternUrl;

  // 1. Cập nhật trạng thái trang hiện tại
  if (studioPages && studioPages[activePageIndex]) {
    studioPages[activePageIndex].bgPattern = patternUrl;
    studioPages[activePageIndex].bg = null;
  }

  // 2. Nạp nền giấy lên Fabric.js 2D Canvas
  fabric.Image.fromURL(patternUrl, (patternImg) => {
    if (!patternImg) return;

    patternImg.set({
      originX: 'left',
      originY: 'top',
      scaleX: canvas.getWidth() / (patternImg.width || 711),
      scaleY: canvas.getHeight() / (patternImg.height || 1008)
    });

    canvas.setBackgroundColor(null);
    canvas.setBackgroundImage(patternImg, () => {
      canvas.renderAll();
      saveCanvasState();
      updateCanvasStats();

      // 3. Đồng bộ ngay lập tức sang trang ruột 3D (Bên phải)
      if (typeof syncTo3DViewer === 'function') {
        syncTo3DViewer();
      }

      // 4. Đồng bộ màu nền giấy sang trang trong 3D (Bên trái)
      if (typeof change3DInsidePattern === 'function') {
        change3DInsidePattern(patternUrl);
      }

      showToast(`✦ Đã đồng bộ nền giấy "${name}" sang cả 2D và 3D!`, 'success');
    }, { crossOrigin: 'anonymous' });
  }, { crossOrigin: 'anonymous' });
}

function applyPaperPatternToCanvas(patternUrl, patternName) {
  applyBackgroundPattern('PAT-CUSTOM', patternName || 'Nền Giấy Mỹ Thuật', patternUrl, 500);
}


// ================= AUTO-SAVE & DRAFT RECOVERY ENGINE (LOCALSTORAGE) =================
const DRAFT_STORAGE_KEY = 'memour_studio_draft_v2';
let autoSaveDebounceTimer = null;

function saveStudioDraftToStorage(isImmediate = false) {
  if (!canvas) return;

  const performSave = () => {
    saveCurrentPageData();

    const now = new Date();
    const timeStr = now.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit', second: '2-digit' });

    const draftData = {
      version: 2,
      savedAt: now.toISOString(),
      savedTimeFormatted: timeStr,
      activePageIndex: activePageIndex,
      currentBookSku: currentBookSku || 'SCR-001',
      currentSizeKey: currentSizeKey || 'a5_portrait',
      currentPaperPatternUrl: (typeof currentPaperPatternUrl !== 'undefined') ? currentPaperPatternUrl : '/static/assets/patterns/pat_001.webp',
      studioPages: studioPages.map(page => ({
        id: page.id,
        name: page.name,
        json: page.json,
        bg: page.bg,
        bgPattern: page.bgPattern
      }))
    };

    try {
      localStorage.setItem(DRAFT_STORAGE_KEY, JSON.stringify(draftData));
      
      const saveStatusEl = document.getElementById('auto-save-status');
      if (saveStatusEl) {
        saveStatusEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-700 font-black"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>Đã lưu (${timeStr})</span>`;
      }
    } catch (e) {
      console.warn('LocalStorage save error (likely quota):', e);
    }
  };

  if (isImmediate) {
    performSave();
  } else {
    if (autoSaveDebounceTimer) clearTimeout(autoSaveDebounceTimer);
    autoSaveDebounceTimer = setTimeout(performSave, 400);
  }
}

function loadStudioDraftFromStorage() {
  try {
    const raw = localStorage.getItem(DRAFT_STORAGE_KEY);
    if (!raw) return false;

    const draft = JSON.parse(raw);
    if (!draft || !draft.studioPages || !Array.isArray(draft.studioPages) || draft.studioPages.length === 0) {
      return false;
    }

    studioPages = draft.studioPages;
    currentBookSku = draft.currentBookSku || 'SCR-001';
    currentSizeKey = draft.currentSizeKey || 'a5_portrait';
    if (draft.currentPaperPatternUrl) {
      currentPaperPatternUrl = draft.currentPaperPatternUrl;
    }
    activePageIndex = Math.min(Math.max(0, draft.activePageIndex || 0), studioPages.length - 1);

    // Apply canvas size if custom
    if (CANVAS_SIZES[currentSizeKey]) {
      const sizeConfig = CANVAS_SIZES[currentSizeKey];
      canvas.setWidth(sizeConfig.width);
      canvas.setHeight(sizeConfig.height);
      if (typeof update3DBookDimensions === 'function') {
        update3DBookDimensions(sizeConfig.ratio);
      }
    }

    // Render tabs and load active page
    renderPageTabs();
    const activePage = studioPages[activePageIndex];

    if (activePage && activePage.json) {
      canvas.loadFromJSON(activePage.json, () => {
        canvas.renderAll();
        updateCanvasStats();
        renderSafeZoneGuide();
        if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
        if (typeof update3DSpreadLabels === 'function') update3DSpreadLabels();
      });
    } else if (activePage && activePage.bgPattern) {
      canvas.clear();
      applyBackgroundPattern('PAT-001', 'Nền Giấy Mỹ Thuật', activePage.bgPattern, 500);
    } else {
      canvas.clear();
      canvas.setBackgroundColor(activePage.bg || '#e8d8c3', () => {
        canvas.renderAll();
        updateCanvasStats();
        renderSafeZoneGuide();
        if (typeof syncTo3DViewer === 'function') syncTo3DViewer();
      });
    }

    const saveStatusEl = document.getElementById('auto-save-status');
    if (saveStatusEl) {
      saveStatusEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-700 font-bold"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>Đã khôi phục (${draft.savedTimeFormatted || 'gần nhất'})</span>`;
    }

    showToast(`✦ Đã tự động khôi phục bản thiết kế của bạn (Lưu lúc ${draft.savedTimeFormatted || 'gần nhất'})!`, 'success');
    return true;
  } catch (err) {
    console.error('Error recovering draft:', err);
    return false;
  }
}

function clearStudioDraftAndReset() {
  if (confirm('Bạn có chắc chắn muốn làm mới xưởng thiết kế và xóa bản nháp đã lưu?')) {
    try {
      localStorage.removeItem(DRAFT_STORAGE_KEY);
      if (pageSnapshots) pageSnapshots.clear();
    } catch (e) {}

    studioPages = [
      { id: Date.now(), name: 'Trang 1', json: null, bg: '#e8d8c3', bgPattern: '/static/assets/patterns/pat_001.webp' }
    ];
    activePageIndex = 0;
    switchPage(0);
    showToast('✦ Đã làm mới trang xưởng thiết kế!', 'info');
  }
}

function manualSaveStudioDraft() {
  saveStudioDraftToStorage(true);
  showToast('💾 Đã lưu thành công bản thiết kế vào bộ nhớ trình duyệt!', 'success');
}

// Auto-save listeners on browser unload and page hide
window.addEventListener('beforeunload', () => {
  saveStudioDraftToStorage(true);
});

document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'hidden') {
    saveStudioDraftToStorage(true);
  }
});



// ================= LAYER B: ROBUST PAGE TEXTURE CACHE ENGINE (1 - 100+ PAGES) =================
let snapshotDebounceTimer = null;

function scheduleSnapshotUpdate() {
  if (snapshotDebounceTimer) clearTimeout(snapshotDebounceTimer);
  snapshotDebounceTimer = setTimeout(() => {
    if (!canvas || typeof activePageIndex === 'undefined') return;
    try {
      const liveSnap = canvas.toDataURL({ format: 'png', quality: 0.95, multiplier: 1.2 });
      if (pageSnapshots) {
        pageSnapshots.set(activePageIndex, liveSnap);
      }
      if (typeof updatePage3DTextureCache === 'function') {
        updatePage3DTextureCache(activePageIndex, liveSnap);
      }
    } catch (e) {}
  }, 200);
}

function getPageSnapshotDataUrl(pageIdx, onRenderedCallback) {
  if (pageIdx < 0) {
    if (onRenderedCallback) onRenderedCallback(null);
    return null;
  }

  // 1. If currently active page on 2D editor, snapshot directly
  if (pageIdx === activePageIndex && canvas) {
    try {
      const liveSnap = canvas.toDataURL({ format: 'png', quality: 0.95, multiplier: 1.2 });
      if (pageSnapshots) pageSnapshots.set(pageIdx, liveSnap);
      if (onRenderedCallback) onRenderedCallback(liveSnap);
      return liveSnap;
    } catch(e) {}
  }

  // 2. If cached snapshot exists, return immediately (0ms delay)
  if (pageSnapshots && pageSnapshots.has(pageIdx) && pageSnapshots.get(pageIdx)) {
    const cached = pageSnapshots.get(pageIdx);
    if (onRenderedCallback) onRenderedCallback(cached);
    return cached;
  }

  // 3. If studioPages has JSON, render asynchronously in offscreen canvas
  if (typeof studioPages !== 'undefined' && pageIdx < studioPages.length) {
    const page = studioPages[pageIdx];
    if (page && page.json) {
      try {
        const offElem = document.createElement('canvas');
        offElem.width = canvas ? canvas.getWidth() : 500;
        offElem.height = canvas ? canvas.getHeight() : 708;
        const tempCanvas = new fabric.StaticCanvas(offElem, {
          width: canvas ? canvas.getWidth() : 500,
          height: canvas ? canvas.getHeight() : 708
        });

        tempCanvas.loadFromJSON(page.json, () => {
          tempCanvas.renderAll();
          const snap = tempCanvas.toDataURL({ format: 'png', quality: 0.95, multiplier: 1.2 });
          if (pageSnapshots) pageSnapshots.set(pageIdx, snap);
          tempCanvas.dispose();
          if (onRenderedCallback) onRenderedCallback(snap);
        });
      } catch(e) {}
    }

    const fallbackUrl = (page && page.bgPattern) ? page.bgPattern : ((typeof currentPaperPatternUrl !== 'undefined') ? currentPaperPatternUrl : '/static/assets/patterns/pat_001.webp');
    if (onRenderedCallback) onRenderedCallback(fallbackUrl);
    return fallbackUrl;
  }

  const defaultUrl = (typeof currentPaperPatternUrl !== 'undefined') ? currentPaperPatternUrl : '/static/assets/patterns/pat_001.webp';
  if (onRenderedCallback) onRenderedCallback(defaultUrl);
  return defaultUrl;
}

function preRenderAllPagesSnapshots() {
  if (!studioPages || !Array.isArray(studioPages)) return;
  studioPages.forEach((page, idx) => {
    getPageSnapshotDataUrl(idx, () => {});
  });
}


// ================= GLOBAL WINDOW COMPONENT CLICK HANDLERS =================
window.handleStickerCardClick = function(elem) {
  if (!elem) return;
  const sku = elem.getAttribute('data-sku') || (elem.dataset && elem.dataset.sku);
  const name = elem.getAttribute('data-name') || (elem.dataset && elem.dataset.name);
  const image = elem.getAttribute('data-image') || (elem.dataset && elem.dataset.image);
  const price = parseFloat(elem.getAttribute('data-price') || (elem.dataset && elem.dataset.price)) || 3000;
  addStickerToCanvas(sku, name, image, price);
};

window.addStickerToCanvas = addStickerToCanvas;
window.addLayoutFrameToCanvas = addLayoutFrameToCanvas;
window.addTextLayoutToCanvas = addTextLayoutToCanvas;
window.promptPhotoForLayout = promptPhotoForLayout;
window.applyBackgroundPattern = applyBackgroundPattern;
window.setScrapbookCover = setScrapbookCover;
window.switchPage = switchPage;
window.addNewPage = addNewPage;
window.duplicatePage = duplicatePage;
window.deletePage = deletePage;
