/**
 * Main Application JS - ScrapCraft Studio
 */

// Toast Notifications
function showToast(message, type = 'success') {
  let toastContainer = document.getElementById('toast-container');
  if (!toastContainer) {
    toastContainer = document.createElement('div');
    toastContainer.id = 'toast-container';
    toastContainer.className = 'fixed bottom-6 right-6 z-50 flex flex-col gap-3 pointer-events-none';
    document.body.appendChild(toastContainer);
  }

  const toast = document.createElement('div');
  const bgClass = type === 'success' ? 'bg-amber-300 text-stone-900' : (type === 'info' ? 'bg-rose-800 text-white' : 'bg-stone-900 text-white');
  const icon = type === 'success' ? '✦' : (type === 'info' ? '◈' : '•');
  
  toast.className = `${bgClass} border-2 border-black font-heading font-black px-5 py-3 rounded-xl shadow-neo flex items-center gap-3 toast-badge pointer-events-auto transition-all duration-300 text-xs sm:text-sm`;
  toast.innerHTML = `
    <span class="text-base">${icon}</span>
    <span>${message}</span>
  `;

  toastContainer.appendChild(toast);
  
  setTimeout(() => toast.classList.add('show'), 10);
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// Update Cart Count Badge in Header
function updateCartCount() {
  const badge = document.getElementById('header-cart-count');
  if (!badge) return;
  
  try {
    const cart = JSON.parse(localStorage.getItem('scrapcraft_cart') || '[]');
    const totalItems = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
    badge.innerText = totalItems;
    if (totalItems > 0) {
      badge.classList.remove('hidden');
    } else {
      badge.classList.add('hidden');
    }
  } catch (e) {
    badge.innerText = '0';
  }
}

// Quick Add to Cart
function quickAddToCart(sku, name, price, image, category = 'item') {
  try {
    let cart = JSON.parse(localStorage.getItem('scrapcraft_cart') || '[]');
    const existingIndex = cart.findIndex(i => i.sku === sku);
    
    if (existingIndex > -1) {
      cart[existingIndex].quantity += 1;
    } else {
      cart.push({
        sku: sku,
        name: name,
        price: parseInt(price),
        image: image,
        category: category,
        quantity: 1
      });
    }
    
    localStorage.setItem('scrapcraft_cart', JSON.stringify(cart));
    updateCartCount();
    showToast(`Đã thêm ${sku} (${name}) vào giỏ hàng!`, 'success');
  } catch (e) {
    console.error('Cart add error:', e);
  }
}

// Mobile Menu Toggle & Festive Frame Init
document.addEventListener('DOMContentLoaded', () => {
  updateCartCount();
  initFestiveFrame();
  initSpookySpider();

  const mobileToggle = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-nav-drawer');
  if (mobileToggle && mobileMenu) {
    mobileToggle.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });
  }

  // Handle contact & subscribe form submits
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(contactForm);
      const data = Object.fromEntries(formData.entries());
      
      try {
        const res = await fetch('/api/contact-message', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        });
        const result = await res.json();
        showToast(result.message || 'Gửi lời nhắn thành công!', 'success');
        contactForm.reset();
      } catch (err) {
        showToast('Gửi lời nhắn thành công!', 'success');
        contactForm.reset();
      }
    });
  }

  // Initialize auto-rotator for all carousels on page
  initPageCarousels();
});

// ================= GLOBAL UNIFIED HORIZONTAL CAROUSEL SLIDER ENGINE =================
function slideCarouselTrack(carouselId, step) {
  const container = document.getElementById(carouselId);
  if (!container) return;
  const track = document.getElementById(`${carouselId}-track`);
  if (!track) return;

  const slides = track.querySelectorAll('.carousel-slide-item');
  if (slides.length === 0) return;

  const currentIndex = parseInt(container.getAttribute('data-current-index') || '0', 10);
  const nextIndex = (currentIndex + step + slides.length) % slides.length;
  setCarouselSlide(carouselId, nextIndex);
}

