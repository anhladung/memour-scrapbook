/**
 * Cart & Order Tracking Engine - ScrapCraft Studio
 * Clean Typography, Zero Emojis, Standardized Single Source of Truth
 */

let currentDiscountPercent = 0;
let freeShipping = false;

function formatVND(amount) {
  return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(amount);
}

function loadCartView() {
  const container = document.getElementById('cart-items-container');
  const emptyView = document.getElementById('empty-cart-view');
  const contentView = document.getElementById('cart-content-view');
  const countBadge = document.getElementById('cart-items-count');

  if (!container) return;

  const cart = JSON.parse(localStorage.getItem('scrapcraft_cart') || '[]');

  if (countBadge) countBadge.innerText = cart.reduce((sum, i) => sum + (i.quantity || 1), 0);

  if (cart.length === 0) {
    if (emptyView) emptyView.classList.remove('hidden');
    if (contentView) contentView.classList.add('hidden');
    return;
  }

  if (emptyView) emptyView.classList.add('hidden');
  if (contentView) contentView.classList.remove('hidden');

  let html = '';
  let subtotal = 0;

  cart.forEach((item, index) => {
    const itemTotal = (item.price || 0) * (item.quantity || 1);
    subtotal += itemTotal;

    html += `
      <div class="bg-stone-50 border-2 border-stone-200 rounded-2xl p-4 flex flex-col sm:flex-row items-center gap-4 transition-all hover:border-black">
        <div class="w-16 h-16 bg-white rounded-xl border border-stone-300 p-2 flex items-center justify-center flex-shrink-0">
          <img src="${item.image}" alt="${item.name}" class="w-full h-full object-contain">
        </div>
        
        <div class="flex-grow text-center sm:text-left">
          <div class="flex items-center justify-center sm:justify-start gap-2 mb-1">
            <span class="bg-stone-900 text-white text-[10px] font-mono font-bold px-2 py-0.5 rounded">${item.sku || 'SKU'}</span>
            <span class="text-[10px] text-stone-500 font-bold uppercase">${item.category || 'Phụ kiện'}</span>
          </div>
          <h4 class="font-heading font-bold text-stone-900 text-sm leading-tight">${item.name}</h4>
          <p class="text-rose-800 font-black text-xs mt-0.5">${formatVND(item.price)}</p>
        </div>

        <div class="flex items-center gap-3">
          <div class="flex items-center border border-black rounded-lg overflow-hidden bg-white font-bold text-xs">
            <button type="button" onclick="changeCartQty(${index}, -1)" class="w-7 h-7 flex items-center justify-center hover:bg-amber-300 transition-colors">-</button>
            <span class="w-8 text-center">${item.quantity || 1}</span>
            <button type="button" onclick="changeCartQty(${index}, 1)" class="w-7 h-7 flex items-center justify-center hover:bg-amber-300 transition-colors">+</button>
          </div>

          <p class="font-heading font-black text-stone-900 text-sm min-w-[90px] text-right">${formatVND(itemTotal)}</p>

          <button type="button" onclick="removeCartItem(${index})" class="text-stone-400 hover:text-rose-800 p-1 text-base font-bold transition-transform hover:scale-110" title="Xóa món này">
            &times;
          </button>
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
  calculateOrderTotals(subtotal);
}

function changeCartQty(index, delta) {
  let cart = JSON.parse(localStorage.getItem('scrapcraft_cart') || '[]');
  if (!cart[index]) return;

  cart[index].quantity = (cart[index].quantity || 1) + delta;
  if (cart[index].quantity <= 0) {
    cart.splice(index, 1);
  }

  localStorage.setItem('scrapcraft_cart', JSON.stringify(cart));
  updateCartCount();
  loadCartView();
}

function removeCartItem(index) {
  let cart = JSON.parse(localStorage.getItem('scrapcraft_cart') || '[]');
  cart.splice(index, 1);
  localStorage.setItem('scrapcraft_cart', JSON.stringify(cart));
  updateCartCount();
  loadCartView();
  showToast('Đã xóa món đồ khỏi giỏ hàng', 'info');
}

function clearAllCart() {
  localStorage.removeItem('scrapcraft_cart');
  updateCartCount();
  loadCartView();
  showToast('Đã làm trống giỏ hàng', 'info');
}

function calculateOrderTotals(subtotal) {
  const subtotalElem = document.getElementById('summary-subtotal');
  const discountElem = document.getElementById('summary-discount');
  const shippingElem = document.getElementById('summary-shipping');
  const finalElem = document.getElementById('summary-final');

  let shippingFee = subtotal > 350000 || freeShipping ? 0 : 30000;
  let discountAmount = Math.round(subtotal * currentDiscountPercent);
  let finalTotal = Math.max(0, subtotal - discountAmount + shippingFee);

  if (subtotalElem) subtotalElem.innerText = formatVND(subtotal);
  if (discountElem) discountElem.innerText = '-' + formatVND(discountAmount);
  if (shippingElem) shippingElem.innerText = shippingFee === 0 ? 'MIỄN PHÍ' : formatVND(shippingFee);
  if (finalElem) finalElem.innerText = formatVND(finalTotal);

  return { subtotal, discountAmount, shippingFee, finalTotal };
}

function applyVoucherCode() {
  const input = document.getElementById('voucher-input');
  const msgElem = document.getElementById('voucher-msg');
  if (!input) return;

  const code = input.value.trim().toUpperCase();
  if (code === 'GENZ10') {
    currentDiscountPercent = 0.10;
    showToast('Áp dụng mã GENZ10 thành công: Giảm 10% tổng đơn.', 'success');
    if (msgElem) {
      msgElem.innerText = 'Đã áp dụng mã GENZ10 (-10%)';
      msgElem.className = 'text-xs font-bold text-amber-900 block';
    }
  } else if (code === 'SCRAPCRAFT15') {
    currentDiscountPercent = 0.15;
    showToast('Áp dụng mã SCRAPCRAFT15 thành công: Giảm 15% tổng đơn.', 'success');
    if (msgElem) {
      msgElem.innerText = 'Đã áp dụng mã SCRAPCRAFT15 (-15%)';
      msgElem.className = 'text-xs font-bold text-rose-800 block';
    }
  } else if (code === 'FREESHIP') {
    freeShipping = true;
    showToast('Áp dụng mã FREESHIP thành công: Miễn phí vận chuyển.', 'success');
    if (msgElem) {
      msgElem.innerText = 'Đã áp dụng mã FREESHIP (Miễn phí ship)';
      msgElem.className = 'text-xs font-bold text-amber-900 block';
    }
  } else {
    showToast('Mã voucher không hợp lệ. Hãy thử: GENZ10 hoặc SCRAPCRAFT15', 'info');
    return;
  }

  loadCartView();
}

// Inspiration Bundle Quick Buy
async function buyInspirationBundle(inspId, bundlePrice) {
  try {
    const res = await fetch('/api/inspirations');
    const data = await res.json();
    const insp = (data.inspirations || []).find(i => i.id === inspId);

    if (!insp || !insp.components) {
      showToast('Không tìm thấy thông tin bộ mẫu', 'info');
      return;
    }

    let cart = JSON.parse(localStorage.getItem('scrapcraft_cart') || '[]');

    insp.components.forEach(comp => {
      const existing = cart.find(item => item.sku === comp.sku);
      if (existing) {
        existing.quantity += 1;
      } else {
        cart.push({
          sku: comp.sku,
          name: comp.name,
          price: 1000, // standard baseline unit price
          image: `/static/assets/${comp.sku.startsWith('STK') ? 'stickers/' + comp.sku.toLowerCase().replace('-', '_') + '.svg' : (comp.sku.startsWith('LAY') ? 'layouts/' + comp.sku.toLowerCase().replace('-', '_') + '.svg' : 'books/' + comp.sku.toLowerCase().replace('-', '_') + '.svg')}`,
          category: comp.sku.startsWith('STK') ? 'sticker' : (comp.sku.startsWith('LAY') ? 'layout' : 'scrapbook'),
          quantity: 1
        });
      }
    });

    localStorage.setItem('scrapcraft_cart', JSON.stringify(cart));
    updateCartCount();
    showToast(`Đã thêm trọn bộ ${insp.components.length} linh kiện của ${inspId} vào giỏ hàng!`, 'success');
  } catch (err) {
    console.error('Bundle error:', err);
  }
}

// Submit Customer Order
async function submitCustomerOrder(e) {
  e.preventDefault();

  const cart = JSON.parse(localStorage.getItem('scrapcraft_cart') || '[]');
  if (cart.length === 0) {
    showToast('Giỏ hàng của bạn đang trống!', 'info');
    return;
  }

  const name = document.getElementById('order-name').value.trim();
  const phone = document.getElementById('order-phone').value.trim();
  const address = document.getElementById('order-address').value.trim();
  const note = document.getElementById('order-note').value.trim();

  const subtotal = cart.reduce((sum, i) => sum + ((i.price || 0) * (i.quantity || 1)), 0);
  const totals = calculateOrderTotals(subtotal);

  const orderPayload = {
    name: name,
    phone: phone,
    address: address,
    note: note,
    items: cart,
    total_amount: totals.subtotal,
    discount_amount: totals.discountAmount,
    final_amount: totals.finalTotal
  };

  try {
    const res = await fetch('/api/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(orderPayload)
    });

    const result = await res.json();
    if (result.status === 'success') {
      localStorage.removeItem('scrapcraft_cart');
      updateCartCount();
      window.location.href = `/order-tracking?code=${result.order.order_code}`;
    } else {
      showToast('Có lỗi khi gửi đơn hàng, vui lòng thử lại.', 'info');
    }
  } catch (err) {
    showToast('Không thể kết nối đến máy chủ.', 'info');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  loadCartView();
});
