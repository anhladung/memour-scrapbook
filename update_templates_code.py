import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# 1. templates/index.html
index_html = '''{% extends "base.html" %}

{% block title %}ScrapCraft Studio - Sổ Scrapbook & Phụ Kiện Thủ Công Giấy Gen Z{% endblock %}

{% block content %}
{% import "components/carousel.html" as carousels %}

{% set home_slides = [
  {
    "badge": "GEN Z SCRAPBOOKING REVOLUTION",
    "title": "Bật Mood <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>Sáng Tạo</span> Gói Ký Ức Vào Giấy Thủ Công!",
    "desc": "Đừng để những bức ảnh đẹp ngủ quên trong điện thoại! Tự do phối <b>Sticker 3D Hologram</b>, <b>Khung ảnh Polaroid</b> và <b>Sổ bìa còng Kraft</b> thành tác phẩm độc bản.",
    "buttons": [
      { "text": "Khám Phá Xưởng Thiết Kế 3D", "url": "/studio", "primary": true },
      { "text": "Khám Phá Sản Phẩm", "url": "/products", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_002.svg",
    "corner_badge": "100% Giấy FSC Eco Acid-Free"
  },
  {
    "badge": "MÔ PHỎNG 3D 360° CHÂN THỰC",
    "title": "Xem Trước Từng Góc Cạnh Với <span class='text-rose-800'>Trình Xem 3D</span>",
    "desc": "Quan sát ánh kim Hologram bắt sáng và chi tiết dập nổi 0.8mm trên bề mặt giấy thật trước khi quyết định đặt làm.",
    "buttons": [
      { "text": "Trải Nghiệm Xưởng 3D Ngay", "url": "/studio", "primary": true },
      { "text": "Xem Mẫu Bố Cục", "url": "/inspiration", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_001.svg",
    "corner_badge": "360° WebGL Real-time"
  },
  {
    "badge": "KHO PHỤ KIỆN CHÍNH HÃNG",
    "title": "24 Mã Định Danh Đồng Bộ <span class='text-rose-800'>Single Source of Truth</span>",
    "desc": "Từ nhãn dán dập nổi 3D, khung cài polaroid không hỏng ảnh đến giấy mỹ thuật nhập khẩu tiêu chuẩn bảo tàng.",
    "buttons": [
      { "text": "Xem Kho Phụ Kiện", "url": "/products", "primary": true },
      { "text": "Đọc Cẩm Nang Kỹ Thuật", "url": "/guide", "primary": false }
    ],
    "image": "/static/assets/books/scr_001.svg",
    "corner_badge": "Chuẩn Mã SKU 100%"
  }
] %}

{{ carousels.render_carousel("home-hero-carousel", home_slides) }}

<!-- ================= SECTION 2: CTA XƯỞNG THIẾT KẾ & 3D 360° ================= -->
<section class="py-16 md:py-24 bg-stone-950 text-white relative overflow-hidden border-b-2 border-black">
  <div class="absolute -top-24 -left-24 w-96 h-96 bg-rose-900/30 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-24 -right-24 w-96 h-96 bg-amber-600/20 rounded-full blur-3xl pointer-events-none"></div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
    <div class="bg-gradient-to-br from-stone-900 via-stone-900 to-rose-950 border-3 border-amber-400 rounded-3xl p-8 sm:p-12 shadow-neo-xl">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        <div class="lg:col-span-7 space-y-6">
          <div class="inline-flex items-center gap-2 bg-rose-800 text-white border border-rose-600 px-3.5 py-1 rounded-full text-xs font-black">
            <span>✦ TÍNH NĂNG ĐỘT PHÁ CÔNG NGHỆ</span>
          </div>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-black text-white leading-tight">
            Xưởng Thiết Kế <span class="text-amber-300">Canvas 2D</span> &amp; Trình Xem <span class="text-rose-400">3D 360°</span> Sống Động
          </h2>
          <p class="text-stone-300 text-sm sm:text-base leading-relaxed">
            Trực tiếp kéo thả sticker, layout ảnh và tải ảnh kỷ niệm của bạn lên từng trang sổ. Đặc biệt, trình xem <b>3D 360 độ</b> mô phỏng chân thực <b>hiệu ứng dập nổi 0.8mm và ánh sáng phản chiếu</b> của từng chi tiết thủ công!
          </p>

          <!-- Feature Bullets -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
            <div class="bg-stone-800/80 border border-stone-700 p-3.5 rounded-xl">
              <span class="text-amber-400 font-mono font-bold text-lg block mb-1">01.</span>
              <h4 class="font-bold text-sm text-white">Kéo Thả Tùy Ý</h4>
              <p class="text-xs text-stone-400">Tự do xoay, thu phóng, xếp lớp zIndex</p>
            </div>
            <div class="bg-stone-800/80 border border-stone-700 p-3.5 rounded-xl">
              <span class="text-amber-400 font-mono font-bold text-lg block mb-1">02.</span>
              <h4 class="font-bold text-sm text-amber-300">AI Bố Cục Tự Động</h4>
              <p class="text-xs text-stone-400">Nhập ý tưởng, AI tự chọn SKU và tọa độ</p>
            </div>
            <div class="bg-stone-800/80 border border-stone-700 p-3.5 rounded-xl">
              <span class="text-amber-400 font-mono font-bold text-lg block mb-1">03.</span>
              <h4 class="font-bold text-sm text-rose-300">Xem 3D 360 Độ</h4>
              <p class="text-xs text-stone-400">Mô phỏng vân giấy mộc và màng laser</p>
            </div>
          </div>

          <div class="pt-4">
            <a href="/studio" class="inline-flex items-center gap-3 bg-amber-400 hover:bg-amber-300 text-black font-heading font-black text-base px-8 py-4 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all">
              <span>Khám Phá Xưởng Thiết Kế</span>
              <span class="text-lg font-mono">→</span>
            </a>
          </div>
        </div>

        <!-- 3D Interactive Preview Visual Box -->
        <div class="lg:col-span-5 flex justify-center">
          <div class="relative w-full max-w-sm aspect-square bg-stone-950 border-2 border-rose-600 rounded-3xl p-4 shadow-neo flex flex-col items-center justify-center text-center group">
            <div class="w-full h-full rounded-2xl overflow-hidden relative flex items-center justify-center bg-gradient-to-b from-rose-950/40 to-stone-900">
              <img src="/static/assets/books/scr_001.svg" alt="3D Scrapbook" class="w-48 h-48 object-contain transform group-hover:scale-105 group-hover:rotate-3 transition-transform duration-500">
              <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent flex flex-col justify-end p-4">
                <span class="bg-rose-700 text-white text-[11px] font-black px-2.5 py-1 rounded-full self-center mb-1">360° Real-time WebGL</span>
                <p class="text-xs text-stone-300 font-bold">Xoay 360° &amp; Chạm Thử Độ Nổi</p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</section>

<!-- ================= SECTION 3: GIỚI THIỆU DOANH NGHIỆP (BENTO CRAFT) ================= -->
<section class="py-16 md:py-24 bg-[#fbf8f2] border-b-2 border-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="text-center max-w-2xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 bg-amber-300 border-2 border-black px-3.5 py-1 rounded-full text-xs font-black uppercase mb-3 shadow-neo">
        <span>✦ Câu Chuyện Của Chúng Tôi</span>
      </div>
      <h2 class="text-3xl sm:text-4xl font-heading font-black text-stone-900 leading-tight">
        Tái Sinh Ký Ức Số Thành <br class="hidden sm:inline"> Những Trang Giấy <span class="bg-rose-800 text-white px-2 py-0.5 rounded-lg">Biết Kể Chuyện</span>
      </h2>
    </div>

    <!-- Bento Grid Layout -->
    <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
      
      <!-- Bento 1: Mission Card -->
      <div class="md:col-span-2 bg-white border-2 border-black rounded-3xl p-8 shadow-neo flex flex-col justify-between hover:border-rose-700 transition-colors">
        <div>
          <span class="text-amber-800 font-black text-lg block mb-2 font-mono">✦ SỨ MỆNH</span>
          <h3 class="text-2xl font-heading font-extrabold text-stone-900 mb-2">Sứ Mệnh ScrapCraft Studio</h3>
          <p class="text-stone-600 text-sm leading-relaxed">
            {{ company.story.mission }}
          </p>
        </div>
        <div class="mt-6 flex items-center gap-3 pt-4 border-t border-stone-100">
          <span class="bg-amber-100 text-amber-800 font-black text-xs px-2.5 py-1 rounded-full">#AnalogVibes</span>
          <span class="bg-rose-100 text-rose-800 font-black text-xs px-2.5 py-1 rounded-full">#GenZCraft</span>
        </div>
      </div>

      <!-- Bento 2: Craft Fact 1 -->
      <div class="bg-amber-300 border-2 border-black rounded-3xl p-6 shadow-neo flex flex-col justify-between">
        <span class="text-xs font-black text-stone-800 uppercase tracking-wider">Tiêu Chuẩn Giấy</span>
        <div>
          <span class="text-4xl font-heading font-black text-black">100%</span>
          <p class="text-xs font-bold text-stone-800 mt-1">Giấy mỹ thuật Acid-free nhập khẩu bảo vệ ảnh lâu bền</p>
        </div>
        <div class="text-stone-900 font-bold text-xs">Chuẩn FSC Quốc Tế</div>
      </div>

      <!-- Bento 3: Craft Fact 2 -->
      <div class="bg-rose-800 text-white border-2 border-black rounded-3xl p-6 shadow-neo flex flex-col justify-between">
        <span class="text-xs font-black text-rose-200 uppercase tracking-wider">Độ Nổi Dập Nổi 3D</span>
        <div>
          <span class="text-4xl font-heading font-black text-white">0.8 mm</span>
          <p class="text-xs font-medium text-rose-200 mt-1">Dập nổi chi tiết tạo hiệu ứng nổi khối chân thực</p>
        </div>
        <div class="text-amber-300 font-bold text-xs">Màng Hologram Laser</div>
      </div>

      <!-- Bento 4: Process Feature -->
      <div class="md:col-span-2 bg-rose-50 border-2 border-black rounded-3xl p-6 shadow-neo flex flex-col justify-between">
        <div>
          <span class="text-rose-800 font-black text-lg block mb-2 font-mono">✦ TRIẾT LÝ</span>
          <h4 class="font-heading font-black text-lg text-stone-900 mb-1">Triết Lý Thủ Công &amp; Độc Bản</h4>
          <p class="text-xs text-stone-700 leading-relaxed">
            Mỗi bộ scrapbook được thiết kế từ linh kiện mô-đun hóa: Bạn có thể chọn bìa sổ, layout khung ảnh và sticker theo câu chuyện của riêng mình.
          </p>
        </div>
        <div class="mt-4">
          <a href="/about" class="text-xs font-black text-rose-800 underline flex items-center gap-1">
            Câu chuyện của chúng tôi →
          </a>
        </div>
      </div>

      <!-- Bento 5: AI & 3D Innovation -->
      <div class="md:col-span-2 bg-white border-2 border-black rounded-3xl p-6 shadow-neo flex items-center gap-4">
        <div class="w-14 h-14 bg-amber-100 rounded-2xl border border-black flex items-center justify-center flex-shrink-0 font-heading font-black text-rose-800 text-lg">
          AI
        </div>
        <div>
          <h4 class="font-heading font-bold text-base text-stone-900">Chưa Biết Bắt Đầu Thế Nào?</h4>
          <p class="text-xs text-stone-600 mt-0.5">
            Nhập ý tưởng (dịp tốt nghiệp, sinh nhật, du lịch), trợ lý AI sẽ tự động phân tích và dàn trang bằng linh kiện thực trong kho!
          </p>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ================= SECTION 4: GIỚI THIỆU SẢN PHẨM CHỦ ĐẠO ================= -->
<section class="py-16 md:py-24 bg-white border-b-2 border-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
      <div>
        <div class="inline-flex items-center gap-2 bg-rose-100 text-rose-800 border border-rose-300 px-3.5 py-1 rounded-full text-xs font-black uppercase mb-2">
          <span>✦ 3 DÒNG SẢN PHẨM CỐT LÕI</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-heading font-black text-stone-900">
          Phụ Kiện Chuẩn Gu - Mã Định Danh Đồng Bộ
        </h2>
      </div>
      <a href="/products" class="inline-flex items-center gap-2 text-sm font-black text-rose-800 hover:text-rose-950 underline">
        Xem tất cả sản phẩm ({% if featured_stickers %}{{ featured_stickers|length + featured_layouts|length + featured_books|length }}{% else %}24{% endif %} mã) →
      </a>
    </div>

    <!-- Product Trio Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Group 1: STICKER -->
      <div class="bg-[#fdfbf7] border-2 border-black rounded-3xl p-6 shadow-neo hover:border-rose-700 transition-all flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="bg-rose-800 text-white text-xs font-black px-3 py-1 rounded-full">STK-001 .. STK-012</span>
            <span class="text-xs font-bold text-stone-500">Sticker &amp; Decal 3D</span>
          </div>
          <div class="w-full aspect-video bg-amber-50 rounded-2xl border border-black/10 p-4 flex items-center justify-center mb-5">
            <img src="/static/assets/stickers/stk_001.svg" alt="Sticker" class="max-h-28 object-contain">
          </div>
          <h3 class="font-heading font-bold text-xl text-stone-900 mb-2">Sticker &amp; Decal Nổi 3D</h3>
          <p class="text-xs text-stone-600 leading-relaxed mb-4">
            Màng Hologram phản quang laser, dập nổi 3D đa tầng 0.8mm và giấy Washi xé tay tự nhiên. Tương thích trực tiếp với Xưởng Thiết Kế.
          </p>
          <div class="text-xs text-stone-500 space-y-1 mb-4">
            <p>• <b>Chất liệu:</b> Decal Vinyl dập nổi, Giấy Washi tự nhiên</p>
            <p>• <b>Độ nổi:</b> 0.2mm - 0.8mm, phản quang ánh sáng thật</p>
          </div>
        </div>
        <a href="/products?category=sticker" class="w-full text-center bg-rose-100 hover:bg-rose-200 text-rose-900 font-bold text-xs py-2.5 rounded-xl border border-rose-300 transition-colors">
          Xem Kho Sticker (STK-xxx) →
        </a>
      </div>

      <!-- Group 2: LAYOUT -->
      <div class="bg-[#fdfbf7] border-2 border-black rounded-3xl p-6 shadow-neo hover:border-amber-600 transition-all flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="bg-amber-600 text-white text-xs font-black px-3 py-1 rounded-full">LAY-001 .. LAY-008</span>
            <span class="text-xs font-bold text-stone-500">Layout Khung Ảnh</span>
          </div>
          <div class="w-full aspect-video bg-rose-50 rounded-2xl border border-black/10 p-4 flex items-center justify-center mb-5">
            <img src="/static/assets/layouts/lay_001.svg" alt="Layout" class="max-h-28 object-contain">
          </div>
          <h3 class="font-heading font-bold text-xl text-stone-900 mb-2">Layout Khung Ảnh Thủ Công</h3>
          <p class="text-xs text-stone-600 leading-relaxed mb-4">
            Khung Polaroid cài góc giấy không hỏng ảnh, dải phim 35mm hoài cổ và cơ chế gập Accordion 3D tương tác.
          </p>
          <div class="text-xs text-stone-500 space-y-1 mb-4">
            <p>• <b>Chất liệu:</b> Giấy mỹ thuật Canson bồi 350gsm</p>
            <p>• <b>Kỹ thuật:</b> Khe cài thông minh giữ nguyên ảnh gốc</p>
          </div>
        </div>
        <a href="/products?category=layout" class="w-full text-center bg-amber-100 hover:bg-amber-200 text-amber-900 font-bold text-xs py-2.5 rounded-xl border border-amber-300 transition-colors">
          Xem Kho Layout (LAY-xxx) →
        </a>
      </div>

      <!-- Group 3: BOOK -->
      <div class="bg-[#fdfbf7] border-2 border-black rounded-3xl p-6 shadow-neo hover:border-stone-800 transition-all flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="bg-stone-900 text-white text-xs font-black px-3 py-1 rounded-full">SCR-001 .. SCR-004</span>
            <span class="text-xs font-bold text-stone-500">Sổ Scrapbook Bìa Cứng</span>
          </div>
          <div class="w-full aspect-video bg-stone-100 rounded-2xl border border-black/10 p-4 flex items-center justify-center mb-5">
            <img src="/static/assets/books/scr_001.svg" alt="Book" class="max-h-28 object-contain">
          </div>
          <h3 class="font-heading font-bold text-xl text-stone-900 mb-2">Cuốn Sổ Scrapbook Thủ Công</h3>
          <p class="text-xs text-stone-600 leading-relaxed mb-4">
            Bìa cứng dày 3mm bọc Kraft mộc mạc, da PU pastel mềm mại hoặc vải Linen dệt thô. Còng kim loại mở linh hoạt để thêm bớt trang.
          </p>
          <div class="text-xs text-stone-500 space-y-1 mb-4">
            <p>• <b>Chất liệu:</b> Bìa Carton 1200gsm + Giấy Kraft đen/nâu 300gsm</p>
            <p>• <b>Đặc điểm:</b> Chống cong vênh, bảo quản bền lâu</p>
          </div>
        </div>
        <a href="/products?category=scrapbook" class="w-full text-center bg-stone-200 hover:bg-stone-300 text-stone-900 font-bold text-xs py-2.5 rounded-xl border border-stone-400 transition-colors">
          Xem Các Mẫu Sổ (SCR-xxx) →
        </a>
      </div>

    </div>
  </div>
</section>

<!-- ================= SECTION 5: CÁC MẪU THAM KHẢO NỔI BẬT ================= -->
<section class="py-16 md:py-24 bg-[#fbf8f2] border-b-2 border-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
      <div>
        <div class="inline-flex items-center gap-2 bg-amber-300 border-2 border-black px-3.5 py-1 rounded-full text-xs font-black uppercase mb-2 shadow-neo">
          <span>✦ 100% SỬ DỤNG LINH KIỆN CÓ SẴN TRONG KHO</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-heading font-black text-stone-900">
          Mẫu Tham Khảo Ý Tưởng &amp; Remix Sáng Tạo
        </h2>
      </div>
      <a href="/inspiration" class="inline-flex items-center gap-2 bg-white text-stone-900 font-bold text-sm px-5 py-2.5 rounded-xl border-2 border-black shadow-neo shadow-neo-hover transition-all">
        Xem thêm cảm hứng →
      </a>
    </div>

    <!-- Inspirations Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {% for insp in inspirations[:3] %}
      <div class="bg-white border-2 border-black rounded-3xl overflow-hidden shadow-neo flex flex-col justify-between group hover:border-rose-700 transition-all">
        <div>
          <!-- Image -->
          <div class="w-full aspect-[4/3] bg-stone-100 relative overflow-hidden border-b-2 border-black">
            <img src="{{ insp.image }}" alt="{{ insp.title }}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <span class="absolute top-3 right-3 bg-black text-white text-[10px] font-black px-2.5 py-1 rounded-full">
              {{ insp.theme }}
            </span>
          </div>
          <!-- Body -->
          <div class="p-6">
            <span class="text-xs font-bold text-amber-800 uppercase tracking-wider block mb-1">Mã tham khảo: {{ insp.id }}</span>
            <h4 class="font-heading font-extrabold text-lg text-stone-900 leading-snug mb-2">{{ insp.title }}</h4>
            <p class="text-xs text-stone-600 line-clamp-2 leading-relaxed mb-4">{{ insp.description }}</p>
            
            <!-- Component Badges (Strict SKUs only) -->
            <div class="border-t border-stone-100 pt-3">
              <span class="text-[11px] font-bold text-stone-500 block mb-1.5">Linh kiện cấu thành:</span>
              <div class="flex flex-wrap gap-1.5">
                {% for comp in insp.components %}
                <span class="text-[10px] font-bold bg-stone-100 text-stone-800 px-2 py-0.5 rounded border border-stone-300">{{ comp.sku }}</span>
                {% endfor %}
              </div>
            </div>
          </div>
        </div>

        <!-- Actions -->
        <div class="p-6 pt-0 space-y-2">
          <a href="/studio?remix={{ insp.id }}" class="block w-full text-center bg-rose-800 hover:bg-rose-900 text-white font-extrabold text-xs py-3 rounded-xl border border-black shadow-sm transition-colors">
            Mở Trong Xưởng Thiết Kế →
          </a>
        </div>
      </div>
      {% endfor %}
    </div>

  </div>
</section>

<!-- ================= SECTION 6: CẨM NANG NỔI BẬT (SEO BLOG) ================= -->
<section class="py-16 md:py-24 bg-white border-b-2 border-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
      <div>
        <div class="inline-flex items-center gap-2 bg-rose-100 text-rose-800 border border-rose-300 px-3.5 py-1 rounded-full text-xs font-black uppercase mb-2">
          <span>✦ CẨM NANG THỦ CÔNG &amp; TIPS SEO</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-heading font-black text-stone-900">
          Bí Kíp Layering &amp; Ý Tưởng Scrapbook Hot Trend
        </h2>
      </div>
      <a href="/guide" class="inline-flex items-center gap-2 text-sm font-black text-rose-800 hover:text-rose-950 underline">
        Xem cẩm nang →
      </a>
    </div>

    <!-- Blogs Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      {% for blog in blogs[:3] %}
      <article class="bg-[#fdfbf7] border-2 border-black rounded-3xl overflow-hidden shadow-neo flex flex-col justify-between hover:border-rose-700 transition-all">
        <div>
          <div class="w-full aspect-video bg-rose-50 border-b-2 border-black overflow-hidden relative">
            <img src="{{ blog.cover_image }}" alt="{{ blog.title }}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-500">
            <span class="absolute bottom-3 left-3 bg-amber-300 text-black text-[10px] font-black px-2 py-0.5 rounded border border-black">
              {{ blog.read_time }}
            </span>
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 text-xs text-stone-500 font-bold mb-2">
              <span>{{ blog.published_date }}</span>
              <span>•</span>
              <span class="text-rose-800 font-black">{{ blog.category }}</span>
            </div>
            <h3 class="font-heading font-bold text-lg text-stone-900 leading-snug mb-2 hover:text-rose-800 transition-colors">
              <a href="/guide/{{ blog.slug }}">{{ blog.title }}</a>
            </h3>
            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed">
              {{ blog.excerpt }}
            </p>
          </div>
        </div>

        <div class="p-6 pt-0">
          <a href="/guide/{{ blog.slug }}" class="text-xs font-black text-rose-800 hover:text-rose-950 flex items-center gap-1">
            Đọc tiếp cẩm nang →
          </a>
        </div>
      </article>
      {% endfor %}
    </div>

  </div>
</section>

<!-- ================= SECTION 7: CONTACT POSTCARD SECTION ================= -->
<section class="py-16 md:py-24 bg-gradient-to-b from-[#fdfbf7] to-amber-100/50 relative">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="bg-white border-3 border-black rounded-3xl p-8 sm:p-12 shadow-neo-xl relative">
      <div class="washi-tape-top"></div>

      <div class="text-center max-w-lg mx-auto mb-8">
        <div class="inline-flex items-center gap-2 bg-amber-300 border-2 border-black px-3.5 py-1 rounded-full text-xs font-black uppercase mb-2 shadow-neo">
          <span>✦ Gửi Lời Nhắn Tới Xưởng</span>
        </div>
        <h2 class="text-3xl font-heading font-black text-stone-900">
          Kết Nối Cùng ScrapCraft Studio
        </h2>
        <p class="text-xs text-stone-600 mt-1">
          Bạn cần tư vấn set phụ kiện riêng cho lớp, đặt in số lượng lớn hoặc có ý tưởng muốn hợp tác? Hãy để lại lời nhắn nhé!
        </p>
      </div>

      <form id="contact-form" class="space-y-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label class="block text-xs font-black text-stone-800 uppercase mb-1">Tên của bạn *</label>
            <input type="text" name="name" required placeholder="VD: Linh Đan" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-sm font-medium focus:bg-white focus:outline-none focus:border-rose-700">
          </div>
          <div>
            <label class="block text-xs font-black text-stone-800 uppercase mb-1">Số điện thoại / Zalo *</label>
            <input type="tel" name="phone" required placeholder="0988 xxx xxx" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-sm font-medium focus:bg-white focus:outline-none focus:border-rose-700">
          </div>
        </div>

        <div>
          <label class="block text-xs font-black text-stone-800 uppercase mb-1">Email của bạn</label>
          <input type="email" name="email" placeholder="you@gmail.com" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-sm font-medium focus:bg-white focus:outline-none focus:border-rose-700">
        </div>

        <div>
          <label class="block text-xs font-black text-stone-800 uppercase mb-1">Lời nhắn / Ý tưởng cần hỗ trợ</label>
          <textarea name="message" rows="3" placeholder="Chia sẻ với xưởng về cuốn sổ hoặc dự án bạn đang ấp ủ..." class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-sm font-medium focus:bg-white focus:outline-none focus:border-rose-700"></textarea>
        </div>

        <button type="submit" class="w-full bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-sm py-3.5 rounded-xl border-2 border-black shadow-neo shadow-neo-hover transition-all">
          Gửi Lời Nhắn Ngay →
        </button>
      </form>

    </div>

  </div>
</section>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)
print('Updated templates/index.html')

# 2. templates/about.html
about_html = '''{% extends "base.html" %}

