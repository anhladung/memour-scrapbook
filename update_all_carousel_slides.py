import os
import re

TEMPLATES_DIR = 'templates'

replacements = [
    (
        os.path.join(TEMPLATES_DIR, 'index.html'),
        "Bật Mood <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>Sáng Tạo</span> Gói Ký Ức Vào Giấy Thủ Công!",
        "Bật Mood <span class='text-amber-300 underline decoration-rose-500 decoration-wavy decoration-4'>Sáng Tạo</span> Gói Ký Ức Vào Giấy Thủ Công!"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'index.html'),
        "Xem Trước Từng Góc Cạnh Với <span class='text-rose-800'>Trình Xem 3D</span>",
        "Xem Trước Từng Góc Cạnh Với <span class='text-amber-300'>Trình Xem 3D</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'index.html'),
        "24 Mã Định Danh Đồng Bộ <span class='text-rose-800'>Single Source of Truth</span>",
        "24 Mã Định Danh Đồng Bộ <span class='text-amber-300'>Single Source of Truth</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'about.html'),
        "Tái Sinh Ký Ức Số Thành <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>Trang Sổ Biết Kể Chuyện</span>",
        "Tái Sinh Ký Ức Số Thành <span class='text-amber-300 underline decoration-rose-500 decoration-wavy decoration-4'>Trang Sổ Biết Kể Chuyện</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'about.html'),
        "Chất Liệu Giấy Mỹ Thuật <span class='text-rose-800'>Acid-Free Cao Cấp</span>",
        "Chất Liệu Giấy Mỹ Thuật <span class='text-amber-300'>Acid-Free Cao Cấp</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'about.html'),
        "Kết Nối Thủ Công Tinh Xảo Với <span class='text-rose-800'>Trí Tuệ Nhân Tạo</span>",
        "Kết Nối Thủ Công Tinh Xảo Với <span class='text-amber-300'>Trí Tuệ Nhân Tạo</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'products.html'),
        "Kho Phụ Kiện <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>Chuẩn Gu Gen Z</span> 24 Mã SKU",
        "Kho Phụ Kiện <span class='text-amber-300 underline decoration-rose-500 decoration-wavy decoration-4'>Chuẩn Gu Gen Z</span> 24 Mã SKU"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'products.html'),
        "Sticker Dập Nổi 0.8mm <span class='text-rose-800'>Phủ Màng Hologram Laser</span>",
        "Sticker Dập Nổi 0.8mm <span class='text-amber-300'>Phủ Màng Hologram Laser</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'products.html'),
        "Layout Khung Cài Thông Minh & <span class='text-rose-800'>Sổ Bìa Cứng Kraft</span>",
        "Layout Khung Cài Thông Minh & <span class='text-amber-300'>Sổ Bìa Cứng Kraft</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'inspirations.html'),
        "Mẫu Bố Cục Tinh Tuyển <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>100% SKU Có Sẵn</span>",
        "Mẫu Bố Cục Tinh Tuyển <span class='text-amber-300 underline decoration-rose-500 decoration-wavy decoration-4'>100% SKU Có Sẵn</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'inspirations.html'),
        "Từ Vintage Kỷ Yếu Đến <span class='text-rose-800'>Cyberpunk Y2K &amp; Couple</span>",
        "Từ Vintage Kỷ Yếu Đến <span class='text-amber-300'>Cyberpunk Y2K &amp; Couple</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'inspirations.html'),
        "Ưu Đãi Trọn Bộ Combo <span class='text-rose-800'>Tự Động Giảm Giá 15%</span>",
        "Ưu Đãi Trọn Bộ Combo <span class='text-amber-300'>Tự Động Giảm Giá 15%</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'handbook.html'),
        "Bí Quyết Sáng Tạo <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>Scrapbook Chuẩn Gu Gen Z</span>",
        "Bí Quyết Sáng Tạo <span class='text-amber-300 underline decoration-rose-500 decoration-wavy decoration-4'>Scrapbook Chuẩn Gu Gen Z</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'handbook.html'),
        "Nghệ Thuật Xếp Lớp <span class='text-rose-800'>Tạo Chiều Sâu Đa Tầng</span>",
        "Nghệ Thuật Xếp Lớp <span class='text-amber-300'>Tạo Chiều Sâu Đa Tầng</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'handbook.html'),
        "Lựa Chọn Giấy Acid-Free & <span class='text-rose-800'>Khung Cài Bảo Tàng</span>",
        "Lựa Chọn Giấy Acid-Free & <span class='text-amber-300'>Khung Cài Bảo Tàng</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'contact.html'),
        "Showroom &amp; Xưởng Thủ Công <span class='text-rose-800 underline decoration-amber-400 decoration-wavy decoration-4'>ScrapCraft Studio</span>",
        "Showroom &amp; Xưởng Thủ Công <span class='text-amber-300 underline decoration-rose-500 decoration-wavy decoration-4'>ScrapCraft Studio</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'contact.html'),
        "Nhận Gia Công Sổ Kỷ Yếu & <span class='text-rose-800'>Set Quà Tặng Doanh Nghiệp</span>",
        "Nhận Gia Công Sổ Kỷ Yếu & <span class='text-amber-300'>Set Quà Tặng Doanh Nghiệp</span>"
    ),
    (
        os.path.join(TEMPLATES_DIR, 'contact.html'),
        "Chính Sách Bảo Mật 100% & <span class='text-rose-800'>Bảo Hành 1-Đổi-1 Trong 7 Ngày</span>",
        "Chính Sách Bảo Mật 100% & <span class='text-amber-300'>Bảo Hành 1-Đổi-1 Trong 7 Ngày</span>"
    ),
]

for file_path, old, new in replacements:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if old in content:
            content = content.replace(old, new)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated: {file_path}')

print('All carousels synchronized!')
