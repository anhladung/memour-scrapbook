import os
import json

SVGS = {
    "lay_not_001.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <defs>
    <filter id="shadow01" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.18"/>
    </filter>
  </defs>
  <g filter="url(#shadow01)">
    <rect x="20" y="20" width="320" height="260" rx="8" fill="#fdfbf7" stroke="#e2e8f0" stroke-width="2"/>
    <rect x="130" y="10" width="100" height="22" rx="3" fill="#fb7185" opacity="0.85" transform="rotate(-2 180 20)"/>
    <text x="45" y="60" font-family="'Patrick Hand', cursive, sans-serif" font-size="20" font-weight="bold" fill="#881337">✦ Nhật Ký Ghi Chú:</text>
    <line x1="45" y1="95" x2="315" y2="95" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="130" x2="315" y2="130" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="165" x2="315" y2="165" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="200" x2="315" y2="200" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="235" x2="315" y2="235" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <line x1="45" y1="260" x2="315" y2="260" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 2"/>
    <text x="310" y="272" font-family="'Patrick Hand', cursive" font-size="11" fill="#94a3b8" text-anchor="end">MEMOUR • LAY-NOT-001</text>
  </g>
</svg>""",

    "lay_not_002.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <defs>
    <filter id="shadow02" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.18"/>
    </filter>
    <pattern id="dotPattern" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="1.6" fill="#94a3b8"/>
    </pattern>
  </defs>
  <g filter="url(#shadow02)">
    <rect x="20" y="20" width="320" height="260" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
    <rect x="35" y="35" width="290" height="230" fill="url(#dotPattern)"/>
    <!-- Binder Clip Top Center -->
    <rect x="155" y="12" width="50" height="18" rx="4" fill="#0284c7"/>
    <circle cx="180" cy="21" r="4" fill="#ffffff"/>
    <text x="45" y="58" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="900" fill="#0284c7" letter-spacing="1">BULLET DOT GRID ✦</text>
    <text x="310" y="272" font-family="monospace" font-size="10" font-weight="bold" fill="#64748b" text-anchor="end">LAY-NOT-002</text>
  </g>
</svg>""",

    "lay_not_003.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <defs>
    <filter id="shadow03" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.18"/>
    </filter>
    <pattern id="gridPattern" width="16" height="16" patternUnits="userSpaceOnUse">
      <path d="M 16 0 L 0 0 0 16" fill="none" stroke="#e2e8f0" stroke-width="1.2"/>
    </pattern>
  </defs>
  <g filter="url(#shadow03)">
    <rect x="20" y="20" width="320" height="260" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
    <rect x="35" y="35" width="290" height="230" fill="url(#gridPattern)"/>
    <rect x="145" y="12" width="70" height="18" rx="4" fill="#1e293b"/>
    <text x="45" y="58" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="900" fill="#1e293b" letter-spacing="1">MINIMAL GRID ✦</text>
    <text x="310" y="272" font-family="monospace" font-size="10" font-weight="bold" fill="#64748b" text-anchor="end">LAY-NOT-003</text>
  </g>
</svg>""",

    "lay_not_004.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <defs>
    <filter id="shadow04" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="4" flood-color="#78350f" flood-opacity="0.22"/>
    </filter>
  </defs>
  <g filter="url(#shadow04)">
    <rect x="20" y="20" width="320" height="260" rx="10" fill="#e8d8c3" stroke="#b45309" stroke-width="2"/>
    <rect x="32" y="32" width="296" height="236" rx="6" fill="none" stroke="#78350f" stroke-width="1.5" stroke-dasharray="5 4"/>
    <circle cx="285" cy="65" r="22" fill="none" stroke="#881337" stroke-width="2" opacity="0.8"/>
    <text x="285" y="68" font-family="monospace" font-size="8" font-weight="bold" fill="#881337" text-anchor="middle">PASSPORT</text>
    <text x="45" y="65" font-family="'Patrick Hand', cursive" font-size="20" font-weight="bold" fill="#78350f">✦ Ghi Chú Kraft:</text>
    <line x1="45" y1="100" x2="305" y2="100" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="45" y1="140" x2="305" y2="140" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="45" y1="180" x2="305" y2="180" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="45" y1="220" x2="305" y2="220" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
    <line x1="45" y1="250" x2="305" y2="250" stroke="#b45309" stroke-width="1.5" stroke-dasharray="3 3"/>
  </g>
</svg>""",

    "lay_not_005.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <defs>
    <filter id="shadow05" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="4" flood-color="#db2777" flood-opacity="0.18"/>
    </filter>
    <linearGradient id="pastelHeader" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fbcfe8"/>
      <stop offset="50%" stop-color="#e9d5ff"/>
      <stop offset="100%" stop-color="#c7d2fe"/>
    </linearGradient>
  </defs>
  <g filter="url(#shadow05)">
    <rect x="20" y="20" width="320" height="260" rx="14" fill="#ffffff" stroke="#f472b6" stroke-width="2"/>
    <rect x="20" y="20" width="320" height="45" rx="14" fill="url(#pastelHeader)"/>
    <rect x="20" y="50" width="320" height="15" fill="url(#pastelHeader)"/>
    <text x="45" y="48" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="900" fill="#831843">💖 SWEET DIARY ✦</text>
    <line x1="45" y1="100" x2="315" y2="100" stroke="#fbcfe8" stroke-width="2"/>
    <line x1="45" y1="140" x2="315" y2="140" stroke="#fbcfe8" stroke-width="2"/>
    <line x1="45" y1="180" x2="315" y2="180" stroke="#fbcfe8" stroke-width="2"/>
    <line x1="45" y1="220" x2="315" y2="220" stroke="#fbcfe8" stroke-width="2"/>
    <text x="310" y="265" font-family="monospace" font-size="10" font-weight="bold" fill="#db2777" text-anchor="end">LAY-NOT-005</text>
  </g>
</svg>""",

    "lay_not_006.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="360" height="300" viewBox="0 0 360 300">
  <defs>
    <filter id="shadow06" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="3" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.2"/>
    </filter>
  </defs>
  <g filter="url(#shadow06)">
    <rect x="20" y="20" width="320" height="260" rx="6" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>
    <rect x="40" y="35" width="280" height="140" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="4 3"/>
    <text x="180" y="110" font-family="'Patrick Hand', cursive" font-size="16" fill="#94a3b8" text-anchor="middle">📷 Dán ảnh hoặc vẽ tay</text>
    <line x1="40" y1="205" x2="320" y2="205" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3 2"/>
    <line x1="40" y1="240" x2="320" y2="240" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3 2"/>
    <text x="315" y="268" font-family="'Patrick Hand', cursive" font-size="12" fill="#64748b" text-anchor="end">MEMOUR POLAROID • LAY-NOT-006</text>
  </g>
</svg>"""
}

