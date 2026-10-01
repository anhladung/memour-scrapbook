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
    "Boo! 👻 Tớ là Nhện Memour 2026 nè!",
    "Bắt được tớ rồi! +10 điểm khéo tay DIY 🍬",
    "Trick or Treat! Nhớ dán sticker đẹp nha! 🎃",
    "Hù! Chúc bạn có mùa Halloween siêu ma mị! ✨",
    "Bé nhện đang đi tìm kẹo bắp Candy Corn đây 🍭",
    "Sáng tạo sổ scrapbook cùng Memour vui quá! 📖✨",
    "Chào bạn! Cùng dán sticker ma quái nào! 🕸️",
    "Bé nhện tặng bạn 1 chiếc sticker bí ngô nha! 🎃✨",
    "Ú òa! Scrapbook Memour làm quà tặng siêu ý nghĩa! 💝"
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
        showBubble("Boo! Bé nhện 2026 đã hạ cánh! 🕷️✨", 2200);
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
        triggerPause("👀 Hết đường rồi, quay lại thôi!");
      } else if (posX <= minX) {
        posX = minX;
        speedX = Math.abs(speedX);
        triggerPause("🍬 Đi dạo vòng nữa nào!");
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
    showBubble(randomQuote, 3000);
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
      if (toggleText) toggleText.innerText = 'Bắt Nhện Về Tổ';
      showToast('🕷️ Bé nhện Halloween 2026 đang trượt xuống dạo chơi! Nhấp vào bé nhện để nhận kẹo nhé!', 'success');
      cancelAnimationFrame(animFrameId);
      animFrameId = requestAnimationFrame(render);
    } else {
      isClimbing = true;
      actor.classList.remove('spider-walking');
      showBubble("Bye bye! Hẹn gặp lại nhé! 👋🕸️", 1800);
      if (toggleText) toggleText.innerText = 'Thả Nhện 2026';
      showToast('🕷️ Bé nhện đã leo lên trần nhà ngủ rồi!', 'info');
    }
  }

  toggleBtn.addEventListener('click', () => {
    setSpiderState(!active);
  });

  // Auto-launch spider on load if previously enabled (or enable by default for Halloween vibe)
  const savedState = localStorage.getItem('memour_spider_active');
  if (savedState === 'true' || savedState === null) {
    setSpiderState(true);
  } else {
    if (toggleText) toggleText.innerText = 'Thả Nhện 2026';
  }

  // Handle window resize gracefully
  window.addEventListener('resize', () => {
    if (!isDropping && !isClimbing) {
      posY = getGroundY();
      posX = Math.max(20, Math.min(window.innerWidth - 90, posX));
    }
  });
}



