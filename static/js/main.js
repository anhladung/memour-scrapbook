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

// Mid-Autumn Festival Decoration Controller
function initFestiveFrame() {
  const overlay = document.getElementById('trung-thu-frame-overlay');
  const toggleBtn = document.getElementById('trung-thu-toggle-btn');
  const toggleText = document.getElementById('festive-toggle-text');

  if (!overlay) return;

  const isHidden = localStorage.getItem('memour_trung_thu_hidden') === 'true';
  if (isHidden) {
    overlay.classList.add('hidden-festival');
    if (toggleText) toggleText.innerText = 'Bật Khung Trung Thu';
  } else {
    overlay.classList.remove('hidden-festival');
    if (toggleText) toggleText.innerText = 'Trung Thu 2026';
  }

  if (toggleBtn) {
    toggleBtn.addEventListener('click', () => {
      const currentlyHidden = overlay.classList.toggle('hidden-festival');
      localStorage.setItem('memour_trung_thu_hidden', currentlyHidden);
      if (toggleText) {
        toggleText.innerText = currentlyHidden ? 'Bật Khung Trung Thu' : 'Trung Thu 2026';
      }
      showToast(currentlyHidden ? 'Đã tạm ẩn khung trang trí Trung Thu 🏮' : 'Đã bật không khí Tết Trung Thu rộn ràng! 🏮🥮', 'info');
    });
  }
}