function setCarouselSlide(carouselId, targetIndex) {
  const container = document.getElementById(carouselId);
  if (!container) return;
  const track = document.getElementById(`${carouselId}-track`);
  if (!track) return;

  const slides = track.querySelectorAll('.carousel-slide-item');
  if (slides.length === 0) return;

  const validIndex = (targetIndex + slides.length) % slides.length;
  container.setAttribute('data-current-index', validIndex);

  // Smooth horizontal transform translation (Zero vertical jump, zero reload flash)
  track.style.transform = `translateX(-${validIndex * 100}%)`;

  // Update dot indicators
  const dots = container.querySelectorAll('.carousel-dot-btn');
  dots.forEach((dot, idx) => {
    if (idx === validIndex) {
      dot.className = 'carousel-dot-btn h-3 rounded-full border border-black bg-amber-400 w-7 transition-all duration-300 shadow-sm';
    } else {
      dot.className = 'carousel-dot-btn w-3 h-3 rounded-full border border-black bg-white/70 hover:bg-amber-300 transition-all duration-300';
    }
  });
}

// Backward compatibility aliases
function navigateCarousel(carouselId, step) {
  slideCarouselTrack(carouselId, step);
}

function goToCarouselSlide(carouselId, targetIndex) {
  setCarouselSlide(carouselId, targetIndex);
}

function initPageCarousels() {
  const carousels = document.querySelectorAll('.carousel-container, .unified-carousel');
  carousels.forEach(car => {
    const id = car.id;
    if (!id) return;

    let timer = setInterval(() => {
      slideCarouselTrack(id, 1);
    }, 6000);

    car.addEventListener('mouseenter', () => clearInterval(timer));
    car.addEventListener('mouseleave', () => {
      clearInterval(timer);
      timer = setInterval(() => {
        slideCarouselTrack(id, 1);
      }, 6000);
    });
  });
}

// Halloween & Festive Scrapbook Decoration Controller
function initFestiveFrame() {
  const overlay = document.getElementById('halloween-frame-overlay') || document.getElementById('trung-thu-frame-overlay');
  const toggleBtn = document.getElementById('festive-toggle-btn') || document.getElementById('trung-thu-toggle-btn');
  const toggleText = document.getElementById('festive-toggle-text');

  if (!overlay) return;

  const isHidden = localStorage.getItem('memour_halloween_hidden') === 'true' || localStorage.getItem('memour_trung_thu_hidden') === 'true';
  if (isHidden) {
    overlay.classList.add('hidden-festival');
    if (toggleText) toggleText.innerText = 'Bật Khung Halloween';
  } else {
    overlay.classList.remove('hidden-festival');
    if (toggleText) toggleText.innerText = 'Halloween 2026';
  }

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const currentlyHidden = overlay.classList.toggle('hidden-festival');
      localStorage.setItem('memour_halloween_hidden', currentlyHidden);
      if (toggleText) {
        toggleText.innerText = currentlyHidden ? 'Bật Khung Halloween' : 'Halloween 2026';
      }
      showToast(currentlyHidden ? 'Đã tạm ẩn khung trang trí Halloween 🎃' : 'Đã bật không khí Halloween Scrapbook rực rỡ! 🎃👻🍬', 'info');
    });
  }
}