{% block title %}Về Chúng Tôi - Câu Chuyện Thương Hiệu ScrapCraft Studio{% endblock %}

{% block content %}
{% import "components/carousel.html" as carousels %}

{% set about_slides = [
  {
    "badge": "CÂU CHUYỆN THƯƠNG HIỆU",
    "title": "Tái Sinh Ký Ức Số Thành <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>Trang Sổ Biết Kể Chuyện</span>",
    "desc": "Khởi nguồn từ niềm đam mê chất liệu giấy mỹ thuật và mong muốn đưa ký ức xúc chạm trở lại giữa kỷ nguyên số ngập tràn dữ liệu ảo.",
    "buttons": [
      { "text": "Khám Phá Xưởng Thiết Kế", "url": "/studio", "primary": true },
      { "text": "Xem Sản Phẩm", "url": "/products", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_001.svg",
    "corner_badge": "Thủ Công Độc Bản"
  },
  {
    "badge": "100% NGUYÊN LIỆU GIẤY FSC",
    "title": "Chất Liệu Giấy Mỹ Thuật <span class='text-rose-800'>Acid-Free Cao Cấp</span>",
    "desc": "100% nguyên liệu giấy nhập khẩu có chứng chỉ bảo vệ rừng bền vững, không axit giúp ảnh polaroid và mực viết không bị ố vàng theo năm tháng.",
    "buttons": [
      { "text": "Khám Phá Phụ Kiện", "url": "/products", "primary": true },
      { "text": "Quy Trình Gia Công", "url": "#craft-process", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_003.svg",
    "corner_badge": "FSC Certified Paper"
  },
  {
    "badge": "TIÊN PHONG CÔNG NGHỆ 3D & AI",
    "title": "Kết Nối Thủ Công Tinh Xảo Với <span class='text-rose-800'>Trí Tuệ Nhân Tạo</span>",
    "desc": "Ứng dụng mô phỏng 3D WebGL 360 độ và thuật toán AI gợi ý bố cục thông minh, giúp việc sáng tạo scrapbook trở nên dễ dàng và chuẩn xác.",
    "buttons": [
      { "text": "Vào Xưởng 3D & AI", "url": "/studio", "primary": true },
      { "text": "Liên Hệ Xưởng", "url": "/contact", "primary": false }
    ],
    "image": "/static/assets/books/scr_002.svg",
    "corner_badge": "AI & 3D Tech"
  }
] %}

{{ carousels.render_carousel("about-carousel", about_slides) }}

<!-- Brand Storytelling Visual Section -->
<section class="py-16 md:py-24 bg-white border-b-2 border-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      
      <!-- Visual Collage (Scrapbook Opened Metaphor) -->
      <div class="lg:col-span-6 relative">
        <div class="w-full bg-[#fdfbf7] border-3 border-black rounded-3xl p-6 shadow-neo-xl relative">
          <div class="washi-tape-top"></div>
          <img src="/static/assets/layouts/insp_001.svg" alt="Craft Workshop" class="w-full h-auto rounded-2xl border border-stone-300">
          
          <div class="absolute -bottom-6 -left-6 bg-amber-300 border-2 border-black rounded-2xl p-4 shadow-neo max-w-[200px] hidden sm:block">
            <span class="font-mono font-black text-xs text-stone-900 block mb-1">✦ CHỨNG CHỈ</span>
            <p class="text-xs font-black text-black">100% Giấy Chuẩn FSC &amp; Acid-Free</p>
          </div>

          <div class="absolute -top-6 -right-6 bg-rose-800 text-white border-2 border-black rounded-2xl p-4 shadow-neo max-w-[180px] hidden sm:block">
            <span class="font-mono font-black text-xs text-amber-300 block mb-1">✦ CÔNG NGHỆ</span>
            <p class="text-xs font-black">Dập Nổi 3D &amp; Phủ Laser Hologram</p>
          </div>
        </div>
      </div>

      <!-- Story Text -->
      <div class="lg:col-span-6 space-y-6">
        <div class="inline-flex items-center gap-2 bg-rose-100 text-rose-800 px-3 py-1 rounded-full text-xs font-black uppercase border border-rose-300">
          <span>Khởi nguồn từ một góc bàn thủ công</span>
        </div>
        <h2 class="text-3xl sm:text-4xl font-heading font-black text-stone-900 leading-tight">
          Tại sao lại là Scrapbook trong thời đại số?
        </h2>
        <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
          Chúng ta có hàng ngàn bức ảnh lưu trữ trong điện thoại hay đám mây nhưng hiếm khi mở ra nhìn lại. Một cuốn Scrapbook thủ công không chỉ là nơi dán ảnh, mà là nơi cảm xúc được chạm vào bằng tay: cảm nhận từng thớ giấy Kraft mộc mạc, sự lấp lánh của sticker dập nổi và nét chữ tay nắn nót.
        </p>
        <p class="text-stone-700 text-sm sm:text-base leading-relaxed">
          Tại <b>ScrapCraft Studio</b>, chúng tôi kết hợp tinh thần sáng tạo Gen Z với công nghệ hiện đại: từ việc ứng dụng <b>trợ lý AI phân tích ý tưởng gợi ý bố cục</b> đến <b>trình xem 3D 360 độ chân thực</b>, giúp bất kỳ ai cũng có thể tự tay tạo nên cuốn sổ kỷ niệm độc bản mà không cần phải là một nghệ nhân chuyên nghiệp.
        </p>

        <div class="grid grid-cols-2 gap-4 pt-2">
          <div class="border-l-4 border-amber-500 pl-4">
            <span class="font-heading font-black text-2xl text-stone-900">2023</span>
            <p class="text-xs text-stone-600 font-bold">Khởi xướng dự án DIY Scrapbook tại TP. Hồ Chí Minh</p>
          </div>
          <div class="border-l-4 border-rose-800 pl-4">
            <span class="font-heading font-black text-2xl text-stone-900">5.000+</span>
            <p class="text-xs text-stone-600 font-bold">Cuốn sổ độc bản đã trao gửi tới các bạn trẻ cả nước</p>
          </div>
        </div>
      </div>

    </div>

  </div>
</section>

<!-- Craftsmanship & Quality Standards (4 Pillars) -->
<section id="craft-process" class="py-16 md:py-24 bg-[#fbf8f2] border-b-2 border-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="text-center max-w-2xl mx-auto mb-16">
      <div class="inline-flex items-center gap-2 bg-amber-300 border-2 border-black px-3.5 py-1 rounded-full text-xs font-black uppercase mb-3 shadow-neo">
        <span>✦ TIÊU CHUẨN XƯỞNG THỦ CÔNG</span>
      </div>
      <h2 class="text-3xl sm:text-4xl font-heading font-black text-stone-900">
        4 Cam Kết Chất Lượng Độc Bản
      </h2>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      
      <!-- Pillar 1 -->
      <div class="bg-white border-2 border-black rounded-3xl p-6 shadow-neo flex flex-col justify-between hover:border-rose-700 transition-colors">
        <div>
          <span class="font-heading font-black text-2xl text-rose-800 mb-3 block font-mono">01.</span>
          <h3 class="font-heading font-bold text-lg text-stone-900 mb-2">Giấy Acid-Free Chuẩn FSC</h3>
          <p class="text-xs text-stone-600 leading-relaxed">
            Giấy mỹ thuật định lượng 300 - 350gsm không chứa axit tự do, ngăn chặn triệt để hiện tượng ố vàng ảnh và phai màu mực theo năm tháng.
          </p>
        </div>
        <div class="mt-6 pt-4 border-t border-stone-100 text-xs font-bold text-amber-800">
          Tiêu chuẩn bảo tàng quốc tế
        </div>
      </div>

      <!-- Pillar 2 -->
      <div class="bg-white border-2 border-black rounded-3xl p-6 shadow-neo flex flex-col justify-between hover:border-rose-700 transition-colors">
        <div>
          <span class="font-heading font-black text-2xl text-amber-600 mb-3 block font-mono">02.</span>
          <h3 class="font-heading font-bold text-lg text-stone-900 mb-2">Dập Nổi 3D &amp; Ép Kim Tinh Xảo</h3>
          <p class="text-xs text-stone-600 leading-relaxed">
            Từng chi tiết sticker được dập nổi viền sắc nét với độ sâu 0.8mm, phủ màng Hologram phản chiếu ánh sáng lấp lánh chân thực.
          </p>
        </div>
        <div class="mt-6 pt-4 border-t border-stone-100 text-xs font-bold text-rose-800">
          Hiệu ứng xúc chạm nổi khối
        </div>
      </div>

      <!-- Pillar 3 -->
      <div class="bg-white border-2 border-black rounded-3xl p-6 shadow-neo flex flex-col justify-between hover:border-rose-700 transition-colors">
        <div>
          <span class="font-heading font-black text-2xl text-stone-900 mb-3 block font-mono">03.</span>
          <h3 class="font-heading font-bold text-lg text-stone-900 mb-2">Khung Cài Giấy Không Hỏng Ảnh</h3>
          <p class="text-xs text-stone-600 leading-relaxed">
            Thiết kế khe cài góc thông minh cho ảnh polaroid, cho phép bạn dễ dàng thay đổi ảnh mà không cần dán băng dính trực tiếp lên bề mặt ảnh.
          </p>
        </div>
        <div class="mt-6 pt-4 border-t border-stone-100 text-xs font-bold text-stone-700">
          Bảo vệ tối đa kỷ vật gốc
        </div>
      </div>

      <!-- Pillar 4 -->
      <div class="bg-white border-2 border-black rounded-3xl p-6 shadow-neo flex flex-col justify-between hover:border-rose-700 transition-colors">
        <div>
          <span class="font-heading font-black text-2xl text-rose-800 mb-3 block font-mono">04.</span>
          <h3 class="font-heading font-bold text-lg text-stone-900 mb-2">Đồng Bộ Mã Định Danh SKU</h3>
          <p class="text-xs text-stone-600 leading-relaxed">
            Mọi phụ kiện bạn nhìn thấy trong xưởng thiết kế online đều có sẵn chính xác 100% trong kho thực tế, đảm bảo thành phẩm y hệt bản thảo.
          </p>
        </div>
        <div class="mt-6 pt-4 border-t border-stone-100 text-xs font-bold text-amber-800">
          Single Source of Truth
        </div>
      </div>

    </div>

  </div>
</section>

<!-- Call to action in studio -->
<section class="py-16 md:py-20 bg-gradient-to-r from-stone-900 via-rose-950 to-amber-950 text-white text-center border-b-2 border-black">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
    <h2 class="text-3xl sm:text-4xl font-heading font-black">
      Sẵn Sàng Tự Tay Tạo Nên Cuốn Sổ Kỷ Niệm Của Riêng Bạn?
    </h2>
    <p class="text-stone-300 text-sm sm:text-base max-w-xl mx-auto leading-relaxed">
      Thử nghiệm kéo thả sticker, bố cục khung ảnh và xoay ngắm tác phẩm 360 độ trong không gian 3D tương tác.
    </p>
    <div class="pt-4 flex flex-wrap justify-center gap-4">
      <a href="/studio" class="bg-amber-400 hover:bg-amber-300 text-stone-950 font-heading font-black text-sm px-8 py-3.5 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all">
        Vào Xưởng Thiết Kế Ngay →
      </a>
      <a href="/products" class="bg-white hover:bg-stone-100 text-stone-900 font-heading font-bold text-sm px-7 py-3.5 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all">
        Xem Kho Phụ Kiện
      </a>
    </div>
  </div>
</section>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'about.html'), 'w', encoding='utf-8') as f:
    f.write(about_html)
print('Updated templates/about.html')

# 3. templates/products.html
products_html = '''{% extends "base.html" %}

{% block title %}Cửa Hàng Phụ Kiện Scrapbook & Sổ Thủ Công - ScrapCraft Studio{% endblock %}

{% block content %}
{% import "components/carousel.html" as carousels %}

{% set products_slides = [
  {
    "badge": "DANH MỤC PHỤ KIỆN CHÍNH HÃNG",
    "title": "Kho Phụ Kiện <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>Chuẩn Gu Gen Z</span> 24 Mã SKU",
    "desc": "Mỗi sản phẩm đều sở hữu mã định danh (SKU) chuẩn hóa đồng bộ 100% với Xưởng Thiết Kế 2D, Trình Xem 3D và Thuật Toán AI.",
    "buttons": [
      { "text": "Mở Trong Xưởng 3D", "url": "/studio", "primary": true },
      { "text": "Xem Mẫu Bố Cục", "url": "/inspiration", "primary": false }
    ],
    "image": "/static/assets/stickers/stk_001.svg",
    "corner_badge": "24 SKU Đồng Bộ"
  },
  {
    "badge": "STICKER 3D & DECAL NỔI",
    "title": "Sticker Dập Nổi 0.8mm <span class='text-rose-800'>Phủ Màng Hologram Laser</span>",
    "desc": "Bắt sáng lung linh dưới mọi góc nhìn, chất liệu vinyl chống nước và giấy washi xé tay tự nhiên mang lại vẻ đẹp hoài cổ.",
    "buttons": [
      { "text": "Lọc Sticker 3D", "url": "/products?category=sticker", "primary": true },
      { "text": "Khám Phá Sổ Kraft", "url": "/products?category=scrapbook", "primary": false }
    ],
    "image": "/static/assets/stickers/stk_002.svg",
    "corner_badge": "Dập Nổi 3D"
  },
  {
    "badge": "KHUNG POLAROID & BÌA SỔ FSC",
    "title": "Layout Khung Cài Thông Minh & <span class='text-rose-800'>Sổ Bìa Cứng Kraft</span>",
    "desc": "Không làm hỏng ảnh kỷ niệm, bìa carton dày 3mm chống cong vênh kết hợp còng kim loại mở linh hoạt để thêm bớt trang.",
    "buttons": [
      { "text": "Xem Khung Polaroid", "url": "/products?category=layout", "primary": true },
      { "text": "Xem Các Mẫu Sổ", "url": "/products?category=scrapbook", "primary": false }
    ],
    "image": "/static/assets/books/scr_001.svg",
    "corner_badge": "100% Giấy FSC"
  }
] %}

{{ carousels.render_carousel("products-carousel", products_slides) }}

<!-- Filter & Search Controls Bar -->
<section class="bg-white py-8 border-b-2 border-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
      
      <!-- Search Bar -->
      <form action="/products" method="GET" class="flex items-center gap-2 max-w-md w-full">
        <input type="text" name="q" value="{{ search_q }}" placeholder="Tìm theo mã SKU, từ khóa (y2k, vintage, polaroid...)" class="flex-grow bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800 shadow-sm">
        <button type="submit" class="bg-rose-800 hover:bg-rose-900 text-white font-bold text-xs px-4 py-2.5 rounded-xl border-2 border-black shadow-neo transition-all">
          Tìm kiếm
        </button>
      </form>

      <!-- Quick 3D Filter & Sort Dropdown -->
      <div class="flex items-center gap-2 flex-wrap">
        <a href="/products?category={{ selected_category }}&is_3d={% if selected_3d == 'true' %}all{% else %}true{% endif %}" class="px-3.5 py-2 rounded-xl text-xs font-black border-2 border-black transition-all {% if selected_3d == 'true' %}bg-amber-300 text-stone-900 shadow-neo{% else %}bg-stone-100 text-stone-700 hover:bg-amber-100{% endif %}">
          ✦ Dập Nổi 3D ({% if selected_3d == 'true' %}Đang lọc{% else %}Bật{% endif %})
        </a>
        <select onchange="location = this.value;" class="bg-white border-2 border-black rounded-xl px-3 py-2 text-xs font-bold text-stone-800 focus:outline-none shadow-sm">
          <option value="/products?category={{ selected_category }}&sort=default" {% if selected_sort == 'default' %}selected{% endif %}>Sắp xếp mặc định</option>
          <option value="/products?category={{ selected_category }}&sort=price_asc" {% if selected_sort == 'price_asc' %}selected{% endif %}>Giá: Thấp đến Cao</option>
          <option value="/products?category={{ selected_category }}&sort=price_desc" {% if selected_sort == 'price_desc' %}selected{% endif %}>Giá: Cao đến Thấp</option>
          <option value="/products?category={{ selected_category }}&sort=name_asc" {% if selected_sort == 'name_asc' %}selected{% endif %}>Tên A-Z</option>
        </select>
      </div>
    </div>

    <!-- Category Tabs -->
    <div class="flex flex-wrap items-center gap-2 mt-6 pt-4 border-t border-stone-200">
      <a href="/products?category=all{% if selected_3d != 'all' %}&is_3d={{ selected_3d }}{% endif %}" class="px-4 py-2 rounded-xl text-xs font-black border-2 border-black transition-all {% if selected_category == 'all' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">
        Tất Cả ({{ categories_stat.all }})
      </a>
      <a href="/products?category=sticker{% if selected_3d != 'all' %}&is_3d={{ selected_3d }}{% endif %}" class="px-4 py-2 rounded-xl text-xs font-black border-2 border-black transition-all {% if selected_category == 'sticker' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">
        Sticker &amp; Decal 3D ({{ categories_stat.sticker }})
      </a>
      <a href="/products?category=layout{% if selected_3d != 'all' %}&is_3d={{ selected_3d }}{% endif %}" class="px-4 py-2 rounded-xl text-xs font-black border-2 border-black transition-all {% if selected_category == 'layout' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">
        Layout Khung Ảnh ({{ categories_stat.layout }})
      </a>
      <a href="/products?category=scrapbook{% if selected_3d != 'all' %}&is_3d={{ selected_3d }}{% endif %}" class="px-4 py-2 rounded-xl text-xs font-black border-2 border-black transition-all {% if selected_category == 'scrapbook' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">
        Sổ Scrapbook Bìa Cứng ({{ categories_stat.scrapbook }})
      </a>
    </div>
  </div>
</section>

<!-- Product List Grid -->
<section class="py-12 md:py-16 bg-[#fdfbf7]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    {% if products|length == 0 %}
    <div class="bg-white border-2 border-black rounded-3xl p-12 text-center shadow-neo max-w-lg mx-auto">
      <span class="text-rose-800 font-mono font-black text-2xl block mb-3 font-mono">✦</span>
      <h3 class="font-heading font-black text-lg text-stone-900 mb-1">Không tìm thấy sản phẩm phù hợp</h3>
      <p class="text-xs text-stone-600 mb-4">Vui lòng thử tìm kiếm với từ khóa hoặc danh mục khác.</p>
      <a href="/products" class="inline-block bg-rose-800 text-white font-bold text-xs px-5 py-2.5 rounded-xl border border-black shadow-sm">
        Xem tất cả sản phẩm
      </a>
    </div>
    {% else %}
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      {% for item in products %}
      <div class="bg-white border-2 border-black rounded-3xl overflow-hidden shadow-neo flex flex-col justify-between hover:border-rose-700 transition-all group">
        <div>
          <!-- Thumbnail Box -->
          <div class="w-full aspect-square bg-[#fbf8f2] relative border-b-2 border-black p-4 flex items-center justify-center overflow-hidden">
            <img src="{{ item.image }}" alt="{{ item.name }}" class="max-h-40 object-contain group-hover:scale-105 transition-transform duration-300">
            
            <span class="absolute top-3 left-3 bg-stone-900 text-white text-[10px] font-mono font-black px-2 py-0.5 rounded border border-black shadow-sm">
              {{ item.sku }}
            </span>
            
            {% if item.is_3d %}
            <span class="absolute top-3 right-3 bg-amber-300 text-stone-950 text-[10px] font-black px-2 py-0.5 rounded border border-black shadow-sm">
              3D Relief
            </span>
            {% endif %}
          </div>

          <!-- Content -->
          <div class="p-5">
            <div class="text-[11px] font-bold text-amber-800 uppercase tracking-wider mb-1">
              {{ item.category|capitalize }} • {{ item.material or (item.attributes and item.attributes.material) or 'Thủ công' }}
            </div>
            
            <h3 class="font-heading font-bold text-base text-stone-900 leading-snug line-clamp-1 hover:text-rose-800 transition-colors">
              <a href="/product/{{ item.sku }}">{{ item.name }}</a>
            </h3>

            <p class="text-xs text-stone-500 line-clamp-2 mt-1 leading-relaxed">
              {{ item.description }}
            </p>

            <div class="mt-4 flex items-baseline justify-between border-t border-stone-100 pt-3">
              <span class="text-xs text-stone-500 font-semibold">Giá bán:</span>
              <span class="font-heading font-black text-lg text-rose-800">{{ item.price|format_vnd }}</span>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="p-5 pt-0 grid grid-cols-2 gap-2">
          <button onclick="quickAddToCart('{{ item.sku }}', '{{ item.name }}', {{ item.price }}, '{{ item.image }}', '{{ item.category }}')" class="w-full bg-amber-300 hover:bg-amber-400 text-stone-950 font-bold text-xs py-2.5 rounded-xl border border-black shadow-sm transition-colors text-center">
            Thêm Vào Giỏ
          </button>
          <a href="/studio?sku={{ item.sku }}" class="w-full bg-rose-800 hover:bg-rose-900 text-white font-bold text-xs py-2.5 rounded-xl border border-black shadow-sm transition-colors text-center">
            Mở Trong Xưởng →
          </a>
        </div>
      </div>
      {% endfor %}
    </div>
    {% endif %}

  </div>
</section>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'products.html'), 'w', encoding='utf-8') as f:
    f.write(products_html)
print('Updated templates/products.html')

# 4. templates/product_detail.html
product_detail_html = '''{% extends "base.html" %}

{% block title %}{{ product.name }} ({{ product.sku }}) - ScrapCraft Studio{% endblock %}

{% block content %}
<div class="py-10 bg-[#fdfbf7]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <!-- Breadcrumbs -->
    <nav class="flex items-center gap-2 text-xs font-bold text-stone-500 mb-8">
      <a href="/" class="hover:text-rose-800">Trang chủ</a>
      <span>/</span>
      <a href="/products" class="hover:text-rose-800">Sản phẩm</a>
      <span>/</span>
      <a href="/products?category={{ product.category }}" class="hover:text-rose-800">{{ product.category|capitalize }}</a>
      <span>/</span>
      <span class="text-stone-900 font-mono">{{ product.sku }}</span>
    </nav>

    <!-- Product Main Box -->
    <div class="bg-white border-3 border-black rounded-3xl p-6 sm:p-10 shadow-neo-xl grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <!-- Product Image Gallery -->
      <div class="lg:col-span-6 flex flex-col items-center justify-center">
        <div class="w-full aspect-square bg-[#fbf8f2] border-2 border-black rounded-3xl p-8 flex items-center justify-center relative shadow-inner">
          <div class="washi-tape-top"></div>
          <img src="{{ product.image }}" alt="{{ product.name }}" class="max-h-72 object-contain drop-shadow-md">
          
          <div class="absolute top-4 left-4 bg-stone-900 text-white font-mono font-black text-xs px-3 py-1 rounded-md border border-black shadow-sm">
            {{ product.sku }}
          </div>

          {% if product.is_3d %}
          <div class="absolute top-4 right-4 bg-amber-300 text-stone-950 font-black text-xs px-3 py-1 rounded-md border border-black shadow-sm">
            ✦ Hiệu Ứng Nổi 3D
          </div>
          {% endif %}
        </div>
      </div>

      <!-- Product Info & Direct Actions -->
      <div class="lg:col-span-6 space-y-6">
        <div>
          <div class="inline-flex items-center gap-2 bg-rose-100 text-rose-800 border border-rose-300 px-3 py-1 rounded-full text-xs font-black uppercase mb-2">
            <span>{{ product.category|capitalize }}</span>
          </div>
          <h1 class="text-2xl sm:text-3xl lg:text-4xl font-heading font-black text-stone-900 leading-tight">
            {{ product.name }}
          </h1>
          <p class="text-xs font-mono font-bold text-stone-400 mt-1">Mã định danh kho: {{ product.sku }}</p>
        </div>

        <!-- Price -->
        <div class="flex items-baseline gap-4 border-y border-stone-200 py-4">
          <span class="text-3xl font-heading font-black text-rose-800">{{ product.price|format_vnd }}</span>
          <span class="text-xs text-stone-500 font-bold bg-amber-100 text-amber-900 px-2.5 py-1 rounded-full border border-amber-200">
            100% Sẵn hàng tại Showroom
          </span>
        </div>

        <p class="text-stone-700 text-sm leading-relaxed">
          {{ product.description }}
        </p>

        <!-- Technical Specs Table -->
        <div class="bg-stone-50 border-2 border-black rounded-2xl p-4 space-y-2 text-xs">
          <div class="font-heading font-black text-stone-900 uppercase tracking-wider mb-2">Thông Số Kỹ Thuật:</div>
          {% if product.attributes %}
            {% for key, val in product.attributes.items() %}
            <div class="flex justify-between border-b border-stone-200/80 pb-1.5 last:border-0 last:pb-0">
              <span class="text-stone-500 font-bold capitalize">{{ key.replace('_', ' ') }}:</span>
              <span class="text-stone-900 font-black">{{ val }}</span>
            </div>
            {% endfor %}
          {% elif product.specs %}
            {% for key, val in product.specs.items() %}
            <div class="flex justify-between border-b border-stone-200/80 pb-1.5 last:border-0 last:pb-0">
              <span class="text-stone-500 font-bold capitalize">{{ key.replace('_', ' ') }}:</span>
              <span class="text-stone-900 font-black">{{ val }}</span>
            </div>
            {% endfor %}
          {% endif %}
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-3 pt-2">
          <button onclick="quickAddToCart('{{ product.sku }}', '{{ product.name }}', {{ product.price }}, '{{ product.image }}', '{{ product.category }}')" class="flex-1 bg-amber-300 hover:bg-amber-400 text-stone-950 font-heading font-black text-sm py-4 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all text-center">
            Thêm Vào Giỏ Hàng
          </button>
          
          <a href="/studio?sku={{ product.sku }}" class="flex-1 bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-sm py-4 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all text-center flex items-center justify-center gap-2">
            <span>Mở Trong Xưởng 3D</span>
            <span class="font-mono">→</span>
          </a>
        </div>

      </div>

    </div>

    <!-- Related Products -->
    {% if related_products %}
    <div class="mt-16">
      <div class="flex items-center justify-between mb-8">
        <h3 class="text-2xl font-heading font-black text-stone-900">Sản Phẩm Cùng Bộ Sưu Tập</h3>
        <a href="/products?category={{ product.category }}" class="text-xs font-black text-rose-800 underline">Xem tất cả →</a>
      </div>
      
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6">
        {% for rel in related_products %}
        <div class="bg-white border-2 border-black rounded-3xl overflow-hidden shadow-neo flex flex-col justify-between hover:border-rose-700 transition-all group">
          <div class="p-4 bg-[#fbf8f2] border-b-2 border-black flex items-center justify-center">
            <img src="{{ rel.image }}" alt="{{ rel.name }}" class="max-h-32 object-contain group-hover:scale-105 transition-transform duration-300">
          </div>
          <div class="p-4">
            <span class="text-[10px] font-mono font-bold text-amber-800">{{ rel.sku }}</span>
            <h4 class="font-heading font-bold text-sm text-stone-900 truncate hover:text-rose-800">
              <a href="/product/{{ rel.sku }}">{{ rel.name }}</a>
            </h4>
            <div class="mt-2 flex items-center justify-between">
              <span class="font-heading font-black text-sm text-rose-800">{{ rel.price|format_vnd }}</span>
              <a href="/studio?sku={{ rel.sku }}" class="text-xs font-black text-stone-800 underline">Thử 3D</a>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
    {% endif %}

  </div>
</div>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'product_detail.html'), 'w', encoding='utf-8') as f:
    f.write(product_detail_html)