# 1. Save SVGs
target_dir = os.path.join("static", "assets", "layouts")
os.makedirs(target_dir, exist_ok=True)
for fname, content in SVGS.items():
    fpath = os.path.join(target_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created: {fpath}")

# 2. Add products to data/products.json
NEW_PRODUCTS = [
    {
        "id": "LAY-NOT-001",
        "sku": "LAY-NOT-001",
        "type": "layout",
        "name": "Khung Giấy Kẻ Dòng Viết Tay Vintage Lined Note",
        "category": "layout",
        "category_name": "Khung Ghi Chú & Layout Ảnh",
        "price": 35000,
        "original_price": 45000,
        "image": "/static/assets/layouts/lay_not_001.svg",
        "thumbnail": "/static/assets/layouts/lay_not_001.svg",
        "badge": "Viết Tay Vintage",
        "description": "Khung giấy mỹ thuật kẻ dòng ngang phong cách vintage kèm băng keo washi tape, thiết kế để khách hàng tự viết bút mực, ghi chép kỷ niệm hoặc gõ chữ.",
        "is_3d": True,
        "depth": 0.4,
        "material": "Giấy mỹ thuật Woodfree 250gsm dập nổi",
        "dimension": "Kích thước 12 x 10 cm",
        "themes": ["Vintage", "Viết tay", "Nhật ký", "Kỷ niệm"],
        "colors": ["Trắng Ngà", "Hồng Washi", "Đỏ Rượu"],
        "style": "Vintage Lined Journal Note",
        "occasion": "Nhật ký bạn thân, Thơ tình, Lời chúc sinh nhật",
        "emotion": "Sâu lắng, Hoài niệm, Chân thành",
        "stock": 200,
        "compatible_layouts": ["SCR-001", "SCR-004"],
        "specs": {"paper": "Woodfree 250gsm", "finish": "Matte Craft"}
    },
    {
        "id": "LAY-NOT-002",
        "sku": "LAY-NOT-002",
        "type": "layout",
        "name": "Khung Nhật Ký Chấm Dot Grid Bullet Journal",
        "category": "layout",
        "category_name": "Khung Ghi Chú & Layout Ảnh",
        "price": 35000,
        "original_price": 45000,
        "image": "/static/assets/layouts/lay_not_002.svg",
        "thumbnail": "/static/assets/layouts/lay_not_002.svg",
        "badge": "Bullet Journal",
        "description": "Thẻ ghi chú họa tiết chấm tròn Dot Grid 5mm chuẩn Bullet Journal quốc tế, kèm kẹp kim loại xanh dương để tự do vẽ sơ đồ, ghi quote hoặc viết tay.",
        "is_3d": True,
        "depth": 0.4,
        "material": "Giấy chấm Dot Grid cao cấp chống lem mực",
        "dimension": "Kích thước 12 x 10 cm",
        "themes": ["Bullet Journal", "Dot Grid", "Minimalist", "Sáng tạo"],
        "colors": ["Trắng Tinh", "Xanh Dương", "Xám Slate"],
        "style": "Modern Dot Grid Planner",
        "occasion": "Lập kế hoạch, Ghi quote tâm đắc, Vẽ doodle",
        "emotion": "Gọn gàng, Tự do, Cảm hứng",
        "stock": 200,
        "compatible_layouts": ["SCR-001", "SCR-002", "SCR-003"],
        "specs": {"paper": "Dot Grid 250gsm", "finish": "Smooth"}
    },
    {
        "id": "LAY-NOT-003",
        "sku": "LAY-NOT-003",
        "type": "layout",
        "name": "Khung Ô Lưới Minimalist Grid Memo Card",
        "category": "layout",
        "category_name": "Khung Ghi Chú & Layout Ảnh",
        "price": 35000,
        "original_price": 45000,
        "image": "/static/assets/layouts/lay_not_003.svg",
        "thumbnail": "/static/assets/layouts/lay_not_003.svg",
        "badge": "Minimalist",
        "description": "Khung nhật ký ô lưới 4mm tối giản tinh tế theo phong cách kiến trúc hiện đại, điểm nhấn kẹp sắt đen sang trọng.",
        "is_3d": True,
        "depth": 0.4,
        "material": "Giấy mỹ thuật ô lưới Grid",
        "dimension": "Kích thước 12 x 10 cm",
        "themes": ["Minimalist", "Grid", "Architecture", "Hiện đại"],
        "colors": ["Trắng", "Đen Kim Loại", "Xám Bạc"],
        "style": "Minimal Grid Architecture",
        "occasion": "Lưu bút, Viết nhật ký du lịch, Note ý tưởng",
        "emotion": "Tinh tế, Tối giản, Đẳng cấp",
        "stock": 180,
        "compatible_layouts": ["SCR-003", "SCR-001"],
        "specs": {"paper": "Grid Paper 240gsm", "finish": "Matte"}
    },
    {
        "id": "LAY-NOT-004",
        "sku": "LAY-NOT-004",
        "type": "layout",
        "name": "Thẻ Ghi Chú Giấy Kraft Mộc Tự Nhiên Passport",
        "category": "layout",
        "category_name": "Khung Ghi Chú & Layout Ảnh",
        "price": 35000,
        "original_price": 45000,
        "image": "/static/assets/layouts/lay_not_004.svg",
        "thumbnail": "/static/assets/layouts/lay_not_004.svg",
        "badge": "Kraft Mộc",
        "description": "Thẻ ghi chú giấy Kraft nâu dập viền chỉ may và đóng dấu thị thực Passport du lịch, phong cách Vintage phiêu lưu.",
        "is_3d": True,
        "depth": 0.4,
        "material": "Giấy Kraft tự nhiên 280gsm",
        "dimension": "Kích thước 12 x 10 cm",
        "themes": ["Kraft", "Vintage", "Du lịch", "Passport", "Adventure"],
        "colors": ["Nâu Kraft", "Đỏ Rượu", "Vàng Đất"],
        "style": "Vintage Travel Passport Memo",
        "occasion": "Nhật ký du lịch, Kỷ yếu phượt, Kỷ niệm thanh xuân",
        "emotion": "Phiêu lưu, Ấm áp, Hoài niệm",
        "stock": 220,
        "compatible_layouts": ["SCR-001", "SCR-004"],
        "specs": {"paper": "Kraft 280gsm", "finish": "Organic Texture"}
    },
    {
        "id": "LAY-NOT-005",
        "sku": "LAY-NOT-005",
        "type": "layout",
        "name": "Khung Nhật Ký Pastel Aesthetic Sweet Diary",
        "category": "layout",
        "category_name": "Khung Ghi Chú & Layout Ảnh",
        "price": 38000,
        "original_price": 48000,
        "image": "/static/assets/layouts/lay_not_005.svg",
        "thumbnail": "/static/assets/layouts/lay_not_005.svg",
        "badge": "Sweet Pastel",
        "description": "Khung nhật ký viền hồng pastel ngọt ngào kèm thanh tiêu đề chuyển sắc cầu vồng Hologram, lý tưởng cho lưu bút tình bạn và couple.",
        "is_3d": True,
        "depth": 0.4,
        "material": "Giấy mỹ thuật Pastel phủ màng mờ",
        "dimension": "Kích thước 12 x 10 cm",
        "themes": ["Pastel", "Couple", "Ngọt ngào", "Tình bạn", "Y2K"],
        "colors": ["Hồng Pastel", "Tím Oải Hương", "Xanh Baby"],
        "style": "Sweet Pastel Aesthetic",
        "occasion": "Tình yêu, Kỷ niệm ngày hẹn hò, Sinh nhật bạn gái",
        "emotion": "Ngọt ngào, Dễ thương, Lãng mạn",
        "stock": 190,
        "compatible_layouts": ["SCR-002", "SCR-001"],
        "specs": {"paper": "Pastel Card 250gsm", "finish": "Silky Matte"}
    },
    {
        "id": "LAY-NOT-006",
        "sku": "LAY-NOT-006",
        "type": "layout",
        "name": "Khung Ảnh Polaroid Kèm Phần Ghi Lời Nhắn",
        "category": "layout",
        "category_name": "Khung Ghi Chú & Layout Ảnh",
        "price": 35000,
        "original_price": 45000,
        "image": "/static/assets/layouts/lay_not_006.svg",
        "thumbnail": "/static/assets/layouts/lay_not_006.svg",
        "badge": "Polaroid Memo",
        "description": "Khung ảnh Polaroid cải tiến có khung cài ảnh phía trên và 2 dòng kẻ phía dưới để viết ngày chụp, địa điểm hoặc lời nhắn tay.",
        "is_3d": True,
        "depth": 0.4,
        "material": "Giấy bìa ảnh ép màng chống ẩm",
        "dimension": "Kích thước 12 x 10 cm",
        "themes": ["Polaroid", "Ảnh chụp", "Viết tay", "Kỷ niệm"],
        "colors": ["Trắng Sáng", "Xám Khói"],
        "style": "Hybrid Polaroid Memo Card",
        "occasion": "Lưu ảnh chụp tức thì, Kỷ niệm họp lớp",
        "emotion": "Chân thực, Tự nhiên, Đáng nhớ",
        "stock": 250,
        "compatible_layouts": ["SCR-001", "SCR-002", "SCR-003", "SCR-004"],
        "specs": {"paper": "Photo Card 300gsm", "finish": "Glossy Frame"}
    }
]

prod_path = os.path.join("data", "products.json")
with open(prod_path, "r", encoding="utf-8") as f:
    products = json.load(f)

# Remove any existing duplicate SKUs
existing_skus = {p["sku"] for p in NEW_PRODUCTS}
products = [p for p in products if p.get("sku") not in existing_skus]

# Append new products
products.extend(NEW_PRODUCTS)

with open(prod_path, "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f"Updated data/products.json successfully with {len(products)} total items!")