// =========================================================
// INTERACTIVE HALLOWEEN 2026 SPIDER ENGINE
// =========================================================
function initSpookySpider() {
  const container = document.getElementById('spooky-spider-container');
  const actor = document.getElementById('spooky-spider-actor');
  const jumpWrapper = document.getElementById('spider-jump-wrapper');
  const flipWrapper = document.getElementById('spider-flip-wrapper');
  const toggleBtn = document.getElementById('spider-toggle-btn');
  const toggleText = document.getElementById('spider-toggle-text');
  const silkLine = document.getElementById('spider-silk-line');
  const bubble = document.getElementById('spider-speech-bubble');
  const bubbleText = document.getElementById('spider-speech-text');

  if (!container || !actor || !toggleBtn) return;

  const quotes = [
    "“MUMU không giăng tơ bắt mồi – MUMU giăng tơ giữ kỷ niệm.” 🕸️💖",
    "Boo! 👻 Tớ là MUMU the Spooky Spider - Người giữ ký ức đêm Halloween nè!",
    "Tớ vừa nhặt được 1 khoảnh khắc nhỏ xinh, cất vào scrapbook ngay! 📖✨",
    "MUMU giăng tơ lưu giữ nụ cười và kỷ niệm của bạn mùa Halloween này! 🍬",
    "Bắt được MUMU rồi! +10 điểm khéo tay dán sổ scrapbook thủ công! 🍭",
    "Mỗi trang sổ scrapbook là một kho báu ký ức lung linh cùng MUMU! 🌟",
    "Trick or Treat! Đừng để những kỷ niệm đẹp bị lãng quên nha! 🎃✨",
    "Hù! Cùng MUMU trang trí cuốn sổ lưu niệm thật ma mị và đáng yêu nhé! 👻",
    "MUMU tặng bạn 1 chiếc sticker bí ngô & viên kẹo ngọt ngào nè! 🍬🕸️"
  ];

  let active = false;
  let posX = Math.max(50, window.innerWidth * 0.2);
  let posY = -80;
  let speedX = 2.0;
  let isDropping = true;
  let isClimbing = false;
  let isPaused = false;
  let isJumping = false;
  let pauseTimer = null;
  let bubbleTimer = null;
  let animFrameId = null;

  function getGroundY() {
    return Math.max(120, window.innerHeight - 105);
  }

  function showBubble(text, duration = 2800) {
    if (!bubble || !bubbleText) return;
    bubbleText.innerText = text;
    bubble.classList.add('active-bubble');

    // Giữ bong bóng thoại luôn nằm trong màn hình và thẳng đứng không bị lật ngược
    if (posX < 80) {
      bubble.style.left = '10px';
      bubble.style.right = 'auto';
      bubble.style.transform = 'scale(1)';
    } else if (posX > window.innerWidth - 180) {
      bubble.style.left = 'auto';
      bubble.style.right = '10px';
      bubble.style.transform = 'scale(1)';
    } else {
      bubble.style.left = '50%';
      bubble.style.right = 'auto';
      bubble.style.transform = 'translateX(-50%) scale(1)';
    }

    clearTimeout(bubbleTimer);
    bubbleTimer = setTimeout(() => {
      bubble.classList.remove('active-bubble');
    }, duration);
  }

  function spawnCandySparkles(x, y) {
    const emojis = ['🍬', '✨', '🍭', '⭐', '🎃'];
    for (let i = 0; i < 6; i++) {
      const p = document.createElement('div');
      p.innerText = emojis[Math.floor(Math.random() * emojis.length)];
      p.style.position = 'fixed';
      p.style.left = (x + 20) + 'px';
      p.style.top = (y + 10) + 'px';
      p.style.fontSize = (14 + Math.random() * 8) + 'px';
      p.style.pointerEvents = 'none';
      p.style.zIndex = '1004';
      p.style.transition = 'all 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
      document.body.appendChild(p);

      const angle = (Math.PI * 2 * i) / 6;
      const dist = 30 + Math.random() * 40;
      setTimeout(() => {
        p.style.transform = `translate(${Math.cos(angle) * dist}px, ${Math.sin(angle) * dist - 30}px) scale(0.6)`;
        p.style.opacity = '0';
      }, 20);

      setTimeout(() => {
        if (p.parentNode) p.parentNode.removeChild(p);
      }, 850);
    }
  }

  function render() {
    if (!active && !isClimbing) return;

    const groundY = getGroundY();

    if (isDropping) {
      posY += 5;
      if (silkLine) {
        silkLine.setAttribute('x1', posX + 36);
        silkLine.setAttribute('y1', 0);
        silkLine.setAttribute('x2', posX + 36);
        silkLine.setAttribute('y2', posY + 16);
      }
      if (posY >= groundY) {
        posY = groundY;
        isDropping = false;
        actor.classList.add('spider-walking');
        showBubble("Boo! Tớ là MUMU - Người giữ ký ức đêm Halloween! 🕷️✨", 2500);
        if (silkLine) {
          silkLine.setAttribute('y2', 0);
        }
      }
    } else if (isClimbing) {
      posY -= 8;
      if (silkLine) {
        silkLine.setAttribute('x1', posX + 36);
        silkLine.setAttribute('y1', 0);
        silkLine.setAttribute('x2', posX + 36);
        silkLine.setAttribute('y2', posY + 16);
      }
      if (posY <= -90) {
        isClimbing = false;
        container.classList.add('hidden-spider');
        cancelAnimationFrame(animFrameId);
        return;
      }
    } else if (!isPaused && !isJumping) {
      // Normal horizontal crawling
      posX += speedX;
      const minX = 30;
      const maxX = Math.max(minX + 80, window.innerWidth - 100);

      if (posX >= maxX) {
        posX = maxX;
        speedX = -Math.abs(speedX);
        triggerPause("👀 Hết đường rồi, MUMU quay lại gom thêm ký ức thôi!");
      } else if (posX <= minX) {
        posX = minX;
        speedX = Math.abs(speedX);
        triggerPause("🍬 MUMU đi dạo dệt tơ kỷ niệm vòng nữa nào!");
      }

      // Chỉ lật hình ảnh bé nhện bên trong, tuyệt đối không lật toàn bộ actor (để chữ thoại không bị lộn ngược)
      if (flipWrapper) {
        flipWrapper.style.transform = speedX > 0 ? 'scaleX(1)' : 'scaleX(-1)';
      }
      actor.style.transform = 'none';
    }

    actor.style.left = posX + 'px';
    actor.style.top = posY + 'px';

    animFrameId = requestAnimationFrame(render);
  }

  function triggerPause(pauseMsg = null) {
    isPaused = true;
    actor.classList.remove('spider-walking');
    if (pauseMsg && Math.random() > 0.4) showBubble(pauseMsg, 1600);
    clearTimeout(pauseTimer);
    pauseTimer = setTimeout(() => {
      isPaused = false;
      if (active) actor.classList.add('spider-walking');
    }, 1000 + Math.random() * 800);
  }

  // Click on spider to interact!
  actor.addEventListener('click', (e) => {
    e.stopPropagation();
    if (isJumping) return;
    isJumping = true;
    actor.classList.remove('spider-walking');

    // Thêm hiệu ứng nhảy xoay vào jumpWrapper (không làm lộn ngược chữ trong bong bóng thoại)
    if (jumpWrapper) {
      jumpWrapper.classList.remove('spider-jumping');
      void jumpWrapper.offsetWidth; // Force reflow
      jumpWrapper.classList.add('spider-jumping');
    }

    const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    showBubble(randomQuote, 3200);
    spawnCandySparkles(posX, posY);

    setTimeout(() => {
      if (jumpWrapper) jumpWrapper.classList.remove('spider-jumping');
      isJumping = false;
      if (active && !isPaused) actor.classList.add('spider-walking');
    }, 700);
  });

  // Toggle button click
  function setSpiderState(toActive) {
    active = toActive;
    localStorage.setItem('memour_spider_active', active);

    if (active) {
      container.classList.remove('hidden-spider');
      isClimbing = false;
      isDropping = true;
      posY = -80;
      posX = Math.max(50, Math.min(window.innerWidth - 120, window.innerWidth * 0.25));
      if (jumpWrapper) jumpWrapper.classList.remove('spider-jumping');
      actor.classList.remove('spider-walking');
      actor.style.transform = 'none';
      if (flipWrapper) flipWrapper.style.transform = 'scaleX(1)';
      if (toggleText) toggleText.innerText = 'Cất MUMU Về Tổ';
      showToast('🕷️ Bé Nhện MUMU - “Người giữ ký ức đêm Halloween” đang dạo chơi! Nhấp vào MUMU để nhận kẹo & lắng nghe thông điệp nhé!', 'success');
      cancelAnimationFrame(animFrameId);
      animFrameId = requestAnimationFrame(render);
    } else {
      isClimbing = true;
      actor.classList.remove('spider-walking');
      showBubble("MUMU đi dệt thêm tơ ký ức đây! Hẹn gặp lại bạn nhé! 👋🕸️", 2000);
      if (toggleText) toggleText.innerText = 'Bé Nhện MUMU';
      showToast('🕷️ Bé Nhện MUMU đã về tổ dệt tơ kỷ niệm rồi!', 'info');
    }
  }

  toggleBtn.addEventListener('click', () => {
    setSpiderState(!active);
  });

  // Global helper to interact with MUMU from any button or banner
  window.summonMUMU = function() {
    if (!active) {
      setSpiderState(true);
      setTimeout(() => {
        if (actor) {
          actor.click();
          showToast('🕷️ MUMU: “MUMU không giăng tơ bắt mồi – MUMU giăng tơ giữ kỷ niệm.”', 'info');
        }
      }, 800);
    } else if (actor) {
      actor.click();
      showToast('🕷️ MUMU: “MUMU không giăng tơ bắt mồi – MUMU giăng tơ giữ kỷ niệm.”', 'info');
    }
  };

  // Auto-launch spider on load if previously enabled (or enable by default for Halloween vibe)
  const savedState = localStorage.getItem('memour_spider_active');
  if (savedState === 'true' || savedState === null) {
    setSpiderState(true);
  } else {
    if (toggleText) toggleText.innerText = 'Bé Nhện MUMU';
  }

  // Handle window resize gracefully
  window.addEventListener('resize', () => {
    if (!isDropping && !isClimbing) {
      posY = getGroundY();
      posX = Math.max(20, Math.min(window.innerWidth - 90, posX));
    }
  });
}