print('Updated templates/product_detail.html')

# 5. templates/inspirations.html
inspirations_html = '''{% extends "base.html" %}

{% block title %}Mẫu Tham Khảo Scrapbook DIY - Ý Tưởng Thủ Công Gen Z{% endblock %}

{% block content %}
{% import "components/carousel.html" as carousels %}

{% set inspiration_slides = [
  {
    "badge": "TUYỂN TẬP BỐ CỤC HOÀN CHỈNH",
    "title": "Mẫu Bố Cục Tinh Tuyển <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>100% SKU Có Sẵn</span>",
    "desc": "Tất cả các tác phẩm dưới đây được dựng từ kho Sticker (STK-001..012), Layout ảnh (LAY-001..008) và Sổ (SCR-001..004) chính hãng.",
    "buttons": [
      { "text": "Khám Phá Xưởng 3D", "url": "/studio", "primary": true },
      { "text": "Xem Kho Phụ Kiện", "url": "/products", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_001.svg",
    "corner_badge": "6 Bộ Mẫu Hoàn Chỉnh"
  },
  {
    "badge": "Ý TƯỞNG THEO TỪNG CHỦ ĐỀ",
    "title": "Từ Vintage Kỷ Yếu Đến <span class='text-rose-800'>Cyberpunk Y2K &amp; Couple</span>",
    "desc": "Dễ dàng chọn lựa bộ phối màu phù hợp theo từng sự kiện ý nghĩa, nhấn Remix để chỉnh sửa theo ảnh cá nhân của bạn.",
    "buttons": [
      { "text": "Trải Nghiệm Remix", "url": "/studio?remix=insp_001", "primary": true },
      { "text": "Đọc Cẩm Nang Layering", "url": "/guide", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_002.svg",
    "corner_badge": "Remix Tùy Ý"
  },
  {
    "badge": "TIẾT KIỆM KHI MUA THEO SET",
    "title": "Ưu Đãi Trọn Bộ Combo <span class='text-rose-800'>Tự Động Giảm Giá 15%</span>",
    "desc": "Đặt mua ngay toàn bộ linh kiện của từng mẫu tham khảo chỉ với một cú click, bảo toàn nguyên vẹn bố cục mẫu.",
    "buttons": [
      { "text": "Khám Phá Các Mẫu", "url": "#inspiration-list", "primary": true },
      { "text": "Xem Giỏ Hàng", "url": "/cart", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_004.svg",
    "corner_badge": "Combo Giảm 15%"
  }
] %}

{{ carousels.render_carousel("inspiration-carousel", inspiration_slides) }}

<!-- Inspiration List -->
<section id="inspiration-list" class="py-12 md:py-16 bg-[#fdfbf7]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
    
    {% for insp in inspirations %}
    <div class="bg-white border-3 border-black rounded-3xl p-6 sm:p-8 shadow-neo-xl grid grid-cols-1 lg:grid-cols-12 gap-8 items-center hover:border-rose-700 transition-all">
      
      <!-- Visual Display Box (Mockup) -->
      <div class="lg:col-span-6 relative">
        <div class="w-full aspect-[4/3] bg-stone-100 rounded-2xl overflow-hidden border-2 border-black relative group shadow-sm">
          <img src="{{ insp.image }}" alt="{{ insp.title }}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
          <span class="absolute top-3 left-3 bg-amber-300 text-black text-xs font-black px-3 py-1 rounded-md border border-black shadow-sm">
            {{ insp.theme }}
          </span>
          <span class="absolute bottom-3 right-3 bg-black/80 text-white text-xs font-bold px-2.5 py-1 rounded-md">
            Độ khó: {{ insp.difficulty }}
          </span>
        </div>
      </div>

      <!-- Inspiration Details & Strict Components SKU Checklist -->
      <div class="lg:col-span-6 space-y-4">
        <div>
          <div class="flex items-center justify-between gap-2">
            <span class="text-xs font-mono font-black text-rose-800 uppercase tracking-wider">Mã Dự Án: {{ insp.id|upper }}</span>
            <span class="text-xs font-bold text-amber-800 bg-amber-100 px-2 py-0.5 rounded">Tone: {{ insp.color_palette|join(', ') }}</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-heading font-black text-stone-900 mt-1 leading-tight">
            {{ insp.title }}
          </h2>
          <p class="text-xs text-stone-500 font-semibold mt-0.5">{{ insp.subtitle }}</p>
        </div>

        <p class="text-xs sm:text-sm text-stone-600 leading-relaxed">
          {{ insp.description }}
        </p>

        <!-- Components Breakdown with Exact SKUs -->
        <div class="bg-stone-50 border-2 border-black rounded-2xl p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-heading font-black text-stone-900 uppercase">Linh Kiện Cấu Thành (Chuẩn SKU):</span>
            <span class="text-[11px] font-bold text-rose-800">{{ insp.components|length }} Phụ Kiện</span>
          </div>
          
          <div class="flex flex-wrap gap-2 pt-1">
            {% for comp in insp.components %}
            <a href="/product/{{ comp.sku }}" class="inline-flex items-center gap-1.5 bg-white border border-stone-300 px-2.5 py-1 rounded-lg hover:border-black transition-colors" title="{{ comp.name }}">
              <span class="text-[10px] font-mono font-black text-rose-800">{{ comp.sku }}</span>
              <span class="text-[10px] font-bold text-stone-700 truncate max-w-[120px]">{{ comp.name }}</span>
            </a>
            {% endfor %}
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-3 pt-2">
          <a href="/studio?remix={{ insp.id }}" class="flex-1 bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-xs sm:text-sm py-3.5 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all text-center flex items-center justify-center gap-2">
            <span>Dùng Mẫu Trong Xưởng (Remix)</span>
            <span class="font-mono">→</span>
          </a>

          <button onclick="buyInspirationBundle('{{ insp.id }}', {{ insp.bundle_price }})" class="flex-1 bg-amber-300 hover:bg-amber-400 text-stone-950 font-heading font-black text-xs sm:text-sm py-3.5 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all text-center">
            Mua Trọn Bộ ({{ insp.bundle_price|format_vnd }})
          </button>
        </div>

      </div>

    </div>
    {% endfor %}

  </div>
</section>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'inspirations.html'), 'w', encoding='utf-8') as f:
    f.write(inspirations_html)
print('Updated templates/inspirations.html')

# 6. templates/handbook.html
handbook_html = '''{% extends "base.html" %}

