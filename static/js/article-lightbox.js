(() => {
  if (document.getElementById('article-lightbox')) return;

  const images = document.querySelectorAll('.legacy-article-hero, #article-content img');
  if (!images.length) return;

  const lightbox = document.createElement('div');
  lightbox.id = 'article-lightbox';
  lightbox.className = 'article-lightbox';
  lightbox.setAttribute('role', 'dialog');
  lightbox.setAttribute('aria-modal', 'true');
  lightbox.setAttribute('aria-label', 'Xem ảnh đầy đủ');
  lightbox.setAttribute('aria-hidden', 'true');
  lightbox.innerHTML = '<button type="button" class="article-lightbox-close" aria-label="Đóng ảnh">×</button><img src="" alt=""><p class="article-lightbox-caption"></p>';
  document.body.appendChild(lightbox);

  const fullImage = lightbox.querySelector('img');
  const caption = lightbox.querySelector('.article-lightbox-caption');
  const closeButton = lightbox.querySelector('.article-lightbox-close');
  let lastTrigger = null;

  function open(image) {
    lastTrigger = image;
    fullImage.src = image.currentSrc || image.src;
    fullImage.alt = image.alt || 'Ảnh bài viết';
    caption.textContent = image.alt || '';
    lightbox.classList.add('is-open');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.classList.add('lightbox-open');
    closeButton.focus();
  }

  function close() {
    lightbox.classList.remove('is-open');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('lightbox-open');
    fullImage.src = '';
    if (lastTrigger) lastTrigger.focus();
  }

  images.forEach((image) => {
    image.classList.add('article-zoomable');
    image.setAttribute('role', 'button');
    image.setAttribute('tabindex', '0');
    image.setAttribute('aria-label', `Xem ảnh đầy đủ: ${image.alt || 'Ảnh bài viết'}`);
    image.addEventListener('click', () => open(image));
    image.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        open(image);
      }
    });
  });

  closeButton.addEventListener('click', close);
  lightbox.addEventListener('click', (event) => {
    if (event.target === lightbox) close();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && lightbox.classList.contains('is-open')) close();
  });
})();