// =========================================================
// GEN Z INTERACTIVE MINI-GAME: MUMU GO SĂN STICKER TẶNG THẦY CÔ
// =========================================================
(function() {
  const STICKERS_DATA = [
    {
      id: 0,
      name: "Sticker Bí Ngô Điểm 10",
      icon: "🎃",
      svg: "/static/assets/stickers/halloween/bi-ngo-jack.svg",
      quote: "U là trời! Bí Ngô 10 Điểm! Chúc Thầy/Cô luôn chấm điểm hào phóng ngập tràn 10 điểm ạ! ✨",
      toast: "🎃 Đã nhặt Bí Ngô Điểm 10! Điểm thi kỳ này auto 10!"
    },
    {
      id: 1,
      name: "Sticker Cú Mèo Tri Thức",
      icon: "🦉",
      svg: "/static/assets/stickers/halloween/cu-meo-phu-thuy-kinh-ngo.svg",
      quote: "Flex nhẹ Cú Mèo Thông Thái! Tri thức của Thầy Cô đỉnh nóc kịch trần bay phấp phới! 🎓",
      toast: "🦉 Đã nhặt Cú Mèo Tri Thức! Cảm ơn người thầy thông thái!"
    },
    {
      id: 2,
      name: "Sticker Vạc Yêu Thương",
      icon: "🧪",
      svg: "/static/assets/stickers/halloween/vac-nuoc-phep-slime.svg",
      quote: "100 điểm tinh tế! Vạc tri thức nấu bằng tình thương bao la của Thầy Cô! 💜",
      toast: "🧪 Đã nhặt Vạc Yêu Thương! Tình thương thầy cô bao la!"
    },
    {
      id: 3,
      name: "Sticker Bé Ma Cute",
      icon: "👻",
      svg: "/static/assets/stickers/halloween/ma-cute-boo.svg",
      quote: "Bé Ma siêu cute gửi lời cảm ơn Thầy Cô đã luôn bao dung với tụi em! 🍬",
      toast: "👻 Đã nhặt Bé Ma Cute! Cảm ơn Thầy Cô luôn kiên nhẫn!"
    },
    {
      id: 4,
      name: "Sticker Trăng Tri Ân",
      icon: "🌙",
      svg: "/static/assets/stickers/halloween/mat-trang-khau-chi.svg",
      quote: "Keng keng! Trăng khâu chỉ ký ức – Dệt trọn tình cảm tri ân sâu sắc tới Thầy Cô! 💖",
      toast: "🌙 Đã nhặt Trăng Tri Ân! Sứ mạng hoàn thành xuất sắc!"
    }
  ];

  let modal = null;
  let arena = null;
  let player = null;
  let playerBubble = null;
  let stickersLayer = null;
  let counterEl = null;
  let victoryScreen = null;
  let toastEl = null;

  let playerX = 100;
  let playerY = 100;
  let targetX = 100;
  let targetY = 100;
  let speed = 4;
  let isMoving = false;
  let collectedCount = 0;
  let activeStickers = [];
  let gameLoopId = null;
  let bubbleTimer = null;
  let toastTimer = null;
  const keysDown = {};

  function playChime(freq = 580, type = 'triangle', duration = 0.15) {
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, ctx.currentTime);
      gain.gain.setValueAtTime(0.15, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + duration);
    } catch (e) {}
  }

  function playVictorySound() {
    [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
      setTimeout(() => playChime(freq, 'triangle', 0.25), i * 140);
    });
  }

  function showPlayerBubble(text, duration = 2500) {
    if (!playerBubble) return;
    playerBubble.innerText = text;
    playerBubble.style.opacity = '1';
    clearTimeout(bubbleTimer);
    bubbleTimer = setTimeout(() => {
      if (playerBubble) playerBubble.style.opacity = '0';
    }, duration);
  }

  function showArenaToast(text, duration = 2400) {
    if (!toastEl) return;
    toastEl.innerText = text;
    toastEl.style.opacity = '1';
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      if (toastEl) toastEl.style.opacity = '0';
    }, duration);
  }

  function spawnGameSparkles(x, y) {
    if (!arena) return;
    const emojis = ['🍬', '✨', '🍭', '⭐', '🎃', '💖'];
    for (let i = 0; i < 8; i++) {
      const p = document.createElement('div');
      p.innerText = emojis[Math.floor(Math.random() * emojis.length)];
      p.style.position = 'absolute';
      p.style.left = x + 'px';
      p.style.top = y + 'px';
      p.style.fontSize = (14 + Math.random() * 8) + 'px';
      p.style.pointerEvents = 'none';
      p.style.zIndex = '30';
      p.style.transition = 'all 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
      arena.appendChild(p);

      const angle = (Math.PI * 2 * i) / 8;
      const dist = 30 + Math.random() * 35;
      setTimeout(() => {
        p.style.transform = `translate(${Math.cos(angle) * dist}px, ${Math.sin(angle) * dist}px) scale(0.4)`;
        p.style.opacity = '0';
      }, 16);

      setTimeout(() => {
        if (p.parentNode) p.parentNode.removeChild(p);
      }, 650);
    }
  }

  function initElements() {
    modal = document.getElementById('mumu-game-modal');
    arena = document.getElementById('mumu-game-arena');
    player = document.getElementById('mumu-player');
    playerBubble = document.getElementById('mumu-player-bubble');
    stickersLayer = document.getElementById('mumu-stickers-layer');
    counterEl = document.getElementById('mumu-sticker-counter');
    victoryScreen = document.getElementById('mumu-victory-screen');
    toastEl = document.getElementById('mumu-arena-toast');
  }

  function spawnStickers() {
    if (!stickersLayer || !arena) return;
    stickersLayer.innerHTML = '';
    activeStickers = [];

    const rect = arena.getBoundingClientRect();
    const w = Math.max(300, rect.width || 600);
    const h = Math.max(260, rect.height || 360);
    const pad = 50;

    // Fixed / distributed locations so they never clump or spawn on top of each other
    const positions = [
      { x: pad + (w - pad * 2) * 0.15, y: pad + (h - pad * 2) * 0.25 },
      { x: pad + (w - pad * 2) * 0.85, y: pad + (h - pad * 2) * 0.20 },
      { x: pad + (w - pad * 2) * 0.50, y: pad + (h - pad * 2) * 0.82 },
      { x: pad + (w - pad * 2) * 0.18, y: pad + (h - pad * 2) * 0.78 },
      { x: pad + (w - pad * 2) * 0.80, y: pad + (h - pad * 2) * 0.75 }
    ];

    STICKERS_DATA.forEach((data, index) => {
      const pos = positions[index] || { x: w / 2, y: h / 2 };
      const el = document.createElement('div');
      el.className = 'mumu-target-sticker';
      el.id = `mumu-target-stk-${data.id}`;
      el.style.left = pos.x + 'px';
      el.style.top = pos.y + 'px';
      el.title = data.name;
      el.innerHTML = `<img src="${data.svg}" alt="${data.name}" class="w-full h-full object-contain pointer-events-none drop-shadow-md">`;
      stickersLayer.appendChild(el);

      activeStickers.push({
        id: data.id,
        x: pos.x,
        y: pos.y,
        el: el,
        data: data,
        collected: false
      });
    });
  }

  function updateSlotsUI() {
    if (counterEl) counterEl.innerText = `${collectedCount}/5`;
    document.querySelectorAll('#mumu-inventory-slots .mumu-slot').forEach(slot => {
      const slotId = parseInt(slot.getAttribute('data-slot'));
      const isCollected = activeStickers.find(s => s.id === slotId && s.collected);
      if (isCollected) {
        slot.classList.add('slot-collected');
      } else {
        slot.classList.remove('slot-collected');
      }
    });
  }

  function gameLoop() {
    if (!modal || modal.classList.contains('hidden')) return;

    if (!arena) initElements();
    const rect = arena.getBoundingClientRect();
    const w = rect.width || 600;
    const h = rect.height || 380;

    let moveX = 0;
    let moveY = 0;

    if (keysDown['ArrowUp'] || keysDown['KeyW'] || keysDown['w']) moveY -= speed;
    if (keysDown['ArrowDown'] || keysDown['KeyS'] || keysDown['s']) moveY += speed;
    if (keysDown['ArrowLeft'] || keysDown['KeyA'] || keysDown['a']) moveX -= speed;
    if (keysDown['ArrowRight'] || keysDown['KeyD'] || keysDown['d']) moveX += speed;

    if (moveX !== 0 || moveY !== 0) {
      playerX += moveX;
      playerY += moveY;
      targetX = playerX;
      targetY = playerY;
    } else if (isMoving) {
      const dx = targetX - playerX;
      const dy = targetY - playerY;
      const dist = Math.hypot(dx, dy);
      if (dist < 4) {
        playerX = targetX;
        playerY = targetY;
        isMoving = false;
      } else {
        playerX += (dx / dist) * speed;
        playerY += (dy / dist) * speed;
      }
    }

    // Clamp inside arena boundaries
    playerX = Math.max(30, Math.min(w - 30, playerX));
    playerY = Math.max(30, Math.min(h - 30, playerY));

    if (player) {
      player.style.left = playerX + 'px';
      player.style.top = playerY + 'px';
      if (moveX < 0 || (isMoving && targetX < playerX)) {
        player.style.transform = 'translate(-50%, -50%) scaleX(-1)';
      } else {
        player.style.transform = 'translate(-50%, -50%) scaleX(1)';
      }
    }

    // Check collision with remaining stickers
    activeStickers.forEach(stk => {
      if (stk.collected) return;
      const d = Math.hypot(playerX - stk.x, playerY - stk.y);
      if (d < 42) {
        stk.collected = true;
        collectedCount++;
        playChime(640 + collectedCount * 60, 'triangle', 0.2);
        spawnGameSparkles(stk.x, stk.y);

        if (stk.el) {
          stk.el.style.transform = 'translate(-50%, -50%) scale(1.6)';
          stk.el.style.opacity = '0';
          setTimeout(() => {
            if (stk.el && stk.el.parentNode) stk.el.parentNode.removeChild(stk.el);
          }, 250);
        }

        updateSlotsUI();
        showPlayerBubble(stk.data.quote, 3000);
        showArenaToast(stk.data.toast, 2400);

        if (collectedCount >= 5) {
          setTimeout(triggerVictory, 700);
        }
      }
    });

    gameLoopId = requestAnimationFrame(gameLoop);
  }

  function triggerVictory() {
    playVictorySound();
    if (victoryScreen) {
      victoryScreen.classList.remove('hidden');
    }
    showToast('🎉 Chúc mừng bạn và MUMU đã thu thập đủ 5 sticker kỷ niệm kính tặng Thầy Cô!', 'success');
  }

  window.openMumuGame = function() {
    initElements();
    if (!modal) return;
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';

    // Reset player position to center
    const rect = arena.getBoundingClientRect();
    playerX = (rect.width || 600) / 2;
    playerY = (rect.height || 380) / 2;
    targetX = playerX;
    targetY = playerY;
    isMoving = false;
    collectedCount = 0;

    if (victoryScreen) victoryScreen.classList.add('hidden');
    spawnStickers();
    updateSlotsUI();
    showPlayerBubble("Boo! Dùng phím mũi tên hoặc chạm để nhặt sticker nhé! 🍬", 2600);
    showArenaToast("✨ Dùng phím Mũi tên / WASD hoặc Chạm/Bấm chuột để điều khiển MUMU nhặt sticker!", 3000);

    cancelAnimationFrame(gameLoopId);
    gameLoopId = requestAnimationFrame(gameLoop);
  };

  window.closeMumuGame = function() {
    if (!modal) return;
    modal.classList.add('hidden');
    document.body.style.overflow = '';
    cancelAnimationFrame(gameLoopId);
  };

  window.restartMumuGame = function() {
    if (victoryScreen) victoryScreen.classList.add('hidden');
    collectedCount = 0;
    spawnStickers();
    updateSlotsUI();
    showPlayerBubble("Vòng mới bắt đầu! Cùng MUMU săn sticker tặng Thầy Cô nào! 🎒✨", 2500);
  };

  window.copyTeacherTribute = function() {
    const tributeText = `Kính gửi tặng các Thầy / Cô thân thương của chúng em! 💖\n\nNhóm học trò chúng em cùng Bé Nhện MUMU xin gửi tặng Thầy/Cô trọn bộ 5 Sticker Ký Ức Mùa Halloween 2026 độc bản này. Cảm ơn Thầy Cô vì đã luôn là ngọn hải đăng soi sáng tri thức, kiên nhẫn và bao dung cho những trò nghịch ngợm của tụi em!\n\n“MUMU không giăng tơ bắt mồi – MUMU giăng tơ giữ kỷ niệm.”\n\nKính chúc Thầy/Cô mùa lễ hội Halloween ngập tràn niềm vui, sức khỏe dồi dào và luôn giữ nụ cười hạnh phúc rạng rỡ trên bục giảng! ✨💐\n\n— Nhóm Học Trò Tinh Nghịch & MEMOUR Studio —`;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(tributeText).then(() => {
        showToast('📋 Đã sao chép trọn vẹn lời chúc tri ân Thầy Cô vào bộ nhớ tạm! Bạn có thể dán gửi ngay nhé! 💖', 'success');
      }).catch(() => {
        showToast('Đã sao chép lời chúc tri ân Thầy Cô!', 'info');
      });
    } else {
      showToast('Đã sao chép lời chúc tri ân Thầy Cô!', 'info');
    }
  };

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (!modal || modal.classList.contains('hidden')) return;
    if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'KeyW', 'KeyA', 'KeyS', 'KeyD', 'w', 'a', 's', 'd'].includes(e.code) || ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(e.key)) {
      e.preventDefault();
      keysDown[e.code || e.key] = true;
    }
    if (e.key === 'Escape') {
      window.closeMumuGame();
    }
  });

  window.addEventListener('keyup', (e) => {
    delete keysDown[e.code || e.key];
  });

  // Arena Click / Touch Event Listeners for smooth tap-to-move
  document.addEventListener('DOMContentLoaded', () => {
    initElements();
    if (arena) {
      const handlePointer = (e) => {
        const rect = arena.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clientY = e.touches ? e.touches[0].clientY : e.clientY;
        targetX = clientX - rect.left;
        targetY = clientY - rect.top;
        isMoving = true;
      };

      arena.addEventListener('mousedown', handlePointer);
      arena.addEventListener('touchstart', handlePointer, { passive: true });
    }

    // Mobile D-Pad Buttons
    document.querySelectorAll('.mumu-dpad-btn').forEach(btn => {
      const dir = btn.getAttribute('data-dir');
      const startMove = (e) => {
        e.preventDefault();
        if (dir === 'up') keysDown['ArrowUp'] = true;
        if (dir === 'down') keysDown['ArrowDown'] = true;
        if (dir === 'left') keysDown['ArrowLeft'] = true;
        if (dir === 'right') keysDown['ArrowRight'] = true;
      };
      const endMove = (e) => {
        e.preventDefault();
        delete keysDown['ArrowUp'];
        delete keysDown['ArrowDown'];
        delete keysDown['ArrowLeft'];
        delete keysDown['ArrowRight'];
      };
      btn.addEventListener('mousedown', startMove);
      btn.addEventListener('mouseup', endMove);
      btn.addEventListener('touchstart', startMove, { passive: false });
      btn.addEventListener('touchend', endMove, { passive: false });
    });
  });
})();