{% block title %}Cẩm Nang Scrapbook & Nghệ Thuật Thủ Công Giấy Chuẩn SEO - ScrapCraft Studio{% endblock %}

{% block content %}
{% import "components/carousel.html" as carousels %}

{% set handbook_slides = [
  {
    "badge": "CẨM NANG THỦ CÔNG & SEO BLOG",
    "title": "Bí Quyết Sáng Tạo <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>Scrapbook Chuẩn Gu Gen Z</span>",
    "desc": "Tổng hợp các bài viết hướng dẫn kỹ thuật layering dán sổ, cách bảo quản ảnh lưu niệm và nghệ thuật phối sticker 3D độc đáo.",
    "buttons": [
      { "text": "Đọc Bài Viết Mới", "url": "#handbook-list", "primary": true },
      { "text": "Thử Nghiệm Trong Xưởng", "url": "/studio", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_005.svg",
    "corner_badge": "Kiến Thức Thủ Công"
  },
  {
    "badge": "KỸ THUẬT LAYERING 3 TẦNG",
    "title": "Nghệ Thuật Xếp Lớp <span class='text-rose-800'>Tạo Chiều Sâu Đa Tầng</span>",
    "desc": "Phân chia không gian Background - Midground - Foreground giúp trang sổ có chiều sâu thị giác như một tác phẩm mỹ thuật.",
    "buttons": [
      { "text": "Xem Hướng Dẫn Chi Tiết", "url": "/guide/huong-dan-layering-sticker-3d-chieu-sau-scrapbook", "primary": true },
      { "text": "Xem Layout Phù Hợp", "url": "/products?category=layout", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_002.svg",
    "corner_badge": "Kỹ Thuật Chuyên Sâu"
  },
  {
    "badge": "BẢO QUẢN KỶ NIỆM BỀN LÂU",
    "title": "Lựa Chọn Giấy Acid-Free & <span class='text-rose-800'>Khung Cài Bảo Tàng</span>",
    "desc": "Bảo vệ những bức ảnh polaroid quý giá không bị ố vàng hay phai màu sau hàng chục năm lưu giữ.",
    "buttons": [
      { "text": "Đọc Bài Viết Bảo Quản", "url": "/guide/bao-quan-anh-polaroid-scrapbook-khong-o-vang", "primary": true },
      { "text": "Xem Các Mẫu Sổ FSC", "url": "/products?category=scrapbook", "primary": false }
    ],
    "image": "/static/assets/books/scr_001.svg",
    "corner_badge": "Chuẩn Bảo Quản"
  }
] %}

{{ carousels.render_carousel("handbook-carousel", handbook_slides) }}

<!-- Tag Filter -->
<section class="bg-white py-6 border-b-2 border-black">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap gap-2">
    <a href="/guide" class="text-xs font-black px-4 py-2 rounded-xl border-2 border-black transition-all {% if selected_tag == 'all' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">Tất cả bài viết</a>
    <a href="/guide?tag=scrapbook-la-gi" class="text-xs font-black px-4 py-2 rounded-xl border-2 border-black transition-all {% if selected_tag == 'scrapbook-la-gi' or selected_tag == 'Scrapbook' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">#Scrapbook Là Gì</a>
    <a href="/guide?tag=layering" class="text-xs font-black px-4 py-2 rounded-xl border-2 border-black transition-all {% if selected_tag == 'layering' or selected_tag == 'Layering' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">#Kỹ Thuật Layering</a>
    <a href="/guide?tag=sticker-3d" class="text-xs font-black px-4 py-2 rounded-xl border-2 border-black transition-all {% if selected_tag == 'sticker-3d' or selected_tag == 'Sticker 3D' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">#Sticker 3D</a>
    <a href="/guide?tag=polaroid" class="text-xs font-black px-4 py-2 rounded-xl border-2 border-black transition-all {% if selected_tag == 'polaroid' or selected_tag == 'Polaroid' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">#Khung Polaroid</a>
    <a href="/guide?tag=ai-studio" class="text-xs font-black px-4 py-2 rounded-xl border-2 border-black transition-all {% if selected_tag == 'ai-studio' or selected_tag == 'AI Studio' %}bg-rose-800 text-white shadow-neo{% else %}bg-white text-stone-800 hover:bg-stone-100{% endif %}">#AI Bố Cục</a>
  </div>
</section>

<!-- Blog List Grid -->
<section id="handbook-list" class="py-12 md:py-16 bg-[#fdfbf7]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      {% for blog in blogs %}
      <article class="bg-white border-2 border-black rounded-3xl overflow-hidden shadow-neo flex flex-col justify-between hover:border-rose-700 transition-all group">
        <div>
          <div class="w-full aspect-video bg-stone-100 relative overflow-hidden border-b-2 border-black">
            <img src="{{ blog.cover_image }}" alt="{{ blog.title }}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <span class="absolute top-3 left-3 bg-stone-900 text-white text-[10px] font-black px-2.5 py-0.5 rounded-md">
              {{ blog.category }}
            </span>
          </div>

          <div class="p-6 space-y-2">
            <div class="flex items-center gap-2 text-xs text-stone-400 font-bold">
              <span>{{ blog.published_date }}</span>
              <span>•</span>
              <span>{{ blog.read_time }}</span>
            </div>

            <h2 class="font-heading font-extrabold text-lg text-stone-900 leading-snug hover:text-rose-800 transition-colors">
              <a href="/guide/{{ blog.slug }}">{{ blog.title }}</a>
            </h2>

            <p class="text-xs text-stone-600 line-clamp-3 leading-relaxed">
              {{ blog.excerpt }}
            </p>

            <div class="flex flex-wrap gap-1 pt-2">
              {% for tag in blog.tags %}
              <span class="text-[10px] bg-amber-100 text-amber-900 font-bold px-2 py-0.5 rounded">#{{ tag }}</span>
              {% endfor %}
            </div>
          </div>
        </div>

        <div class="p-6 pt-0">
          <a href="/guide/{{ blog.slug }}" class="w-full block text-center bg-rose-50 hover:bg-rose-100 text-rose-900 font-bold text-xs py-2.5 rounded-xl border border-rose-200 transition-colors">
            Đọc Bài Hướng Dẫn →
          </a>
        </div>
      </article>
      {% endfor %}
    </div>

  </div>
</section>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'handbook.html'), 'w', encoding='utf-8') as f:
    f.write(handbook_html)
print('Updated templates/handbook.html')

# 7. templates/handbook_detail.html
handbook_detail_html = '''{% extends "base.html" %}

{% block title %}{{ blog.title }} - Cẩm Nang ScrapCraft Studio{% endblock %}

{% block content %}
<article class="py-12 bg-[#fdfbf7]">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <!-- Breadcrumbs -->
    <nav class="flex items-center gap-2 text-xs font-bold text-stone-500 mb-6">
      <a href="/" class="hover:text-rose-800">Trang chủ</a>
      <span>/</span>
      <a href="/guide" class="hover:text-rose-800">Cẩm nang</a>
      <span>/</span>
      <span class="text-stone-900">{{ blog.category }}</span>
    </nav>

    <!-- Post Header Card -->
    <div class="bg-white border-3 border-black rounded-3xl p-6 sm:p-10 shadow-neo-xl space-y-6">
      
      <div>
        <div class="flex items-center gap-2 text-xs font-bold text-amber-800 mb-3">
          <span class="bg-amber-300 text-stone-950 px-3 py-0.5 rounded-full border border-black font-black uppercase">{{ blog.category }}</span>
          <span>•</span>
          <span>{{ blog.published_date }}</span>
          <span>•</span>
          <span>{{ blog.read_time }}</span>
        </div>

        <h1 class="text-2xl sm:text-3xl lg:text-4xl font-heading font-black text-stone-900 leading-tight">
          {{ blog.title }}
        </h1>
        
        <p class="text-sm sm:text-base text-stone-600 font-medium mt-3 leading-relaxed">
          {{ blog.excerpt }}
        </p>
      </div>

      <!-- Hero Image -->
      <div class="w-full aspect-video bg-stone-100 rounded-2xl overflow-hidden border-2 border-black relative">
        <img src="{{ blog.cover_image }}" alt="{{ blog.title }}" class="w-full h-full object-cover">
      </div>

      <!-- Post Content Body -->
      <div class="prose prose-stone max-w-none text-stone-800 text-sm sm:text-base leading-relaxed space-y-4 pt-4 border-t border-stone-200">
        {{ blog.content | safe }}
      </div>

      <!-- Tags & Share -->
      <div class="border-t border-stone-200 pt-6 flex flex-wrap items-center justify-between gap-4">
        <div class="flex flex-wrap items-center gap-1.5">
          <span class="text-xs font-black text-stone-900 uppercase">Tags:</span>
          {% for tag in blog.tags %}
          <a href="/guide?tag={{ tag }}" class="text-xs bg-stone-100 hover:bg-rose-100 text-stone-800 hover:text-rose-800 px-3 py-1 rounded-lg border border-stone-300 transition-colors font-bold">
            #{{ tag }}
          </a>
          {% endfor %}
        </div>

        <a href="/studio" class="bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-xs px-5 py-2.5 rounded-xl border border-black shadow-sm transition-all flex items-center gap-2">
          <span>Thử Nghiệm Trong Xưởng</span>
          <span class="font-mono">→</span>
        </a>
      </div>

    </div>

    <!-- Related Products Box -->
    {% if related_products %}
    <div class="mt-12 bg-amber-50 border-2 border-black rounded-3xl p-6 shadow-neo">
      <h3 class="font-heading font-black text-lg text-stone-900 mb-4">Linh Kiện Gợi Ý Sử Dụng Trong Bài Viết Này:</h3>
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
        {% for rel in related_products %}
        <div class="bg-white border border-black rounded-2xl p-4 flex items-center gap-3">
          <img src="{{ rel.image }}" alt="{{ rel.name }}" class="w-12 h-12 object-contain flex-shrink-0">
          <div class="overflow-hidden">
            <span class="text-[10px] font-mono font-black text-rose-800">{{ rel.sku }}</span>
            <h4 class="font-bold text-xs text-stone-900 truncate">{{ rel.name }}</h4>
            <span class="text-xs font-black text-stone-800">{{ rel.price|format_vnd }}</span>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
    {% endif %}

  </div>
</article>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'handbook_detail.html'), 'w', encoding='utf-8') as f:
    f.write(handbook_detail_html)
print('Updated templates/handbook_detail.html')

# 8. templates/contact.html
contact_html = '''{% extends "base.html" %}

{% block title %}Liên Hệ &amp; Chính Sách Bảo Mật Chi Tiết - ScrapCraft Studio{% endblock %}

{% block content %}
{% import "components/carousel.html" as carousels %}

{% set contact_slides = [
  {
    "badge": "KẾT NỐI VỚI XƯỞNG THỦ CÔNG",
    "title": "Showroom &amp; Xưởng Thủ Công <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>ScrapCraft Studio</span>",
    "desc": "Không gian trải nghiệm chạm thử chất liệu giấy mỹ thuật, sticker dập nổi 3D và tư vấn gia công sổ kỷ yếu theo yêu cầu.",
    "buttons": [
      { "text": "Gửi Lời Nhắn Cho Xưởng", "url": "#contact-box", "primary": true },
      { "text": "Vào Xưởng 3D", "url": "/studio", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_006.svg",
    "corner_badge": "Showroom TP.HCM"
  },
  {
    "badge": "HỖ TRỢ THIẾT KẾ & DOANH NGHIỆP",
    "title": "Nhận Gia Công Sổ Kỷ Yếu & <span class='text-rose-800'>Set Quà Tặng Doanh Nghiệp</span>",
    "desc": "Tùy biến bìa dập chìm logo, phối màu theo brand guideline với định dạng file thiết kế chuẩn in ấn offset.",
    "buttons": [
      { "text": "Liên Hệ Báo Giá", "url": "#contact-box", "primary": true },
      { "text": "Xem Mẫu Tham Khảo", "url": "/inspiration", "primary": false }
    ],
    "image": "/static/assets/books/scr_004.svg",
    "corner_badge": "In Ấn Theo Yêu Cầu"
  },
  {
    "badge": "CAM KẾT MINH BẠCH & BẢO MẬT",
    "title": "Chính Sách Bảo Mật 100% & <span class='text-rose-800'>Bảo Hành 1-Đổi-1 Trong 7 Ngày</span>",
    "desc": "Mọi cam kết về bảo mật hình ảnh cá nhân, quyền sở hữu thiết kế và quyền lợi khách hàng đều được công khai minh bạch.",
    "buttons": [
      { "text": "Xem Chi Tiết Chính Sách", "url": "#policies-section", "primary": true },
      { "text": "Tra Cứu Đơn Hàng", "url": "/order-tracking", "primary": false }
    ],
    "image": "/static/assets/layouts/insp_001.svg",
    "corner_badge": "Bảo Mật Tuyệt Đối"
  }
] %}

{{ carousels.render_carousel("contact-carousel", contact_slides) }}

<!-- Content Grid -->
<div id="contact-box" class="py-12 md:py-16 bg-[#fdfbf7]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
    
    <!-- Top Row: Contact Info & Membership Form -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
      
      <!-- Company Information Card -->
      <div class="lg:col-span-5 bg-white border-3 border-black rounded-3xl p-6 sm:p-8 shadow-neo-xl space-y-6">
        <div>
          <span class="bg-amber-300 text-stone-900 text-xs font-black px-3 py-1 rounded-full border border-black inline-block mb-2">Showroom &amp; Xưởng Thủ Công</span>
          <h2 class="text-2xl font-heading font-black text-stone-900">{{ company.brand_name }}</h2>
          <p class="text-xs text-stone-500 font-semibold mt-1">{{ company.tagline }}</p>
        </div>

        <div class="space-y-3 text-xs sm:text-sm text-stone-700">
          <p class="flex items-start gap-2.5">
            <span class="font-mono font-bold text-rose-800 flex-shrink-0">✦</span>
            <span><b>Địa chỉ:</b> {{ company.contact.address }}</span>
          </p>
          <p class="flex items-center gap-2.5">
            <span class="font-mono font-bold text-rose-800 flex-shrink-0">✦</span>
            <span><b>Hotline Zalo:</b> <span class="text-rose-800 font-black">{{ company.contact.hotline }}</span></span>
          </p>
          <p class="flex items-center gap-2.5">
            <span class="font-mono font-bold text-rose-800 flex-shrink-0">✦</span>
            <span><b>Email:</b> <span class="text-rose-800 font-bold">{{ company.contact.email }}</span></span>
          </p>
          <p class="flex items-center gap-2.5">
            <span class="font-mono font-bold text-rose-800 flex-shrink-0">✦</span>
            <span><b>Giờ làm việc:</b> {{ company.contact.working_hours }}</span>
          </p>
        </div>

        <div class="pt-4 border-t border-stone-200">
          <span class="text-xs font-black text-stone-900 uppercase block mb-3">Kênh Mạng Xã Hội Chính Thức:</span>
          <div class="grid grid-cols-2 gap-2">
            <a href="{{ company.contact.socials.tiktok }}" target="_blank" class="bg-stone-100 hover:bg-rose-100 text-stone-900 text-xs font-bold p-2.5 rounded-xl border border-stone-300 flex items-center justify-center gap-2 transition-colors">
              <span>TikTok</span>
            </a>
            <a href="{{ company.contact.socials.instagram }}" target="_blank" class="bg-stone-100 hover:bg-rose-100 text-stone-900 text-xs font-bold p-2.5 rounded-xl border border-stone-300 flex items-center justify-center gap-2 transition-colors">
              <span>Instagram</span>
            </a>
            <a href="{{ company.contact.socials.facebook }}" target="_blank" class="bg-stone-100 hover:bg-rose-100 text-stone-900 text-xs font-bold p-2.5 rounded-xl border border-stone-300 flex items-center justify-center gap-2 transition-colors">
              <span>Facebook</span>
            </a>
            <a href="{{ company.contact.socials.shopee }}" target="_blank" class="bg-stone-100 hover:bg-rose-100 text-stone-900 text-xs font-bold p-2.5 rounded-xl border border-stone-300 flex items-center justify-center gap-2 transition-colors">
              <span>Shopee</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Contact Message Form -->
      <div class="lg:col-span-7 bg-white border-3 border-black rounded-3xl p-6 sm:p-8 shadow-neo-xl">
        <div class="mb-6">
          <div class="inline-flex items-center gap-2 bg-rose-100 text-rose-800 px-3 py-1 rounded-full text-xs font-black uppercase mb-2">
            <span>Hộp Thư Tiếp Nhận Yêu Cầu</span>
          </div>
          <h3 class="text-2xl font-heading font-black text-stone-900">Gửi Lời Nhắn Cho ScrapCraft Studio</h3>
          <p class="text-xs text-stone-500 font-medium mt-1">Đội ngũ nghệ nhân sẽ phản hồi qua Zalo/Email trong vòng 2 giờ làm việc.</p>
        </div>

        <form id="contact-form" class="space-y-4">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-black text-stone-800 uppercase mb-1">Họ &amp; Tên *</label>
              <input type="text" name="name" required placeholder="Nguyễn Văn A" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800">
            </div>
            <div>
              <label class="block text-xs font-black text-stone-800 uppercase mb-1">Số điện thoại / Zalo *</label>
              <input type="tel" name="phone" required placeholder="0988 xxx xxx" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800">
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs font-black text-stone-800 uppercase mb-1">Email</label>
              <input type="email" name="email" placeholder="email@gmail.com" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800">
            </div>
            <div>
              <label class="block text-xs font-black text-stone-800 uppercase mb-1">Chủ đề cần tư vấn</label>
              <select name="subject" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800">
                <option value="custom_order">Đặt làm sổ thiết kế riêng</option>
                <option value="bulk_order">Đặt in số lượng lớn / Lớp học</option>
                <option value="product_qa">Tư vấn phụ kiện &amp; Kỹ thuật</option>
                <option value="cooperation">Hợp tác thương hiệu / Workshop</option>
              </select>
            </div>
          </div>

          <div>
            <label class="block text-xs font-black text-stone-800 uppercase mb-1">Nội dung chi tiết</label>
            <textarea name="message" rows="4" placeholder="Mô tả ý tưởng cuốn sổ, số lượng trang dự kiến, dịp kỷ niệm..." class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800"></textarea>
          </div>

          <button type="submit" class="w-full bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-sm py-3.5 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all">
            Gửi Thông Tin Ngay →
          </button>
        </form>
      </div>

    </div>

    <!-- Bottom Row: Detailed Policies (4 Pillars) -->
    <div id="policies-section" class="space-y-8 pt-6">
      <div class="text-center max-w-2xl mx-auto">
        <div class="inline-flex items-center gap-2 bg-amber-300 border-2 border-black px-3.5 py-1 rounded-full text-xs font-black uppercase mb-2 shadow-neo">
          <span>✦ CAM KẾT MINH BẠCH</span>
        </div>
        <h2 class="text-3xl font-heading font-black text-stone-900">
          Chính Sách Khách Hàng &amp; Bảo Mật Toàn Diện
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        
        <!-- Policy 1: Privacy -->
        <div class="bg-white border-2 border-black rounded-3xl p-6 shadow-neo space-y-3">
          <div class="flex items-center gap-3">
            <span class="font-mono font-black text-rose-800 text-lg">01.</span>
            <h3 class="font-heading font-bold text-lg text-stone-900">{{ company.policies.privacy.title }}</h3>
          </div>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed">
            {{ company.policies.privacy.detail }}
          </p>
        </div>

        <!-- Policy 2: Copyright -->
        <div class="bg-white border-2 border-black rounded-3xl p-6 shadow-neo space-y-3">
          <div class="flex items-center gap-3">
            <span class="font-mono font-black text-amber-600 text-lg">02.</span>
            <h3 class="font-heading font-bold text-lg text-stone-900">{{ company.policies.copyright.title }}</h3>
          </div>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed">
            {{ company.policies.copyright.detail }}
          </p>
        </div>

        <!-- Policy 3: Shipping -->
        <div class="bg-white border-2 border-black rounded-3xl p-6 shadow-neo space-y-3">
          <div class="flex items-center gap-3">
            <span class="font-mono font-black text-stone-900 text-lg">03.</span>
            <h3 class="font-heading font-bold text-lg text-stone-900">{{ company.policies.shipping.title }}</h3>
          </div>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed">
            {{ company.policies.shipping.detail }}
          </p>
        </div>

        <!-- Policy 4: Warranty -->
        <div class="bg-white border-2 border-black rounded-3xl p-6 shadow-neo space-y-3">
          <div class="flex items-center gap-3">
            <span class="font-mono font-black text-rose-800 text-lg">04.</span>
            <h3 class="font-heading font-bold text-lg text-stone-900">{{ company.policies.warranty.title }}</h3>
          </div>
          <p class="text-xs sm:text-sm text-stone-600 leading-relaxed">
            {{ company.policies.warranty.detail }}
          </p>
        </div>

      </div>
    </div>

  </div>
</div>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'contact.html'), 'w', encoding='utf-8') as f:
    f.write(contact_html)
print('Updated templates/contact.html')

# 9. templates/studio.html
studio_html = '''{% extends "base.html" %}

{% block title %}Xưởng Thiết Kế Scrapbook 2D/3D & Trợ Lý AI - ScrapCraft Studio{% endblock %}

{% block extra_head %}
<script>
  // Server-side preset data if user came from "Remix" button
  window.STUDIO_PRESET_DATA = {% if active_preset %}{{ active_preset.canvas_preset | tojson }}{% else %}null{% endif %};
  window.STUDIO_ACTIVE_PRODUCT = {% if active_product %}{{ active_product | tojson }}{% else %}null{% endif %};
</script>
{% endblock %}

{% block content %}
<!-- Studio Top Bar -->
<section class="bg-stone-900 text-white py-4 px-4 sm:px-6 lg:px-8 border-b-2 border-black sticky top-20 z-30 shadow-md">
  <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-4">
    
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 bg-amber-400 text-stone-950 font-black text-xl rounded-xl border border-black flex items-center justify-center shadow-neo">
        ✦
      </div>
      <div>
        <h1 class="font-heading font-black text-base sm:text-lg text-white leading-tight flex items-center gap-2">
          <span>Xưởng Thiết Kế ScrapCraft</span>
          <span class="bg-rose-800 text-white text-[10px] font-mono font-bold px-2 py-0.5 rounded-full border border-rose-600">AI + 3D WebGL</span>
        </h1>
        <p class="text-[11px] text-stone-400 font-medium">Kéo thả phụ kiện chính hãng • Mô phỏng 3D thời gian thực</p>
      </div>
    </div>

    <!-- Mode Switcher Tabs (2D Canvas vs 3D 360° Viewer) -->
    <div class="flex items-center gap-2 bg-stone-950 p-1 rounded-2xl border border-stone-800">
      <button id="tab-btn-2d" onclick="switchStudioView('2d')" class="px-5 py-2 rounded-xl font-heading font-black text-xs border-2 border-black bg-rose-800 text-white shadow-neo transition-all">
        Thiết Kế 2D
      </button>
      <button id="tab-btn-3d" onclick="switchStudioView('3d')" class="px-5 py-2 rounded-xl font-heading font-black text-xs border-2 border-black bg-white text-stone-900 hover:bg-amber-100 transition-all flex items-center gap-1.5">
        <span>Xem 3D 360°</span>
        <span class="bg-amber-300 text-stone-950 text-[9px] px-1 py-0.2 rounded font-black">WebGL</span>
      </button>
    </div>

    <!-- Action Toolbar (Export & Add to Cart) -->
    <div class="flex items-center gap-2">
      <button onclick="exportCanvasImage()" class="bg-stone-800 hover:bg-stone-700 text-white text-xs font-bold px-3.5 py-2 rounded-xl border border-stone-700 flex items-center gap-1.5 transition-colors">
        <span>Xuất Ảnh HD</span>
      </button>
      <button onclick="addDesignComponentsToCart()" class="bg-amber-300 hover:bg-amber-400 text-stone-950 text-xs font-heading font-black px-4 py-2 rounded-xl border-2 border-black shadow-neo transition-all flex items-center gap-1.5">
        <span>Mua Trọn Bộ Linh Kiện</span>
      </button>
    </div>

  </div>
</section>

<!-- Studio Workspace Container -->
<div class="bg-[#f4efe6] py-6 sm:py-8 min-h-[calc(100vh-160px)]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
      
      <!-- ================= LEFT COLUMN: COMPONENTS TABS & AI ASSISTANT ================= -->
      <div class="lg:col-span-4 space-y-4">
        
        <!-- AI SMART ASSISTANT PANEL -->
        <div class="bg-gradient-to-br from-stone-900 to-rose-950 text-white border-3 border-amber-400 rounded-3xl p-5 shadow-neo-lg relative overflow-hidden">
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
              <span class="text-amber-400 font-mono font-bold text-base">✦</span>
              <h3 class="font-heading font-black text-sm text-amber-300">Trợ Lý AI Gợi Ý Bố Cục</h3>
            </div>
            <span class="text-[10px] bg-rose-800 text-white px-2 py-0.5 rounded-full font-bold">Auto Arranger</span>
          </div>

          <p class="text-xs text-stone-300 leading-relaxed mb-3">
            Nhập chủ đề bạn muốn làm, AI sẽ phân tích ngữ cảnh và chọn mã <b>STK-xxx &amp; LAY-xxx</b> chuẩn kho để dàn trang cho bạn:
          </p>

          <div class="space-y-2">
            <div class="relative">
              <input type="text" id="ai-prompt-input" placeholder="VD: Kỷ niệm bạn thân đi đà lạt vintage..." class="w-full bg-stone-800 border-2 border-stone-700 rounded-xl px-3.5 py-2.5 text-xs text-white placeholder-stone-400 font-medium focus:outline-none focus:border-amber-400">
              <button id="btn-ai-generate" onclick="requestAiLayoutSuggestion()" class="absolute right-1.5 top-1.5 bg-amber-400 hover:bg-amber-300 text-stone-950 font-black text-xs px-3 py-1.5 rounded-lg transition-colors">
                Gợi Ý AI
              </button>
            </div>

            <!-- Quick Preset Chips -->
            <div class="flex flex-wrap gap-1.5 pt-1">
              <button onclick="setAiPrompt('kỷ yếu bạn thân phong cách y2k')" class="text-[10px] bg-stone-800 hover:bg-rose-800 text-stone-300 hover:text-white px-2 py-0.5 rounded-md border border-stone-700 transition-colors">
                #Y2K Kỷ Yếu
              </button>
              <button onclick="setAiPrompt('kỷ niệm ngày yêu nhau lãng mạn')" class="text-[10px] bg-stone-800 hover:bg-rose-800 text-stone-300 hover:text-white px-2 py-0.5 rounded-md border border-stone-700 transition-colors">
                #Couple Tình Yêu
              </button>
              <button onclick="setAiPrompt('chuyến đi đà lạt hoài niệm vintage')" class="text-[10px] bg-stone-800 hover:bg-rose-800 text-stone-300 hover:text-white px-2 py-0.5 rounded-md border border-stone-700 transition-colors">
                #Vintage Đà Lạt
              </button>
            </div>
          </div>

          <!-- AI Loading Spinner -->
          <div id="ai-loading" class="hidden mt-3 text-center py-2 bg-stone-800/80 rounded-xl border border-amber-400/50">
            <span class="text-xs font-bold text-amber-300 animate-pulse">✦ AI đang phân tích kho linh kiện và bố trí layout...</span>
          </div>
        </div>

        <!-- UPLOAD PHOTO TOOL -->
        <div class="bg-white border-2 border-black rounded-3xl p-4 shadow-neo">
          <label class="block text-xs font-heading font-black text-stone-900 uppercase mb-2">
            Tải Ảnh Cá Nhân Vào Trang Sổ:
          </label>
          <div class="relative border-2 border-dashed border-stone-300 hover:border-rose-800 rounded-2xl p-4 text-center bg-stone-50 cursor-pointer transition-colors" onclick="document.getElementById('user-photo-upload').click()">
            <input type="file" id="user-photo-upload" accept="image/*" class="hidden" onchange="handleUserPhotoUpload(event)">
            <p class="text-xs font-bold text-stone-700">Nhấn để tải ảnh (JPG, PNG)</p>
            <p class="text-[10px] text-stone-400 mt-0.5">Tự động đặt vào khung ảnh hoặc kéo thả tự do</p>
          </div>
        </div>

        <!-- COMPONENT CATALOG ACCORDION (STICKER / LAYOUT / BOOK) -->
        <div class="bg-white border-2 border-black rounded-3xl p-4 shadow-neo space-y-4">
          <div class="flex items-center justify-between pb-2 border-b border-stone-200">
            <span class="font-heading font-black text-xs text-stone-900 uppercase">Kho Phụ Kiện Chuẩn SKU</span>
            <span class="text-[10px] bg-rose-100 text-rose-800 font-bold px-2 py-0.5 rounded">24 Mã Khả Dụng</span>
          </div>

          <!-- Component Tabs -->
          <div class="flex gap-1 bg-stone-100 p-1 rounded-xl">
            <button onclick="switchCatalogTab('stickers')" id="tab-stk-btn" class="flex-1 py-1.5 rounded-lg text-xs font-black bg-white text-stone-900 border border-black shadow-sm transition-all">
              Sticker (12)
            </button>
            <button onclick="switchCatalogTab('layouts')" id="tab-lay-btn" class="flex-1 py-1.5 rounded-lg text-xs font-bold text-stone-600 hover:bg-white transition-all">
              Layout (8)
            </button>
            <button onclick="switchCatalogTab('books')" id="tab-book-btn" class="flex-1 py-1.5 rounded-lg text-xs font-bold text-stone-600 hover:bg-white transition-all">
              Bìa Sổ (4)
            </button>
          </div>

          {% set sticker_items = stickers if stickers else (products | selectattr('category', 'equalto', 'sticker') | list) %}
          {% set layout_items = layouts if layouts else (products | selectattr('category', 'equalto', 'layout') | list) %}
          {% set book_items = books if books else (products | selectattr('category', 'in', ['scrapbook', 'book']) | list) %}

          <!-- Catalog 1: Stickers (STK-001..STK-012) -->
          <div id="catalog-stickers" class="grid grid-cols-3 gap-2.5 max-h-[360px] overflow-y-auto pr-1">
            {% for stk in sticker_items %}
            <div onclick="addStickerToCanvas('{{ stk.sku }}', '{{ stk.name }}', '{{ stk.image }}', {{ stk.price }})" class="bg-stone-50 hover:bg-amber-50 border border-stone-200 hover:border-black rounded-2xl p-2 cursor-pointer transition-all flex flex-col items-center justify-between text-center group shadow-sm hover:shadow-md">
              <div class="w-14 h-14 bg-white rounded-xl p-1 flex items-center justify-center border border-stone-100 mb-1">
                <img src="{{ stk.image }}" alt="{{ stk.name }}" class="w-full h-full object-contain group-hover:scale-110 transition-transform">
              </div>
              <span class="text-[9px] font-mono font-black text-rose-800 block">{{ stk.sku }}</span>
              <span class="text-[10px] font-bold text-stone-700 leading-tight line-clamp-2 w-full mt-0.5">{{ stk.name }}</span>
            </div>
            {% endfor %}
          </div>

          <!-- Catalog 2: Layouts (LAY-001..LAY-008) -->
          <div id="catalog-layouts" class="hidden grid grid-cols-2 gap-2.5 max-h-[360px] overflow-y-auto pr-1">
            {% for lay in layout_items %}
            <div onclick="addLayoutToCanvas('{{ lay.sku }}', '{{ lay.name }}', '{{ lay.image }}', {{ lay.price }})" class="bg-stone-50 hover:bg-amber-50 border border-stone-200 hover:border-black rounded-2xl p-2.5 cursor-pointer transition-all flex flex-col items-center justify-between text-center group shadow-sm hover:shadow-md">
              <div class="w-20 h-20 bg-white rounded-xl p-1 flex items-center justify-center border border-stone-100 mb-1">
                <img src="{{ lay.image }}" alt="{{ lay.name }}" class="w-full h-full object-contain group-hover:scale-105 transition-transform">
              </div>
              <span class="text-[9px] font-mono font-black text-amber-800 block">{{ lay.sku }}</span>
              <span class="text-[10px] font-bold text-stone-700 leading-tight line-clamp-2 w-full mt-0.5">{{ lay.name }}</span>
            </div>
            {% endfor %}
          </div>

          <!-- Catalog 3: Books (SCR-001..SCR-004) -->
          <div id="catalog-books" class="hidden grid grid-cols-2 gap-2.5 max-h-[360px] overflow-y-auto pr-1">
            {% for book in book_items %}
            <div onclick="setScrapbookCover('{{ book.sku }}', '{{ book.name }}', '{{ book.image }}', {{ book.price }}, '{{ (book.attributes and book.attributes.color) or (book.specs and book.specs.color) or \'#d97706\' }}')" class="bg-stone-50 hover:bg-amber-50 border border-stone-200 hover:border-black rounded-2xl p-2.5 cursor-pointer transition-all flex flex-col items-center justify-between text-center group shadow-sm hover:shadow-md">
              <div class="w-20 h-20 bg-white rounded-xl p-1 flex items-center justify-center border border-stone-100 mb-1">
                <img src="{{ book.image }}" alt="{{ book.name }}" class="w-full h-full object-contain group-hover:scale-105 transition-transform">
              </div>
              <span class="text-[9px] font-mono font-black text-stone-900 block">{{ book.sku }}</span>
              <span class="text-[10px] font-bold text-stone-700 leading-tight line-clamp-2 w-full mt-0.5">{{ book.name }}</span>
            </div>
            {% endfor %}
          </div>

        </div>

      </div>

      <!-- ================= CENTER/RIGHT COLUMN: WORKSPACE CANVASES ================= -->
      <div class="lg:col-span-8 space-y-4">
        
        <!-- 2D FABRIC CANVAS VIEW -->
        <div id="studio-2d-panel" class="bg-white border-3 border-black rounded-3xl p-4 sm:p-6 shadow-neo-xl">
          <div class="flex items-center justify-between mb-4 flex-wrap gap-2">
            <div class="flex items-center gap-2">
              <span class="text-xs font-heading font-black text-stone-900 uppercase">Trang Sổ 2D (600x600 px)</span>
              <span class="text-[10px] bg-stone-100 text-stone-600 px-2 py-0.5 rounded font-mono">Tự động đồng bộ 3D</span>
            </div>

            <!-- Canvas Quick Actions -->
            <div class="flex items-center gap-1.5 flex-wrap">
              <button onclick="addTextToCanvas()" class="text-xs bg-stone-100 hover:bg-amber-300 font-bold px-3 py-1.5 rounded-lg border border-black transition-colors" title="Thêm chữ viết tay">
                + Chữ Viết Tay
              </button>
              <button onclick="deleteSelectedObject()" class="text-xs bg-stone-100 hover:bg-rose-200 font-bold px-3 py-1.5 rounded-lg border border-black transition-colors" title="Xóa phần tử đang chọn">
                Xóa Chọn
              </button>
              <button onclick="clearCanvas()" class="text-xs bg-stone-100 hover:bg-stone-200 font-bold px-3 py-1.5 rounded-lg border border-black transition-colors" title="Làm mới trang trắng">
                Trang Trắng
              </button>
            </div>
          </div>

          <!-- Canvas Interactive Workspace -->
          <div class="w-full flex justify-center items-center bg-[#eae3d2] rounded-2xl p-4 sm:p-6 border-2 border-stone-300 shadow-inner overflow-hidden">
            <div class="relative bg-[#fdfbf7] shadow-2xl rounded border border-stone-400">
              <canvas id="scrapbook-fabric-canvas" width="600" height="600"></canvas>
            </div>
          </div>
        </div>

        <!-- 3D THREE.JS 360° VIEWER -->
        <div id="studio-3d-panel" class="hidden bg-stone-950 border-3 border-amber-400 rounded-3xl p-4 sm:p-6 shadow-neo-xl text-white">
          <div class="flex items-center justify-between mb-4 flex-wrap gap-2">
            <div class="flex items-center gap-2">
              <span class="font-mono font-bold text-amber-400">✦</span>
              <h3 class="font-heading font-black text-sm text-white uppercase">Mô Phỏng 3D Scrapbook 360° Chân Thực</h3>
              <span class="text-[10px] bg-rose-800 text-white px-2 py-0.5 rounded-full font-bold">Chất Liệu Giấy Mộc &amp; Nổi Khối 3D</span>
            </div>

            <!-- 3D Controls Bar -->
            <div class="flex items-center gap-1.5">
              <button id="btn-toggle-rotate" onclick="toggle3DAutoRotate()" class="text-xs bg-stone-800 hover:bg-stone-700 text-amber-300 font-bold px-3 py-1.5 rounded-lg border border-stone-700">
                Dừng xoay
              </button>
              <button onclick="set3DViewAngle('front')" class="text-xs bg-stone-800 hover:bg-stone-700 text-white font-bold px-2.5 py-1.5 rounded-lg border border-stone-700">
                Góc Thẳng
              </button>
              <button onclick="set3DViewAngle('iso')" class="text-xs bg-stone-800 hover:bg-stone-700 text-white font-bold px-2.5 py-1.5 rounded-lg border border-stone-700">
                Góc Nghiêng
              </button>
              <button onclick="set3DViewAngle('top')" class="text-xs bg-stone-800 hover:bg-stone-700 text-white font-bold px-2.5 py-1.5 rounded-lg border border-stone-700">
                Từ Trên Xuống
              </button>
            </div>
          </div>

          <!-- WebGL Three.js Container -->
          <div id="threejs-container" class="w-full h-[520px] rounded-2xl bg-gradient-to-b from-[#fdfbf7] to-[#e8d8c3] border border-stone-700 overflow-hidden relative">
            <div class="absolute bottom-4 left-4 bg-stone-900/80 backdrop-blur text-stone-300 text-xs px-3 py-1.5 rounded-xl border border-stone-700 pointer-events-none font-bold">
              Kéo chuột để xoay 360° • Cuộn chuột để phóng to/thu nhỏ
            </div>
          </div>
        </div>

        <!-- USED COMPONENTS SKU SUMMARY & COST BREAKDOWN -->
        <div class="bg-white border-2 border-black rounded-3xl p-5 shadow-neo">
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center gap-2">
              <span class="font-heading font-black text-xs text-stone-900 uppercase">Danh Mục Linh Kiện Đang Sử Dụng:</span>
              <span id="used-skus-count" class="text-xs font-mono font-bold bg-amber-300 text-stone-950 px-2 py-0.5 rounded">0 linh kiện</span>
            </div>
            <div class="text-xs font-bold text-stone-600">
              Tổng giá trị set: <span id="design-total-price" class="font-heading font-black text-base text-rose-800">0 đ</span>
            </div>
          </div>

          <!-- Dynamic Used SKU List Container -->
          <div id="used-components-list" class="flex flex-wrap gap-2 min-h-[36px] items-center text-xs text-stone-400">
            <span>Chưa có phụ kiện nào được thêm vào trang sổ. Hãy chọn sticker hoặc layout ở cột bên trái.</span>
          </div>
        </div>

      </div>

    </div>

  </div>
</div>
{% endblock %}

{% block extra_scripts %}
<script src="/static/js/studio-canvas.js"></script>
<script src="/static/js/studio-3d.js"></script>
<script src="/static/js/studio-ai.js"></script>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'studio.html'), 'w', encoding='utf-8') as f:
    f.write(studio_html)
print('Updated templates/studio.html')

# 10. templates/cart.html
cart_html = '''{% extends "base.html" %}

{% block title %}Giỏ Hàng Của Bạn - ScrapCraft Studio{% endblock %}

{% block content %}
<div class="py-12 md:py-16 bg-[#fdfbf7]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="mb-8">
      <div class="inline-flex items-center gap-2 bg-amber-300 text-stone-950 px-3.5 py-1 rounded-full text-xs font-black uppercase mb-2 border border-black shadow-neo">
        <span>✦ THANH TOÁN &amp; ĐƠN HÀNG</span>
      </div>
      <h1 class="text-3xl sm:text-4xl font-heading font-black text-stone-900">
        Giỏ Hàng &amp; Đặt Hàng Thủ Công
      </h1>
      <p class="text-xs sm:text-sm text-stone-600 font-medium mt-1">
        Kiểm tra danh mục linh kiện, áp dụng mã voucher và điền địa chỉ nhận hàng.
      </p>
    </div>

    <!-- Empty Cart Box -->
    <div id="empty-cart-view" class="hidden bg-white border-3 border-black rounded-3xl p-12 text-center shadow-neo-xl max-w-lg mx-auto space-y-4">
      <span class="text-amber-800 font-mono font-black text-3xl block font-mono">✦</span>
      <h2 class="text-2xl font-heading font-black text-stone-900">Giỏ hàng của bạn đang trống</h2>
      <p class="text-xs text-stone-600">Bạn chưa thêm phụ kiện hoặc thiết kế nào vào giỏ.</p>
      <div class="pt-2 flex justify-center gap-3">
        <a href="/products" class="bg-amber-300 hover:bg-amber-400 text-stone-950 font-heading font-black text-xs px-6 py-3 rounded-xl border-2 border-black shadow-neo transition-all">
          Khám Phá Phụ Kiện
        </a>
        <a href="/studio" class="bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-xs px-6 py-3 rounded-xl border-2 border-black shadow-neo transition-all">
          Vào Xưởng Thiết Kế
        </a>
      </div>
    </div>

    <!-- Cart Layout Grid (Items + Checkout Form) -->
    <div id="cart-content-view" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
      
      <!-- Left Column: Items List -->
      <div class="lg:col-span-7 space-y-6">
        
        <div class="bg-white border-3 border-black rounded-3xl p-6 sm:p-8 shadow-neo-xl space-y-6">
          <div class="flex items-center justify-between pb-4 border-b border-stone-200">
            <h2 class="text-lg font-heading font-black text-stone-900">Danh Mục Sản Phẩm (<span id="cart-items-count">0</span>)</h2>
            <button onclick="clearAllCart()" class="text-xs font-bold text-rose-800 hover:underline">Xóa tất cả</button>
          </div>

          <!-- Dynamic Items Container -->
          <div id="cart-items-container" class="space-y-4">
            <!-- Items rendered via static/js/cart.js -->
          </div>
        </div>

        <!-- Voucher Code Box -->
        <div class="bg-white border-2 border-black rounded-3xl p-6 shadow-neo space-y-3">
          <label class="block text-xs font-heading font-black text-stone-900 uppercase">Mã Khuyến Mãi / Voucher Giảm Giá:</label>
          <div class="flex items-center gap-2">
            <input type="text" id="voucher-input" placeholder="Nhập GENZ10 hoặc SCRAPCRAFT15" class="flex-grow bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-mono font-bold uppercase focus:outline-none focus:border-rose-800">
            <button onclick="applyVoucherCode()" class="bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-xs px-5 py-2.5 rounded-xl border-2 border-black shadow-neo transition-all">
              Áp Dụng
            </button>
          </div>
          <p id="voucher-msg" class="text-xs font-bold text-amber-900 hidden"></p>
        </div>

      </div>

      <!-- Right Column: Checkout Form & Summary -->
      <div class="lg:col-span-5 space-y-6">
        
        <div class="bg-white border-3 border-black rounded-3xl p-6 sm:p-8 shadow-neo-xl space-y-6">
          <h2 class="text-lg font-heading font-black text-stone-900 pb-3 border-b border-stone-200">Thông Tin Nhận Hàng</h2>

          <form id="checkout-form" onsubmit="submitCustomerOrder(event)" class="space-y-4">
            <div>
              <label class="block text-xs font-black text-stone-800 uppercase mb-1">Họ &amp; Tên Người Nhận *</label>
              <input type="text" id="order-name" required placeholder="Nguyễn Văn A" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800">
            </div>

            <div>
              <label class="block text-xs font-black text-stone-800 uppercase mb-1">Số Điện Thoại / Zalo *</label>
              <input type="tel" id="order-phone" required placeholder="0988 xxx xxx" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800">
            </div>

            <div>
              <label class="block text-xs font-black text-stone-800 uppercase mb-1">Địa Chỉ Nhận Hàng Chi Tiết *</label>
              <input type="text" id="order-address" required placeholder="Số nhà, tên đường, phường/xã, quận/huyện, tỉnh/TP" class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800">
            </div>

            <div>
              <label class="block text-xs font-black text-stone-800 uppercase mb-1">Ghi Chú Đơn Hàng (Tùy chọn)</label>
              <textarea id="order-note" rows="2" placeholder="VD: Gói quà kèm nơ, giao giờ hành chính..." class="w-full bg-stone-50 border-2 border-black rounded-xl px-4 py-2.5 text-xs font-semibold focus:outline-none focus:border-rose-800"></textarea>
            </div>

            <!-- Price Breakdown -->
            <div class="border-t border-stone-200 pt-4 space-y-2 text-xs">
              <div class="flex justify-between text-stone-600">
                <span>Tạm tính:</span>
                <span id="summary-subtotal" class="font-bold text-stone-900">0 đ</span>
              </div>
              <div class="flex justify-between text-stone-600">
                <span>Giảm giá voucher:</span>
                <span id="summary-discount" class="font-bold text-rose-800">-0 đ</span>
              </div>
              <div class="flex justify-between text-stone-600">
                <span>Phí vận chuyển:</span>
                <span id="summary-shipping" class="font-bold text-stone-900">30.000 đ</span>
              </div>
              <div class="flex justify-between text-base font-heading font-black text-stone-900 border-t border-stone-300 pt-2">
                <span>Tổng thanh toán:</span>
                <span id="summary-final" class="text-rose-800">0 đ</span>
              </div>
            </div>

            <button type="submit" id="btn-place-order" class="w-full bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-sm py-4 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all text-center flex items-center justify-center gap-2">
              <span>Xác Nhận Đặt Hàng</span>
              <span class="font-mono">→</span>
            </button>
          </form>

        </div>

      </div>

    </div>

  </div>
</div>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'cart.html'), 'w', encoding='utf-8') as f:
    f.write(cart_html)
print('Updated templates/cart.html')

# 11. templates/order_tracking.html
order_tracking_html = '''{% extends "base.html" %}

{% block title %}Tra Cứu Tiến Độ Đơn Hàng - ScrapCraft Studio{% endblock %}

{% block content %}
<div class="py-12 md:py-16 bg-[#fdfbf7]">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
    
    <div class="text-center max-w-xl mx-auto">
      <div class="inline-flex items-center gap-2 bg-amber-300 text-stone-950 px-3.5 py-1 rounded-full text-xs font-black uppercase mb-2 border border-black shadow-neo">
        <span>✦ HỆ THỐNG TRA CỨU ĐƠN HÀNG</span>
      </div>
      <h1 class="text-3xl font-heading font-black text-stone-900">
        Kiểm Tra Tiến Độ Đơn Hàng
      </h1>
      <p class="text-xs text-stone-600 mt-1">
        Nhập mã đơn hàng (VD: SC-xxxxxx) hoặc số điện thoại bạn đã dùng khi đặt hàng.
      </p>
    </div>

    <!-- Query Search Form -->
    <div class="bg-white border-3 border-black rounded-3xl p-6 sm:p-8 shadow-neo-xl">
      <form id="order-tracking-form" onsubmit="handleOrderSearch(event)" class="flex flex-col sm:flex-row items-center gap-3">
        <input type="text" id="query-input" value="{{ initial_code }}" required placeholder="Nhập mã đơn hàng hoặc SĐT..." class="flex-grow w-full bg-stone-50 border-2 border-black rounded-2xl px-5 py-3 text-sm font-semibold focus:outline-none focus:border-rose-800">
        <button type="submit" class="w-full sm:w-auto bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-sm px-8 py-3.5 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all">
          Tra Cứu Ngay →
        </button>
      </form>
    </div>

    <!-- Tracking Results Area -->
    <div id="tracking-results-area" class="space-y-6">
      <!-- Injected via JavaScript -->
    </div>

  </div>
</div>
{% endblock %}

{% block extra_scripts %}
<script>
document.addEventListener('DOMContentLoaded', () => {
  const initCode = '{{ initial_code }}';
  if (initCode) {
    fetchOrdersData(initCode);
  }
});

async function handleOrderSearch(e) {
  e.preventDefault();
  const q = document.getElementById('query-input').value.trim();
  if (q) fetchOrdersData(q);
}

async function fetchOrdersData(query) {
  const resultsArea = document.getElementById('tracking-results-area');
  resultsArea.innerHTML = '<div class=\"text-center py-8 font-bold text-stone-600\">Đang tra cứu cơ sở dữ liệu xưởng...</div>';
  
  try {
    const res = await fetch(`/api/orders?q=${encodeURIComponent(query)}`);
    const data = await res.json();
    
    if (!data.orders || data.orders.length === 0) {
      resultsArea.innerHTML = `
        <div class="bg-white border-2 border-black rounded-3xl p-8 text-center shadow-neo">
          <p class="font-heading font-black text-lg text-stone-900 mb-1">Không tìm thấy đơn hàng phù hợp</p>
          <p class="text-xs text-stone-500">Vui lòng kiểm tra lại mã đơn hàng hoặc số điện thoại.</p>
        </div>
      `;
      return;
    }

    resultsArea.innerHTML = data.orders.map(order => `
      <div class="bg-white border-3 border-black rounded-3xl p-6 sm:p-8 shadow-neo-xl space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-4 pb-4 border-b border-stone-200">
          <div>
            <span class="text-xs font-mono font-bold text-stone-400">Mã đơn:</span>
            <h2 class="text-xl font-heading font-black text-rose-800 font-mono">${order.order_code}</h2>
          </div>
          <span class="bg-amber-300 text-stone-950 text-xs font-black px-3.5 py-1.5 rounded-full border border-black shadow-sm">
            ${order.status}
          </span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
          <div>
            <span class="text-stone-400 font-bold block mb-1">Thông tin khách hàng:</span>
            <p class="font-bold text-stone-900">${order.name} - ${order.phone}</p>
            <p class="text-stone-600 mt-0.5">${order.address}</p>
          </div>
          <div>
            <span class="text-stone-400 font-bold block mb-1">Thời gian đặt:</span>
            <p class="font-bold text-stone-900">${order.created_at}</p>
            <p class="text-stone-600 mt-0.5">Ghi chú: ${order.note || 'Không có'}</p>
          </div>
        </div>

        <div class="border-t border-stone-200 pt-4 space-y-3">
          <span class="text-xs font-black text-stone-900 uppercase">Sản phẩm trong đơn:</span>
          <div class="space-y-2">
            ${order.items.map(item => `
              <div class="flex justify-between items-center bg-stone-50 p-3 rounded-xl border border-stone-200 text-xs">
                <span class="font-bold text-stone-800">${item.sku || ''} - ${item.name} (x${item.quantity || 1})</span>
                <span class="font-black text-stone-900">${(item.price * (item.quantity || 1)).toLocaleString('vi-VN')} đ</span>
              </div>
            `).join('')}
          </div>
        </div>

        <div class="border-t border-stone-200 pt-4 flex justify-between items-center text-sm">
          <span class="font-bold text-stone-600">Tổng thanh toán:</span>
          <span class="font-heading font-black text-xl text-rose-800">${order.final_amount.toLocaleString('vi-VN')} đ</span>
        </div>
      </div>
    `).join('');

  } catch (err) {
    resultsArea.innerHTML = '<div class=\"text-center py-8 font-bold text-rose-800\">Lỗi kết nối máy chủ!</div>';
  }
}
</script>
{% endblock %}
'''

with open(os.path.join(TEMPLATES_DIR, 'order_tracking.html'), 'w', encoding='utf-8') as f:
    f.write(order_tracking_html)
print('Updated templates/order_tracking.html')
print('ALL 11 TEMPLATES SUCCESSFULLY GENERATED AND SYNCHRONIZED!')