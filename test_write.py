import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
ASSETS_DIR = os.path.join(STATIC_DIR, 'assets')
STICKERS_DIR = os.path.join(ASSETS_DIR, 'stickers')
LAYOUTS_DIR = os.path.join(ASSETS_DIR, 'layouts')
BOOKS_DIR = os.path.join(ASSETS_DIR, 'books')

for d in [DATA_DIR, STATIC_DIR, ASSETS_DIR, STICKERS_DIR, LAYOUTS_DIR, BOOKS_DIR]:
    os.makedirs(d, exist_ok=True)

# 1. PRODUCTS DATA (SINGLE SOURCE OF TRUTH)
products = [
  # STICKERS (12 items)
  {
    "id": "STK-001",
    "sku": "STK-001",
    "type": "sticker",
    "name": "Sticker 3D Hologram Y2K Sparkle Stars",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 35000,
    "original_price": 45000,
    "image": "/static/assets/stickers/stk_001.svg",
    "thumbnail": "/static/assets/stickers/stk_001.svg",
    "badge": "Hot Trend Gen Z",
    "description": "Bộ sticker ngôi sao 4 cánh phong cách Y2K Cyberpunk dập nổi 3D, phủ lớp màng cầu vồng Hologram phản chiếu ánh sáng cực bắt mắt.",
    "is_3d": True,
    "depth": 0.8,
    "material": "Decal Vinyl dập nổi 3D + Phủ Hologram Laser",
    "dimension": "Tấm 10 x 15 cm (Gồm 24 chi tiết rời)",
    "themes": ["Y2K", "Cyber Aesthetic", "Sparkle", "Sinh nhật", "Party"],
    "colors": ["Cầu vồng Hologram", "Bạc Ánh Kim", "Tím Pastel"],
    "style": "Y2K Cyberpunk Hologram",
    "occasion": "Sinh nhật, Kỷ yếu, Party quẩy cùng bạn thân",
    "emotion": "Năng động, Lấp lánh, Tự tin",
    "stock": 150,
    "compatible_layouts": ["LAY-001", "LAY-003", "LAY-008"],
    "attributes": {
      "material": "Decal Vinyl dập nổi 3D + Phủ Hologram Laser",
      "dimension": "Tấm 10 x 15 cm (Gồm 24 chi tiết)",
      "theme": "Y2K / Cyber Aesthetic / Sparkle",
      "color": "Cầu vồng Hologram / Bạc Ánh Kim",
      "finish_3d": "Dập nổi viền 0.8mm, phản quang 360°",
      "waterproof": True,
      "origin": "Xưởng Thủ Công ScrapCraft - Màng Laser Hàn Quốc"
    },
    "tags": ["y2k", "hologram", "ngôi sao", "sparkle", "cyber", "sinh nhật", "lấp lánh", "sticker 3d"],
    "ai_keywords": ["y2k", "ngôi sao", "hologram", "lấp lánh", "cyber", "năng động", "sinh nhật", "trend", "sparkle", "star", "holographic", "quẩy", "party"]
  },
  {
    "id": "STK-002",
    "sku": "STK-002",
    "type": "sticker",
    "name": "Sticker Giấy Kraft Vintage Botanical Florals",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 32000,
    "original_price": 40000,
    "image": "/static/assets/stickers/stk_002.svg",
    "thumbnail": "/static/assets/stickers/stk_002.svg",
    "badge": "Best Seller Vintage",
    "description": "Bộ nhãn dán hoa cỏ đồng nội ép khô phong cách Vintage cổ điển, in trên nền giấy Washi Kraft Nhật Bản mộc mạc và hoài niệm.",
    "is_3d": False,
    "depth": 0.2,
    "material": "Giấy Washi tự nhiên xé tay + Mực đậu nành Eco-friendly",
    "dimension": "Tấm 12 x 18 cm (Gồm 30 chi tiết hoa lá)",
    "themes": ["Vintage", "Botanical", "Cottagecore", "Hoài niệm", "Du lịch"],
    "colors": ["Nâu Kraft", "Xanh Olive", "Cam Đất", "Vàng Mù Tạt"],
    "style": "Cổ điển Mộc mạc (Botanical Vintage)",
    "occasion": "Du lịch Đà Lạt, Kỷ niệm gia đình, Sổ nhật ký",
    "emotion": "Bình yên, Hoài niệm, Ấm áp",
    "stock": 200,
    "compatible_layouts": ["LAY-001", "LAY-004", "LAY-007"],
    "attributes": {
      "material": "Giấy Washi tự nhiên xé tay + Mực đậu nành Eco-friendly",
      "dimension": "Tấm 12 x 18 cm (Gồm 30 chi tiết hoa lá)",
      "theme": "Vintage / Botanical / Cottagecore / Hoài niệm",
      "color": "Nâu Kraft / Xanh Olive / Cam Đất",
      "finish_3d": "Mặt giấy mờ vân nổi nhẹ 0.2mm",
      "waterproof": False,
      "origin": "Giấy tái chế FSC thân thiện môi trường"
    },
    "tags": ["vintage", "hoa cỏ", "kraft", "botanical", "hoài niệm", "đà lạt", "cổ điển", "nhật ký"],
    "ai_keywords": ["vintage", "hoa lá", "cổ điển", "kỷ niệm", "đà lạt", "hoài niệm", "kraft", "botanical", "nature", "retro", "du lịch", "ấm áp"]
  },
  {
    "id": "STK-003",
    "sku": "STK-003",
    "type": "sticker",
    "name": "Sticker 3D Doodle Emoji & Gen Z Slang Vibes",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 38000,
    "original_price": 50000,
    "image": "/static/assets/stickers/stk_003.svg",
    "thumbnail": "/static/assets/stickers/stk_003.svg",
    "badge": "Gen Z Signature",
    "description": "Bộ sticker câu nói Gen Z hot trend kết hợp hình vẽ doodle biểu cảm siêu lầy lội, viền phủ bóng nổi 3D như thạch dẻo Resin.",
    "is_3d": True,
    "depth": 1.2,
    "material": "Decal Resin Thạch 3D Dẻo (Dome 3D Epoxy)",
    "dimension": "Tấm 11 x 16 cm (Gồm 18 biểu cảm)",
    "themes": ["Gen Z Slang", "Funny Doodles", "Street Vibe", "Tình bạn", "Trường học"],
    "colors": ["Xanh Neon (Lime)", "Hồng Acid (Pink)", "Vàng Chanh"],
    "style": "Neo-Brutalism & Street Gen Z",
    "occasion": "Kỷ yếu lớp, Tặng bạn thân, Sổ lưu bút",
    "emotion": "Hài hước, Tinh nghịch, Năng lượng cao",
    "stock": 120,
    "compatible_layouts": ["LAY-002", "LAY-005", "LAY-008"],
    "attributes": {
      "material": "Decal Resin Thạch 3D Dẻo (Dome 3D Epoxy)",
      "dimension": "Tấm 11 x 16 cm (Gồm 18 biểu cảm)",
      "theme": "Gen Z Slang / Funny Doodles / Street Vibe",
      "color": "Neon Pink / Acid Lime / Pastel Yellow",
      "finish_3d": "Đổ keo epoxy nổi hình vòm 1.2mm",
      "waterproof": True,
      "origin": "Thiết kế độc quyền bởi ScrapCraft Team"
    },
    "tags": ["gen z", "doodle", "slay", "meme", "hài hước", "bạn thân", "kỷ yếu", "thạch 3d"],
    "ai_keywords": ["doodle", "slang", "genz", "meme", "vui nhộn", "bạn thân", "kỷ yếu", "slay", "tình bạn", "lầy lội", "resil", "3d epoxy"]
  },
  {
    "id": "STK-004",
    "sku": "STK-004",
    "type": "sticker",
    "name": "Băng Dính Washi Tape Pastel Grid Memory",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 28000,
    "original_price": 35000,
    "image": "/static/assets/stickers/stk_004.svg",
    "thumbnail": "/static/assets/stickers/stk_004.svg",
    "badge": "Scrapbook Essential",
    "description": "Cuộn băng dính washi họa tiết lưới caro pastel và dòng chữ typo mộng mơ, chất liệu giấy mờ dễ xé tay và viết chữ bằng bút mực.",
    "is_3d": False,
    "depth": 0.1,
    "material": "Giấy Washi Nhật Bản keo dính Acrylic không để lại vệt keo",
    "dimension": "Cuộn rộng 1.5 cm x dài 5 mét",
    "themes": ["Minimalist", "Pastel", "Bullet Journal", "Memory"],
    "colors": ["Tím Lavender", "Hồng Phấn", "Trắng Sữa"],
    "style": "Pastel Minimalist Journal",
    "occasion": "Trang trí viền ảnh, Dán ghi chú, Đánh dấu trang",
    "emotion": "Dịu dàng, Ngọt ngào, Gọn gàng",
    "stock": 300,
    "compatible_layouts": ["LAY-001", "LAY-002", "LAY-003", "LAY-005"],
    "attributes": {
      "material": "Giấy Washi Nhật Bản keo dính Acrylic Acid-Free",
      "dimension": "Cuộn rộng 1.5 cm x dài 5 mét",
      "theme": "Minimalist / Pastel / Bullet Journal",
      "color": "Tím Lavender / Hồng Phấn / Trắng",
      "finish_3d": "Mặt mờ tự nhiên chống lóa",
      "waterproof": False,
      "origin": "Nhập khẩu Giấy Washi Nhật Bản"
    },
    "tags": ["washi tape", "băng dính", "caro", "pastel", "journal", "trang trí", "tím lavender"],
    "ai_keywords": ["washi", "băng dính", "caro", "pastel", "tím", "bullet journal", "viền ảnh", "nhẹ nhàng", "ngọt ngào"]
  },
  {
    "id": "STK-005",
    "sku": "STK-005",
    "type": "sticker",
    "name": "Sticker 3D Băng Cassette & Máy Ảnh Ép Kim Vàng",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 42000,
    "original_price": 55000,
    "image": "/static/assets/stickers/stk_005.svg",
    "thumbnail": "/static/assets/stickers/stk_005.svg",
    "badge": "Premium Foil 3D",
    "description": "Sticker dập nổi chi tiết máy nghe nhạc cassette cổ điển thập niên 90s, viền mạ lá vàng kim (Gold Foil Stamping) lấp lánh sang trọng.",
    "is_3d": True,
    "depth": 1.0,
    "material": "Giấy Ivory 300gsm ép nhũ vàng Metallic 3D dập nổi",
    "dimension": "Tấm 10 x 14 cm (Gồm 12 sticker cassette & đĩa than)",
    "themes": ["90s Retro", "Music Playlist", "Vintage Gold", "Hoài niệm"],
    "colors": ["Vàng Kim (Gold)", "Đen Tuyển (Obsidian)", "Nâu Gỗ"],
    "style": "Retro 90s Luxury Gold",
    "occasion": "Kỷ niệm tình yêu, Tặng bạn mê âm nhạc, Album chuyến đi",
    "emotion": "Sang trọng, Sâu lắng, Hoài niệm",
    "stock": 90,
    "compatible_layouts": ["LAY-001", "LAY-002", "LAY-004"],
    "attributes": {
      "material": "Giấy Ivory 300gsm ép nhũ vàng Metallic 3D dập nổi",
      "dimension": "Tấm 10 x 14 cm (Gồm 12 chi tiết)",
      "theme": "90s Retro / Music Playlist / Vintage Gold",
      "color": "Vàng Kim Gold / Đen Than",
      "finish_3d": "Dập nổi cơ học 1.0mm ép nhũ vàng gương",
      "waterproof": False,
      "origin": "Xưởng Dập Nổi Thủ Công ScrapCraft"
    },
    "tags": ["cassette", "retro", "nhũ vàng", "90s", "âm nhạc", "gold foil", "sang trọng", "sticker 3d"],
    "ai_keywords": ["cassette", "retro", "90s", "nhạc", "playlist", "nhũ vàng", "hoài niệm", "vintage", "máy ảnh", "film", "kỷ niệm"]
  },
  {
    "id": "STK-006",
    "sku": "STK-006",
    "type": "sticker",
    "name": "Sticker 3D Trái Tim Bạc Hologram Silver Shine",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 36000,
    "original_price": 46000,
    "image": "/static/assets/stickers/stk_006.svg",
    "thumbnail": "/static/assets/stickers/stk_006.svg",
    "badge": "Romantic Trend",
    "description": "Họa tiết trái tim kết hợp ánh bạc kim cương và viền chỉ may thủ công, dập nổi 3D mềm mại mang lại nét lãng mạn tinh tế cho cuốn album.",
    "is_3d": True,
    "depth": 0.9,
    "material": "Màng Silver Metallic dập nổi 3D cao cấp",
    "dimension": "Tấm 10 x 15 cm (Gồm 20 trái tim kích cỡ khác nhau)",
    "themes": ["Love Story", "Anniversary", "Valentine", "Romantic"],
    "colors": ["Bạc Ánh Kim", "Hồng Pastel", "Trắng Ngọc Trai"],
    "style": "Romantic Silver Shine",
    "occasion": "Kỷ niệm yêu nhau, Valentine, Cầu hôn, Đám cưới",
    "emotion": "Lãng mạn, Ngọt ngào, Say đắm",
    "stock": 140,
    "compatible_layouts": ["LAY-001", "LAY-003", "LAY-007"],
    "attributes": {
      "material": "Màng Silver Metallic dập nổi 3D cao cấp",
      "dimension": "Tấm 10 x 15 cm (Gồm 20 chi tiết)",
      "theme": "Love Story / Anniversary / Romantic",
      "color": "Bạc Ánh Kim / Hồng Pastel",
      "finish_3d": "Dập nổi viền đệm khí 0.9mm",
      "waterproof": True,
      "origin": "ScrapCraft Studio"
    },
    "tags": ["trái tim", "tình yêu", "bạc kim", "anniversary", "valentine", "lãng mạn", "sticker 3d"],
    "ai_keywords": ["trái tim", "tình yêu", "người yêu", "anniversary", "valentine", "bạc", "hologram", "ngọt ngào", "lãng mạn", "hẹn hò"]
  },
  {
    "id": "STK-007",
    "sku": "STK-007",
    "type": "sticker",
    "name": "Sticker 3D Mũ Cử Nhân & Ruy Băng Tốt Nghiệp 2026",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 39000,
    "original_price": 49000,
    "image": "/static/assets/stickers/stk_007.svg",
    "thumbnail": "/static/assets/stickers/stk_007.svg",
    "badge": "Graduation Special",
    "description": "Mẫu sticker chuyên biệt cho lễ tốt nghiệp với hình ảnh mũ cử nhân viền vàng, bằng khen cuộn tròn và dải ruy băng vinh danh dập nổi 3D.",
    "is_3d": True,
    "depth": 1.1,
    "material": "Decal phủ nhũ vàng Gold Metallic dập nổi 3D",
    "dimension": "Tấm 11 x 16 cm (Gồm 16 chi tiết tốt nghiệp)",
    "themes": ["Graduation", "School Memory", "Thanh xuân", "Tốt nghiệp"],
    "colors": ["Xanh Navy Hoàng Gia", "Vàng Hoàng Gia", "Đỏ Rượu"],
    "style": "Royal Academic Graduation",
    "occasion": "Lễ tốt nghiệp, Kỷ yếu đại học, Chia tay cấp 3",
    "emotion": "Tự hào, Xúc động, Trưởng thành",
    "stock": 160,
    "compatible_layouts": ["LAY-001", "LAY-002", "LAY-005"],
    "attributes": {
      "material": "Decal phủ nhũ vàng Gold Metallic dập nổi 3D",
      "dimension": "Tấm 11 x 16 cm (Gồm 16 chi tiết)",
      "theme": "Graduation / School Memory / Thanh xuân",
      "color": "Xanh Navy / Vàng Gold / Đen",
      "finish_3d": "Dập nổi góc cạnh 1.1mm",
      "waterproof": True,
      "origin": "ScrapCraft Studio"
    },
    "tags": ["tốt nghiệp", "mũ cử nhân", "kỷ yếu", "graduation", "thanh xuân", "bạn thân", "sticker 3d"],
    "ai_keywords": ["tốt nghiệp", "graduation", "mũ cử nhân", "kỷ yếu", "lớp học", "thanh xuân", "đại học", "bạn bè", "trưởng thành", "vinh danh"]
  },
  {
    "id": "STK-008",
    "sku": "STK-008",
    "type": "sticker",
    "name": "Sticker Máy Ảnh Film 35mm Analog Shot 3D",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 37000,
    "original_price": 48000,
    "image": "/static/assets/stickers/stk_008.svg",
    "thumbnail": "/static/assets/stickers/stk_008.svg",
    "badge": "Photographer Favorite",
    "description": "Mô phỏng chân thực chiếc máy ảnh film Rangefinder cổ điển với ống kính dập nổi 3D phủ bóng UV như thấu kính thủy tinh thật.",
    "is_3d": True,
    "depth": 0.9,
    "material": "Decal tráng kim loại + Phủ bóng UV thấu kính 3D",
    "dimension": "Tấm 10 x 15 cm (Gồm 15 máy ảnh & cuộn film)",
    "themes": ["Photography", "Film Grain", "Roadtrip", "Vintage"],
    "colors": ["Nâu Da Bò", "Bạc Kim Loại", "Đen"],
    "style": "Analog Film Camera 3D",
    "occasion": "Chuyến du lịch bụi, Chụp ảnh ngoại cảnh, Kỷ niệm phượt",
    "emotion": "Nghệ thuật, Phóng khoáng, Ký ức",
    "stock": 110,
    "compatible_layouts": ["LAY-001", "LAY-002", "LAY-006"],
    "attributes": {
      "material": "Decal tráng kim loại + Phủ bóng UV thấu kính 3D",
      "dimension": "Tấm 10 x 15 cm (Gồm 15 chi tiết)",
      "theme": "Photography / Film Grain / Roadtrip",
      "color": "Nâu Da Bò / Bạc Kim Loại / Đen",
      "finish_3d": "Thấu kính phủ UV nổi vòm 0.9mm",
      "waterproof": True,
      "origin": "ScrapCraft Studio"
    },
    "tags": ["máy ảnh", "film 35mm", "analog", "du lịch", "nhiếp ảnh", "vintage", "sticker 3d"],
    "ai_keywords": ["máy ảnh", "film", "35mm", "chụp ảnh", "du lịch", "phượt", "analog", "kỷ niệm", "roadtrip", "khung hình"]
  },
  {
    "id": "STK-009",
    "sku": "STK-009",
    "type": "sticker",
    "name": "Con Dấu Thị Thực Passport & Airmail Stamp",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 29000,
    "original_price": 38000,
    "image": "/static/assets/stickers/stk_009.svg",
    "thumbnail": "/static/assets/stickers/stk_009.svg",
    "badge": "Travel Essential",
    "description": "Bộ tem thư hàng không và dấu mộc thị thực nhập cảnh các thành phố du lịch nổi tiếng thế giới, in chất mờ mực cổ điển.",
    "is_3d": False,
    "depth": 0.2,
    "material": "Giấy mờ tự dính có viền răng cưa tem thư cổ",
    "dimension": "Tấm 12 x 18 cm (Gồm 28 con dấu & tem thư)",
    "themes": ["Wanderlust", "Traveler", "Summer Vacation", "Airmail"],
    "colors": ["Xanh Biển (Sky Blue)", "Đỏ Bưu Điện", "Nâu Kraft"],
    "style": "Vintage Airmail Postage",
    "occasion": "Du lịch biển, Đi phượt mùa hè, Kỷ niệm chuyến bay",
    "emotion": "Tự do, Phiêu lưu, Khám phá",
    "stock": 220,
    "compatible_layouts": ["LAY-001", "LAY-004", "LAY-005"],
    "attributes": {
      "material": "Giấy mờ tự dính có viền răng cưa tem thư cổ",
      "dimension": "Tấm 12 x 18 cm (Gồm 28 con dấu)",
      "theme": "Wanderlust / Travel / Summer / Airmail",
      "color": "Xanh Biển / Đỏ Bưu Điện / Nâu Kraft",
      "finish_3d": "Bề mặt mờ tự nhiên vintage",
      "waterproof": False,
      "origin": "ScrapCraft Studio"
    },
    "tags": ["passport", "tem thư", "airmail", "du lịch", "chuyến đi", "hành trình", "con dấu"],
    "ai_keywords": ["passport", "du lịch", "tem thư", "airmail", "mùa hè", "hành trình", "chuyến bay", "biển", "khám phá", "wanderlust"]
  },
  {
    "id": "STK-010",
    "sku": "STK-010",
    "type": "sticker",
    "name": "Con Dấu Sáp Niêm Phong Wax Seal Hoàng Gia 3D",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 45000,
    "original_price": 58000,
    "image": "/static/assets/stickers/stk_010.svg",
    "thumbnail": "/static/assets/stickers/stk_010.svg",
    "badge": "Handmade Wax 3D",
    "description": "Con dấu sáp đúc thủ công viền chảy tự nhiên bằng chất liệu sáp dẻo Resin màu đỏ Burgundy quý phái, tạo điểm nhấn hoàng gia sang trọng.",
    "is_3d": True,
    "depth": 1.5,
    "material": "Sáp dẻo Resin nguyên khối có sẵn keo 3M siêu dính",
    "dimension": "Bộ 8 con dấu đường kính 3.0 cm",
    "themes": ["Royal Classic", "Burgundy Red", "Wax Seal", "Wedding"],
    "colors": ["Đỏ Rượu Vang (Burgundy)", "Đỏ Mận", "Vàng Nhũ"],
    "style": "European Royal Vintage",
    "occasion": "Thiệp cưới, Thư tay lãng mạn, Bìa sổ trang trọng",
    "emotion": "Quý phái, Trang trọng, Bí mật",
    "stock": 85,
    "compatible_layouts": ["LAY-001", "LAY-004", "LAY-007"],
    "attributes": {
      "material": "Sáp dẻo Resin nguyên khối + Keo 3M",
      "dimension": "Bộ 8 con dấu đường kính 3.0 cm",
      "theme": "Royal Classic / Burgundy Red / Wax Seal",
      "color": "Đỏ Rượu Vang Burgundy / Vàng Nhũ",
      "finish_3d": "Độ dày khối sáp 1.5mm cực kỳ sống động",
      "waterproof": True,
      "origin": "Xưởng Đúc Sáp Thủ Công ScrapCraft"
    },
    "tags": ["wax seal", "dấu sáp", "đỏ rượu", "burgundy", "hoàng gia", "niêm phong", "sang trọng", "sticker 3d"],
    "ai_keywords": ["wax seal", "dấu sáp", "burgundy", "đỏ rượu", "hoàng gia", "thư tay", "sang trọng", "quý tộc", "cổ điển", "lãng mạn"]
  },
  {
    "id": "STK-011",
    "sku": "STK-011",
    "type": "sticker",
    "name": "Sticker Cốc Cà Phê & Châm Ngôn Thư Giãn Cozy",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 30000,
    "original_price": 38000,
    "image": "/static/assets/stickers/stk_011.svg",
    "thumbnail": "/static/assets/stickers/stk_011.svg",
    "badge": "Cozy Daily",
    "description": "Những chiếc cốc cà phê bốc khói, cuốn sách mở và câu quote chill nhẹ nhàng cho những trang nhật ký ghi lại nhịp sống thường nhật.",
    "is_3d": False,
    "depth": 0.2,
    "material": "Giấy Decal Matte chống lóa viết bút chì được",
    "dimension": "Tấm 10 x 15 cm (Gồm 22 sticker)",
    "themes": ["Cozy Life", "Cafe Time", "Study & Read", "Peaceful"],
    "colors": ["Tím Khói", "Nâu Cà Phê", "Kem Vanilla"],
    "style": "Cozy Cafe Minimalist",
    "occasion": "Nhật ký hàng ngày, Lên kế hoạch tuần, Trang trí góc học tập",
    "emotion": "Thư thái, Bình yên, Tập trung",
    "stock": 175,
    "compatible_layouts": ["LAY-001", "LAY-002", "LAY-004"],
    "attributes": {
      "material": "Giấy Decal Matte chống lóa viết được",
      "dimension": "Tấm 10 x 15 cm (Gồm 22 sticker)",
      "theme": "Cozy Life / Cafe Time / Peaceful",
      "color": "Tím Khói / Nâu Cà Phê / Kem",
      "finish_3d": "Mặt mờ chống bám vân tay",
      "waterproof": False,
      "origin": "ScrapCraft Studio"
    },
    "tags": ["cà phê", "cozy", "nhật ký", "chill", "sách", "thư giãn", "bình yên"],
    "ai_keywords": ["cà phê", "coffee", "cozy", "chill", "nhật ký", "đọc sách", "bình yên", "học tập", "thư giãn", "hàng ngày"]
  },
  {
    "id": "STK-012",
    "sku": "STK-012",
    "type": "sticker",
    "name": "Sticker Khung Film 35mm Âm Bản Cyber Dark",
    "category": "sticker",
    "category_name": "Sticker & Decal Thủ Công",
    "price": 33000,
    "original_price": 42000,
    "image": "/static/assets/stickers/stk_012.svg",
    "thumbnail": "/static/assets/stickers/stk_012.svg",
    "badge": "Dark Aesthetic",
    "description": "Sticker dải phim âm bản màu đen huyền bí với các chi tiết thông số ISO, chấm màu neon phát sáng mang đậm phong cách Dark Academia.",
    "is_3d": False,
    "depth": 0.2,
    "material": "Decal nhựa PVC xuyên sáng mờ phong cách film nhựa",
    "dimension": "Tấm 10 x 16 cm (Gồm 14 khung dải phim)",
    "themes": ["Dark Mode", "Film Negative", "Cyber Aesthetic", "Concert"],
    "colors": ["Đen Obsidian", "Xám Khói", "Neon Lime"],
    "style": "Dark Mode Film Cyberpunk",
    "occasion": "Đêm nhạc rock, Tiệc tối, Chuyến đi đêm",
    "emotion": "Bí ẩn, Cá tính, Đột phá",
    "stock": 135,
    "compatible_layouts": ["LAY-002", "LAY-008"],
    "attributes": {
      "material": "Decal nhựa PVC xuyên sáng mờ",
      "dimension": "Tấm 10 x 16 cm (Gồm 14 chi tiết)",
      "theme": "Dark Mode / Film Negative / Cyber",
      "color": "Đen Obsidian / Xám Khói / Neon Lime",
      "finish_3d": "Mặt bóng xuyên sáng nhẹ",
      "waterproof": True,
      "origin": "ScrapCraft Studio"
    },
    "tags": ["film 35mm", "dark mode", "cyber", "đen", "bí ẩn", "cá tính", "âm bản"],
    "ai_keywords": ["film", "dark mode", "cyber", "đen", "bí ẩn", "cá tính", "âm bản", "concert", "party", "night"]
  },

  # LAYOUTS (8 items)
  {
    "id": "LAY-001",
    "sku": "LAY-001",
    "type": "layout",
    "name": "Layout Khung Ảnh Polaroid Cài Giấy Cổ Điển",
    "category": "layout",
    "category_name": "Khung Ảnh & Bố Cục Tương Tác",
    "price": 45000,
    "original_price": 55000,
    "image": "/static/assets/layouts/lay_001.svg",
    "thumbnail": "/static/assets/layouts/lay_001.svg",
    "badge": "Best Seller Layout",
    "description": "Khung ảnh phong cách Polaroid khổ vuông kèm 4 góc cài giấy da bò tự nhiên và dòng kẻ viết lời nhắn tay ý nghĩa.",
    "photo_count": 1,
    "orientation": "vertical",
    "theme": "Polaroid / Vintage / Memory",
    "style": "Polaroid Classic",
    "occasion": "Ảnh chân dung, Du lịch, Kỷ niệm đôi",
    "color_palette": "Trắng Giấy Mỹ Thuật / Nâu Kraft",
    "compatible_stickers": ["STK-001", "STK-002", "STK-004", "STK-005", "STK-006", "STK-007", "STK-008", "STK-010"],
    "stock": 180,
    "attributes": {
      "material": "Giấy mỹ thuật bồi dày 350gsm + Góc cài giấy tự nhiên",
      "dimension": "10.5 x 13.5 cm (Vừa ảnh 7.5 x 7.5 cm)",
      "theme": "Polaroid / Vintage / Memory",
      "color": "Trắng Giấy Mỹ Thuật / Nâu Kraft",
      "finish_3d": "Góc cài giấy nổi 0.5mm chống rớt ảnh",
      "photo_capacity": "1 ảnh chính + 1 dòng note",
      "origin": "Gia công cắt bế chính xác tại Xưởng"
    },
    "tags": ["polaroid", "khung ảnh", "vintage", "cài giấy", "kỷ niệm", "đơn ảnh", "thủ công"],
    "ai_keywords": ["polaroid", "khung ảnh", "vintage", "kỷ niệm", "ảnh đơn", "lời nhắn", "kraft", "chân dung", "bạn thân"]
  },
  {
    "id": "LAY-002",
    "sku": "LAY-002",
    "type": "layout",
    "name": "Layout Dải Phim 35mm Filmstrip 3 Khung",
    "category": "layout",
    "category_name": "Khung Ảnh & Bố Cục Tương Tác",
    "price": 48000,
    "original_price": 60000,
    "image": "/static/assets/layouts/lay_002.svg",
    "thumbnail": "/static/assets/layouts/lay_002.svg",
    "badge": "Analog Vibe",
    "description": "Dải phim nhựa cổ điển với 3 ô ảnh nối tiếp kèm lỗ bánh răng phim chân thực, lý tưởng để kể câu chuyện hành trình theo dòng thời gian.",
    "photo_count": 3,
    "orientation": "horizontal",
    "theme": "35mm Film / Timeline / Storytelling",
    "style": "Filmstrip Analog",
    "occasion": "Chuyến đi phượt, Nhật ký hành trình, Ảnh liên hoàn hài hước",
    "color_palette": "Đen Film / Trắng / Xám Khói",
    "compatible_stickers": ["STK-003", "STK-005", "STK-008", "STK-009", "STK-012"],
    "stock": 140,
    "attributes": {
      "material": "Bìa cứng đen dập lỗ sprocket film chuẩn xác",
      "dimension": "7 x 22 cm (Gồm 3 khung ảnh 5 x 5 cm)",
      "theme": "35mm Film / Timeline / Storytelling",
      "color": "Đen Film / Trắng",
      "finish_3d": "Mặt giấy cán màng mờ chống trầy",
      "photo_capacity": "3 ảnh liên hoàn",
      "origin": "ScrapCraft Studio"
    },
    "tags": ["filmstrip", "dải phim", "35mm", "timeline", "du lịch", "hành trình", "3 ảnh"],
    "ai_keywords": ["filmstrip", "dải phim", "3 ảnh", "timeline", "film", "chuyến đi", "bạn thân", "roadtrip", "hài hước"]
  },
  {
    "id": "LAY-003",
    "sku": "LAY-003",
    "type": "layout",
    "name": "Layout Gấp Xếp Accordion 3D Mở Rộng 8 Khung",
    "category": "layout",
    "category_name": "Khung Ảnh & Bố Cục Tương Tác",
    "price": 65000,
    "original_price": 80000,
    "image": "/static/assets/layouts/lay_003.svg",
    "thumbnail": "/static/assets/layouts/lay_003.svg",
    "badge": "Pop-up 3D",
    "description": "Cấu trúc tương tác 3D dạng quạt xếp đàn Accordion buộc nơ ruy băng, khi kéo mở sẽ bung ra 8 khung ảnh bí mật chứa đầy bất ngờ.",
    "photo_count": 8,
    "orientation": "expandable",
    "theme": "Surprise / Accordion / Pop-up / Love",
    "style": "Interactive 3D Fold",
    "occasion": "Quà sinh nhật bất ngờ, Kỷ niệm yêu nhau, Tặng bạn thân",
    "color_palette": "Hồng Pastel / Tím Mộng Mơ / Trắng Sữa",
    "compatible_stickers": ["STK-001", "STK-004", "STK-006", "STK-007"],
    "stock": 95,
    "attributes": {
      "material": "Giấy Pastel mỹ thuật gập cấn đa tầng + Nơ ruy băng lụa",
      "dimension": "Gấp lại 9 x 12 cm (Mở rộng dài 48 cm)",
      "theme": "Surprise / Accordion / Pop-up",
      "color": "Hồng Pastel / Tím Mộng Mơ",
      "finish_3d": "Cấu trúc xếp lớp gập 3D tương tác tay",
      "photo_capacity": "8 ảnh cỡ 5 x 7 cm",
      "origin": "Nghệ nhân gập thủ công từng nếp"
    },
    "tags": ["accordion", "gấp quạt", "popup 3d", "8 ảnh", "bất ngờ", "tình yêu", "sinh nhật"],
    "ai_keywords": ["accordion", "popup", "3d", "nhiều ảnh", "8 ảnh", "bất ngờ", "sinh nhật", "tình yêu", "quà tặng", "gấp xếp"]
  },
  {
    "id": "LAY-004",
    "sku": "LAY-004",
    "type": "layout",
    "name": "Layout Phong Bì Túi Bí Mật Kèm Thẻ Tag",
    "category": "layout",
    "category_name": "Khung Ảnh & Bố Cục Tương Tác",
    "price": 42000,
    "original_price": 52000,
    "image": "/static/assets/layouts/lay_004.svg",
    "thumbnail": "/static/assets/layouts/lay_004.svg",
    "badge": "Secret Pocket",
    "description": "Túi phong bì giấy Kraft buộc dây nút cúc cổ điển, bên trong chứa 2 thẻ tag rút có thể kẹp ảnh mini hoặc viết những tâm tư bí mật.",
    "photo_count": 2,
    "orientation": "vertical",
    "theme": "Secret Pocket / Letter / Kraft Vintage",
    "style": "Secret Envelope",
    "occasion": "Thư gửi tương lai, Lời chúc giấu kín, Lưu giữ vé xem phim",
    "color_palette": "Nâu Kraft / Vàng Bơ / Dây Đay",
    "compatible_stickers": ["STK-002", "STK-005", "STK-009", "STK-010", "STK-011"],
    "stock": 160,
    "attributes": {
      "material": "Giấy Kraft nâu Nhật 280gsm + Nút cúc gỗ & Dây cói",
      "dimension": "11 x 14 cm (Kèm 2 thẻ tag rút)",
      "theme": "Secret Pocket / Letter / Kraft",
      "color": "Nâu Kraft / Vàng Bơ",
      "finish_3d": "Túi đựng có độ phồng 3D chứa được 5-10 kỷ vật",
      "photo_capacity": "2 ảnh thẻ tag + Vé xem phim/kỷ vật",
      "origin": "ScrapCraft Studio"
    },
    "tags": ["túi bí mật", "phong bì", "kraft", "thẻ tag", "thư tay", "kỷ vật", "vintage"],
    "ai_keywords": ["túi bí mật", "phong bì", "kraft", "thư tay", "lời chúc", "vé máy bay", "kỷ vật", "vintage", "giấu kín"]
  },
  {
    "id": "LAY-005",
    "sku": "LAY-005",
    "type": "layout",
    "name": "Layout Mosaic Collage Ghép Đa Khung Hình",
    "category": "layout",
    "category_name": "Khung Ảnh & Bố Cục Tương Tác",
    "price": 52000,
    "original_price": 65000,
    "image": "/static/assets/layouts/lay_005.svg",
    "thumbnail": "/static/assets/layouts/lay_005.svg",
    "badge": "Group Photo Favorite",
    "description": "Bố cục ghép hình hiện đại gồm 1 ô ảnh chính góc rộng và 3 ô ảnh khoảnh khắc phụ, tối ưu để lưu giữ ảnh tập thể và hội bạn bè.",
    "photo_count": 4,
    "orientation": "horizontal",
    "theme": "Mosaic Collage / Friendship / Classmate",
    "style": "Modern Collage Grid",
    "occasion": "Kỷ yếu nhóm bạn, Tiệc sinh nhật đông người, Team building",
    "color_palette": "Trắng Sữa / Cam Pastel / Xanh Mint",
    "compatible_stickers": ["STK-001", "STK-003", "STK-007", "STK-009"],
    "stock": 115,
    "attributes": {
      "material": "Bìa mỹ thuật bồi nhiều tầng viền nổi",
      "dimension": "14 x 18 cm (Gồm 4 khung ảnh phối màu)",
      "theme": "Mosaic Collage / Friendship / Classmate",
      "color": "Trắng / Cam Pastel / Xanh Mint",
      "finish_3d": "Viền khung ảnh nổi 0.8mm",
      "photo_capacity": "4 ảnh kích thước so le",
      "origin": "ScrapCraft Studio"
    },
    "tags": ["mosaic", "collage", "ghép ảnh", "hội bạn", "kỷ yếu", "tập thể", "4 ảnh"],
    "ai_keywords": ["ghép ảnh", "mosaic", "collage", "4 ảnh", "bạn thân", "nhóm bạn", "kỷ yếu", "tập thể", "sinh nhật", "lớp"]
  },
  {
    "id": "LAY-006",
    "sku": "LAY-006",
    "type": "layout",
    "name": "Layout Thác Nước Waterfall Kéo Trượt Tự Động",
    "category": "layout",
    "category_name": "Khung Ảnh & Bố Cục Tương Tác",
    "price": 68000,
    "original_price": 85000,
    "image": "/static/assets/layouts/lay_006.svg",
    "thumbnail": "/static/assets/layouts/lay_006.svg",
    "badge": "Interactive Mechanism",
    "description": "Hiệu ứng cơ học độc đáo: khi kéo nhẹ dải ruy băng ở dưới, các tấm ảnh sẽ tự động lật liên hoàn như dòng thác nước chuyển động mượt mà.",
    "photo_count": 5,
    "orientation": "vertical",
    "theme": "Waterfall Slider / Motion / Magic Fold",
    "style": "Mechanical Slider 3D",
    "occasion": "Kỷ niệm theo từng năm, Quá trình trưởng thành, Du lịch nhiều chặng",
    "color_palette": "Xanh Dương Pastel / Trắng / Xanh Cobalt",
    "compatible_stickers": ["STK-001", "STK-006", "STK-008", "STK-011"],
    "stock": 70,
    "attributes": {
      "material": "Bộ ray trượt cơ học bằng bìa cứng chống kẹt + Ruy băng kéo",
      "dimension": "10 x 18 cm (Lật tuần tự 5 ảnh)",
      "theme": "Waterfall Slider / Motion",
      "color": "Xanh Dương / Trắng / Cobalt",
      "finish_3d": "Chuyển động lật tầng cơ học 3D",
      "photo_capacity": "5 ảnh kích thước 6 x 8 cm",
      "origin": "Gia công lắp ráp tỉ mỉ tại Xưởng"
    },
    "tags": ["thác nước", "waterfall", "kéo trượt", "lật ảnh", "chuyển động", "5 ảnh", "độc đáo"],
    "ai_keywords": ["thác nước", "waterfall", "lật ảnh", "kéo trượt", "tương tác", "chuyển động", "timeline", "5 ảnh", "quà tặng"]
  },
  {
    "id": "LAY-007",
    "sku": "LAY-007",
    "type": "layout",
    "name": "Layout Khung Tròn Vòng Nguyệt Quế Vintage",
    "category": "layout",
    "category_name": "Khung Ảnh & Bố Cục Tương Tác",
    "price": 46000,
    "original_price": 58000,
    "image": "/static/assets/layouts/lay_007.svg",
    "thumbnail": "/static/assets/layouts/lay_007.svg",
    "badge": "Botanical Wreath",
    "description": "Khung ảnh hình tròn viền hoa lá dập nổi tinh xảo, mang lại cảm giác mềm mại như một chiếc gương cổ điển trang trí trên mặt trang sổ.",
    "photo_count": 1,
    "orientation": "circular",
    "theme": "Wreath / Botanical / Vintage Portrait",
    "style": "Vintage Circular Frame",
    "occasion": "Ảnh chân dung cô gái, Ảnh hoa cỏ, Kỷ niệm nhẹ nhàng",
    "color_palette": "Vàng Kem / Nâu Đất / Xanh Lá Mạ",
    "compatible_stickers": ["STK-002", "STK-006", "STK-010", "STK-011"],
    "stock": 130,
    "attributes": {
      "material": "Giấy mỹ thuật dập nổi hoa văn vòng lá 3D",
      "dimension": "Đường kính 14 cm (Vừa ảnh tròn 9 cm)",
      "theme": "Wreath / Botanical / Vintage Portrait",
      "color": "Vàng Kem / Nâu Đất / Xanh Lá",
      "finish_3d": "Dập nổi viền vòng nguyệt quế 0.6mm",
      "photo_capacity": "1 ảnh tròn chân dung",
      "origin": "ScrapCraft Studio"
    },
    "tags": ["khung tròn", "nguyệt quế", "botanical", "chân dung", "vintage", "hoa lá", "nhẹ nhàng"],
    "ai_keywords": ["khung tròn", "nguyệt quế", "vintage", "chân dung", "hoa cỏ", "nhẹ nhàng", "lãng mạn", "nữ tính"]
  },
  {
    "id": "LAY-008",
    "sku": "LAY-008",
    "type": "layout",
    "name": "Layout Tổ Ong Hexagon Cyber Vibe",
    "category": "layout",
    "category_name": "Khung Ảnh & Bố Cục Tương Tác",
    "price": 55000,
    "original_price": 70000,
    "image": "/static/assets/layouts/lay_008.svg",
    "thumbnail": "/static/assets/layouts/lay_008.svg",
    "badge": "Cyberpunk Hex",
    "description": "Thiết kế bố cục hình học lục giác tổ ong phá cách với viền màu neon Cyberpunk nổi bật trên nền đen, đậm chất Gen Z Futuristic.",
    "photo_count": 3,
    "orientation": "geometric",
    "theme": "Cyberpunk / Hexagon / Futuristic / Neon",
    "style": "Futuristic Cyber Geometric",
    "occasion": "Ảnh đi quẩy đêm, Lễ hội âm nhạc EDM, Gaming memory",
    "color_palette": "Đen Huyền / Hồng Neon / Tím Cyber / Xanh Cyan",
    "compatible_stickers": ["STK-001", "STK-003", "STK-012"],
    "stock": 90,
    "attributes": {
      "material": "Bìa đen matte dập ép nhũ màng neon phản quang",
      "dimension": "15 x 18 cm (Gồm 3 khung lục giác 7 cm)",
      "theme": "Cyberpunk / Hexagon / Futuristic",
      "color": "Đen Huyền / Hồng Neon / Tím Cyber",
      "finish_3d": "Cắt vát góc cạnh sắc sảo 3D",
      "photo_capacity": "3 ảnh lục giác cá tính",
      "origin": "ScrapCraft Studio"
    },
    "tags": ["lục giác", "hexagon", "cyberpunk", "neon", "gen z", "phá cách", "3 ảnh"],
    "ai_keywords": ["lục giác", "hexagon", "cyberpunk", "neon", "edm", "gaming", "quẩy", "genz", "cá tính", "đen"]
  },

  # SCRAPBOOKS (4 items)
  {
    "id": "SCR-001",
    "sku": "SCR-001",
    "type": "scrapbook",
    "name": "Sổ Scrapbook Bìa Còng Kraft Tự Nhiên",
    "category": "scrapbook",
    "category_name": "Sổ Scrapbook Thủ Công",
    "price": 195000,
    "original_price": 250000,
    "image": "/static/assets/books/scr_001.svg",
    "thumbnail": "/static/assets/books/scr_001.svg",
    "badge": "Best Seller Album",
    "description": "Cuốn sổ kinh điển cho tín đồ handmade với bìa carton Kraft bồi cứng cáp, gáy còng sắt mở đóng linh hoạt giúp dễ dàng thêm bớt trang trí.",
    "pages": 30,
    "cover_material": "Bìa Carton Kraft bồi dày 1800gsm + Còng kim loại không gỉ mạ đồng",
    "dimension": "Khổ vuông 21 x 21 cm (Chứa được 60 - 80 bức ảnh)",
    "color": "Nâu Kraft Tự Nhiên",
    "style": "Vintage Kraft Minimalist",
    "theme": "Vintage / Du lịch / Kỷ niệm gia đình",
    "stock": 100,
    "attributes": {
      "material": "Bìa Carton Kraft bồi dày 1800gsm + Còng kim loại không gỉ mạ đồng",
      "dimension": "Khổ vuông 21 x 21 cm (Chứa được 60 - 80 bức ảnh)",
      "pages": "30 tờ giấy Kraft đen/nâu đan xen dày 300gsm Acid-Free",
      "binding": "Gáy còng sắt 3 khoen mở đóng linh hoạt",
      "weight": "650g",
      "origin": "Đóng gáy thủ công tại Xưởng ScrapCraft"
    },
    "tags": ["sổ scrapbook", "bìa còng", "kraft", "vintage", "handmade", "album ảnh", "30 trang"],
    "ai_keywords": ["sổ", "scrapbook", "bìa còng", "kraft", "vintage", "album", "thủ công", "kỷ niệm", "du lịch", "gia đình"]
  },
  {
    "id": "SCR-002",
    "sku": "SCR-002",
    "type": "scrapbook",
    "name": "Sổ Scrapbook Bìa Da Mềm Pastel Hologram",
    "category": "scrapbook",
    "category_name": "Sổ Scrapbook Thủ Công",
    "price": 235000,
    "original_price": 295000,
    "image": "/static/assets/books/scr_002.svg",
    "thumbnail": "/static/assets/books/scr_002.svg",
    "badge": "Gen Z Signature Album",
    "description": "Phiên bản sổ bìa da PU cao cấp bọc màng Hologram 7 màu lấp lánh chống nước tuyệt đối, ruột giấy mỹ thuật Pastel ngập tràn cảm hứng.",
    "pages": 40,
    "cover_material": "Da PU mềm phủ màng Laser Hologram cầu vồng chống thấm",
    "dimension": "Khổ A5 (16 x 23 cm)",
    "color": "Pastel Hologram / Tím Hồng Ánh Kim",
    "style": "Y2K Dreamy Hologram",
    "theme": "Y2K / Tình bạn / Tình yêu / Thanh xuân",
    "stock": 75,
    "attributes": {
      "material": "Da PU mềm phủ màng Laser Hologram cầu vồng chống thấm",
      "dimension": "Khổ A5 (16 x 23 cm)",
      "pages": "40 tờ giấy mỹ thuật Pastel 250gsm dập viền chỉ may",
      "binding": "Khâu chỉ thủ công mở phẳng 180 độ",
      "weight": "580g",
      "origin": "ScrapCraft Studio"
    },
    "tags": ["sổ da mềm", "pastel", "hologram", "y2k", "tình yêu", "bạn thân", "40 trang"],
    "ai_keywords": ["sổ da", "hologram", "pastel", "y2k", "lấp lánh", "tình bạn", "tình yêu", "crush", "thanh xuân"]
  },
  {
    "id": "SCR-003",
    "sku": "SCR-003",
    "type": "scrapbook",
    "name": "Sổ Scrapbook Bìa Cứng Dark Academia & Film",
    "category": "scrapbook",
    "category_name": "Sổ Scrapbook Thủ Công",
    "price": 215000,
    "original_price": 270000,
    "image": "/static/assets/books/scr_003.svg",
    "thumbnail": "/static/assets/books/scr_003.svg",
    "badge": "Dark Academia Edit",
    "description": "Thiết kế bìa cứng đen mờ tuyền dập nổi họa tiết góc viền sắc sảo, ruột toàn bộ bằng giấy đen mỹ thuật Black Cardstock giúp nổi bật ảnh film.",
    "pages": 35,
    "cover_material": "Bìa cứng ép màng đen mờ chống xước dập kim loại",
    "dimension": "Khổ vuông 22 x 22 cm",
    "color": "Đen Obsidian",
    "style": "Dark Academia / Film Analog",
    "theme": "Film 35mm / Roadtrip / Nghệ thuật / Kỷ yếu",
    "stock": 80,
    "attributes": {
      "material": "Bìa cứng ép màng đen mờ chống xước dập kim loại",
      "dimension": "Khổ vuông 22 x 22 cm",
      "pages": "35 tờ giấy Black Cardstock 350gsm cực dày chống cong",
      "binding": "Gáy lò xo ẩn bọc vải Canvas cao cấp",
      "weight": "720g",
      "origin": "ScrapCraft Studio"
    },
    "tags": ["sổ bìa đen", "dark academia", "giấy đen", "ảnh film", "35mm", "nghệ thuật", "35 trang"],
    "ai_keywords": ["sổ đen", "dark mode", "dark academia", "film", "analog", "chụp ảnh", "nghệ thuật", "cá tính", "bí ẩn"]
  },
  {
    "id": "SCR-004",
    "sku": "SCR-004",
    "type": "scrapbook",
    "name": "Sổ Scrapbook Bìa Vải Linen Cửa Sổ Khung Ảnh",
    "category": "scrapbook",
    "category_name": "Sổ Scrapbook Thủ Công",
    "price": 250000,
    "original_price": 320000,
    "image": "/static/assets/books/scr_004.svg",
    "thumbnail": "/static/assets/books/scr_004.svg",
    "badge": "Premium Linen",
    "description": "Dòng sổ thủ công cao cấp bọc vải Linen dệt thô mộc tự nhiên, mặt bìa khoét ô cửa sổ lồng ảnh đại diện trang trọng và thanh lịch.",
    "pages": 30,
    "cover_material": "Vải dệt Linen cao cấp bọc bìa carton xám ép khuôn",
    "dimension": "Khổ 24 x 24 cm",
    "color": "Xám Tro Mộc (Natural Linen)",
    "style": "Editorial Minimalist Linen",
    "theme": "Gia đình / Đám cưới / Kỷ niệm 10 năm / Quà tặng cao cấp",
    "stock": 60,
    "attributes": {
      "material": "Vải dệt Linen cao cấp bọc bìa carton xám ép khuôn",
      "dimension": "Khổ 24 x 24 cm (Cửa sổ bìa 9 x 9 cm)",
      "pages": "30 tờ giấy mỹ thuật trắng ngà Ivory 300gsm kèm giấy nến bảo vệ",
      "binding": "Đóng gáy chỉ may thủ công phẳng 180 độ",
      "weight": "850g",
      "origin": "Nghệ nhân may bọc vải thủ công cao cấp"
    },
    "tags": ["sổ vải linen", "cửa sổ ảnh", "cao cấp", "đám cưới", "gia đình", "quà tặng", "30 trang"],
    "ai_keywords": ["sổ vải", "linen", "cửa sổ", "sang trọng", "đám cưới", "gia đình", "kỷ niệm", "tối giản", "quà tặng"]
  }
]

with open(os.path.join(DATA_DIR, 'products.json'), 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

# 2. INSPIRATIONS DATA (STRICTLY VALID SKUs ONLY)
inspirations = [
  {
    "id": "insp-001",
    "title": "Chuyến Đi Đà Lạt Mộng Mơ (Vintage Botanical)",
    "concept": "Vintage Botanical Dalat",
    "subtitle": "Bố cục hoài niệm phong cách Cottagecore kết hợp khung Polaroid và hoa khô",
    "image": "/static/assets/layouts/insp_001.svg",
    "theme": "Du lịch / Hoài niệm / Vintage",
    "difficulty": "Dễ làm (15 phút)",
    "book_sku": "SCR-001",
    "layout_skus": ["LAY-001", "LAY-004"],
    "sticker_skus": ["STK-002", "STK-005", "STK-008"],
    "components": [
      {"sku": "SCR-001", "name": "Sổ Scrapbook Bìa Còng Kraft Tự Nhiên", "qty": 1, "category": "scrapbook", "price": 195000},
      {"sku": "LAY-001", "name": "Layout Khung Ảnh Polaroid Cài Giấy Cổ Điển", "qty": 2, "category": "layout", "price": 45000},
      {"sku": "LAY-004", "name": "Layout Phong Bì Túi Bí Mật Kèm Thẻ Tag", "qty": 1, "category": "layout", "price": 42000},
      {"sku": "STK-002", "name": "Sticker Giấy Kraft Vintage Botanical Florals", "qty": 2, "category": "sticker", "price": 32000},
      {"sku": "STK-005", "name": "Sticker 3D Băng Cassette & Máy Ảnh Ép Kim Vàng", "qty": 1, "category": "sticker", "price": 42000}
    ],
    "description": "Mẫu thiết kế lấy cảm hứng từ những đồi thông mờ sương và quán cà phê gỗ cổ điển tại Đà Lạt. Sử dụng nền giấy Kraft tự nhiên kết hợp khung ảnh Polaroid đơn và nhãn dán hoa lá ép khô, điểm xuyết một chiếc máy ảnh film dập nhũ vàng tạo điểm nhấn thị giác ấm cúng.",
    "canvas_preset": {
      "bg_color": "#e8d8c3",
      "items": [
        {"sku": "LAY-001", "type": "layout", "image": "/static/assets/layouts/lay_001.svg", "name": "Layout Khung Polaroid", "left": 130, "top": 140, "angle": -5, "scale": 0.85, "zIndex": 1},
        {"sku": "LAY-001", "type": "layout", "image": "/static/assets/layouts/lay_001.svg", "name": "Layout Khung Polaroid", "left": 340, "top": 200, "angle": 6, "scale": 0.85, "zIndex": 2},
        {"sku": "LAY-004", "type": "layout", "image": "/static/assets/layouts/lay_004.svg", "name": "Túi Bí Mật", "left": 140, "top": 410, "angle": 0, "scale": 0.75, "zIndex": 3},
        {"sku": "STK-002", "type": "sticker", "image": "/static/assets/stickers/stk_002.svg", "name": "Sticker Hoa Lá", "left": 80, "top": 80, "angle": -15, "scale": 0.7, "zIndex": 10},
        {"sku": "STK-002", "type": "sticker", "image": "/static/assets/stickers/stk_002.svg", "name": "Sticker Hoa Lá", "left": 430, "top": 390, "angle": 20, "scale": 0.75, "zIndex": 11},
        {"sku": "STK-005", "type": "sticker", "image": "/static/assets/stickers/stk_005.svg", "name": "Sticker Cassette 3D", "left": 350, "top": 90, "angle": 10, "scale": 0.75, "zIndex": 12}
      ]
    },
    "bundle_price": 388000,
    "original_price": 433000
  },
  {
    "id": "insp-002",
    "title": "Hội Bạn Thân Siêu Quậy (Gen Z Y2K Slang)",
    "concept": "Y2K Friendship Vibes",
    "subtitle": "Phong cách Cyberpunk neon kết hợp sticker thạch 3D và khung ảnh ghép đa giác",
    "image": "/static/assets/layouts/insp_002.svg",
    "theme": "Gen Z / Bạn Thân / Y2K Cyber",
    "difficulty": "Trung bình (25 phút)",
    "book_sku": "SCR-002",
    "layout_skus": ["LAY-005", "LAY-008"],
    "sticker_skus": ["STK-001", "STK-003", "STK-004"],
    "components": [
      {"sku": "SCR-002", "name": "Sổ Scrapbook Bìa Da Mềm Pastel Hologram", "qty": 1, "category": "scrapbook", "price": 235000},
      {"sku": "LAY-005", "name": "Layout Mosaic Collage Ghép Đa Khung Hình", "qty": 1, "category": "layout", "price": 52000},
      {"sku": "LAY-008", "name": "Layout Tổ Ong Hexagon Cyber Vibe", "qty": 1, "category": "layout", "price": 55000},
      {"sku": "STK-001", "name": "Sticker 3D Hologram Y2K Sparkle Stars", "qty": 2, "category": "sticker", "price": 35000},
      {"sku": "STK-003", "name": "Sticker 3D Doodle Emoji & Gen Z Slang", "qty": 2, "category": "sticker", "price": 38000}
    ],
    "description": "Bùng nổ cá tính cùng bảng màu Neon Cyber kết hợp nền sổ Pastel Hologram. Sử dụng sticker thạch 3D dập nổi biểu cảm lầy lội và layout lục giác phá cách để lưu giữ khoảnh khắc thanh xuân không giới hạn.",
    "canvas_preset": {
      "bg_color": "#f3e8ff",
      "items": [
        {"sku": "LAY-005", "type": "layout", "image": "/static/assets/layouts/lay_005.svg", "name": "Layout Mosaic", "left": 180, "top": 160, "angle": -4, "scale": 0.8, "zIndex": 1},
        {"sku": "LAY-008", "type": "layout", "image": "/static/assets/layouts/lay_008.svg", "name": "Layout Hexagon Cyber", "left": 360, "top": 360, "angle": 5, "scale": 0.75, "zIndex": 2},
        {"sku": "STK-001", "type": "sticker", "image": "/static/assets/stickers/stk_001.svg", "name": "Sticker Sao 3D", "left": 100, "top": 90, "angle": 15, "scale": 0.7, "zIndex": 10},
        {"sku": "STK-003", "type": "sticker", "image": "/static/assets/stickers/stk_003.svg", "name": "Sticker Slay Vibes", "left": 440, "top": 140, "angle": -12, "scale": 0.75, "zIndex": 11},
        {"sku": "STK-004", "type": "sticker", "image": "/static/assets/stickers/stk_004.svg", "name": "Washi Caro", "left": 260, "top": 450, "angle": 0, "scale": 0.85, "zIndex": 12}
      ]
    },
    "bundle_price": 448000,
    "original_price": 488000
  },
  {
    "id": "insp-003",
    "title": "Chuyến Phượt Đêm & Film 35mm (Dark Academia)",
    "concept": "Dark Academia Roadtrip",
    "subtitle": "Trang sổ nền đen tuyền sang trọng tôn vinh dải phim nhựa và máy ảnh cổ điển",
    "image": "/static/assets/layouts/insp_003.svg",
    "theme": "Dark Mode / Film 35mm / Roadtrip",
    "difficulty": "Dễ làm (15 phút)",
    "book_sku": "SCR-003",
    "layout_skus": ["LAY-002", "LAY-004"],
    "sticker_skus": ["STK-005", "STK-008", "STK-012"],
    "components": [
      {"sku": "SCR-003", "name": "Sổ Scrapbook Bìa Cứng Dark Academia & Film", "qty": 1, "category": "scrapbook", "price": 215000},
      {"sku": "LAY-002", "name": "Layout Dải Phim 35mm Filmstrip 3 Khung", "qty": 2, "category": "layout", "price": 48000},
      {"sku": "STK-008", "name": "Sticker Máy Ảnh Film 35mm Analog Shot 3D", "qty": 1, "category": "sticker", "price": 37000},
      {"sku": "STK-005", "name": "Sticker 3D Băng Cassette Ép Nhũ Vàng", "qty": 1, "category": "sticker", "price": 42000},
      {"sku": "STK-012", "name": "Sticker Khung Film 35mm Âm Bản Cyber Dark", "qty": 1, "category": "sticker", "price": 33000}
    ],
    "description": "Dành riêng cho những người đam mê nhiếp ảnh analog. Bố cục dải phim 35mm trải dài trên nền giấy đen mỹ thuật cao cấp, kết hợp sticker máy ảnh film nổi 3D và cassette dập nhũ vàng kim cổ điển.",
    "canvas_preset": {
      "bg_color": "#18181b",
      "items": [
        {"sku": "LAY-002", "type": "layout", "image": "/static/assets/layouts/lay_002.svg", "name": "Dải Phim 35mm", "left": 300, "top": 160, "angle": -3, "scale": 0.85, "zIndex": 1},
        {"sku": "LAY-002", "type": "layout", "image": "/static/assets/layouts/lay_002.svg", "name": "Dải Phim 35mm", "left": 300, "top": 360, "angle": 3, "scale": 0.85, "zIndex": 2},
        {"sku": "STK-008", "type": "sticker", "image": "/static/assets/stickers/stk_008.svg", "name": "Máy Ảnh Film 3D", "left": 110, "top": 120, "angle": -15, "scale": 0.75, "zIndex": 10},
        {"sku": "STK-005", "type": "sticker", "image": "/static/assets/stickers/stk_005.svg", "name": "Cassette Nhũ Vàng", "left": 480, "top": 420, "angle": 12, "scale": 0.75, "zIndex": 11},
        {"sku": "STK-012", "type": "sticker", "image": "/static/assets/stickers/stk_012.svg", "name": "Khung Film Âm Bản", "left": 100, "top": 420, "angle": 8, "scale": 0.7, "zIndex": 12}
      ]
    },
    "bundle_price": 389000,
    "original_price": 423000
  },
  {
    "id": "insp-004",
    "title": "365 Ngày Yêu Nhau (Romantic Anniversary)",
    "concept": "Love Story Anniversary",
    "subtitle": "Cấu trúc Accordion mở rộng kết hợp trái tim nhũ bạc và con dấu sáp hoàng gia",
    "image": "/static/assets/layouts/insp_004.svg",
    "theme": "Tình Yêu / Kỷ Niệm / Lãng Mạn",
    "difficulty": "Nâng cao (35 phút)",
    "book_sku": "SCR-002",
    "layout_skus": ["LAY-003", "LAY-007"],
    "sticker_skus": ["STK-006", "STK-010"],
    "components": [
      {"sku": "SCR-002", "name": "Sổ Scrapbook Bìa Da Mềm Pastel Hologram", "qty": 1, "category": "scrapbook", "price": 235000},
      {"sku": "LAY-003", "name": "Layout Gấp Xếp Accordion 3D Mở Rộng", "qty": 1, "category": "layout", "price": 65000},
      {"sku": "LAY-007", "name": "Layout Khung Tròn Vòng Nguyệt Quế", "qty": 1, "category": "layout", "price": 46000},
      {"sku": "STK-006", "name": "Sticker 3D Trái Tim Bạc Hologram", "qty": 2, "category": "sticker", "price": 36000},
      {"sku": "STK-010", "name": "Con Dấu Sáp Niêm Phong Wax Seal 3D", "qty": 1, "category": "sticker", "price": 45000}
    ],
    "description": "Món quà kỷ niệm tình yêu hoàn hảo với cấu trúc mở bung 8 ô ảnh bí mật dạng đàn Accordion. Điểm xuyết những trái tim nhũ bạc 3D lấp lánh và con dấu sáp hoàng gia đỏ rượu quý phái.",
    "canvas_preset": {
      "bg_color": "#fff1f2",
      "items": [
        {"sku": "LAY-003", "type": "layout", "image": "/static/assets/layouts/lay_003.svg", "name": "Layout Accordion 3D", "left": 220, "top": 200, "angle": 0, "scale": 0.85, "zIndex": 1},
        {"sku": "LAY-007", "type": "layout", "image": "/static/assets/layouts/lay_007.svg", "name": "Khung Tròn Nguyệt Quế", "left": 410, "top": 360, "angle": 8, "scale": 0.75, "zIndex": 2},
        {"sku": "STK-006", "type": "sticker", "image": "/static/assets/stickers/stk_006.svg", "name": "Trái Tim Bạc 3D", "left": 100, "top": 100, "angle": -18, "scale": 0.75, "zIndex": 10},
        {"sku": "STK-010", "type": "sticker", "image": "/static/assets/stickers/stk_010.svg", "name": "Con Dấu Sáp 3D", "left": 360, "top": 90, "angle": 10, "scale": 0.75, "zIndex": 11}
      ]
    },
    "bundle_price": 427000,
    "original_price": 463000
  },
  {
    "id": "insp-005",
    "title": "Thanh Xuân Rực Rỡ Kỷ Yếu 2026 (Graduation Memory)",
    "concept": "Graduation Milestone",
    "subtitle": "Lưu giữ chặng đường đại học cùng mũ cử nhân viền vàng và khung ảnh tập thể",
    "image": "/static/assets/layouts/insp_005.svg",
    "theme": "Tốt Nghiệp / Kỷ Yếu / Bạn Bè",
    "difficulty": "Trung bình (20 phút)",
    "book_sku": "SCR-001",
    "layout_skus": ["LAY-001", "LAY-005"],
    "sticker_skus": ["STK-007", "STK-009"],
    "components": [
      {"sku": "SCR-001", "name": "Sổ Scrapbook Bìa Còng Kraft Tự Nhiên", "qty": 1, "category": "scrapbook", "price": 195000},
      {"sku": "LAY-005", "name": "Layout Mosaic Collage Ghép Đa Khung Hình", "qty": 1, "category": "layout", "price": 52000},
      {"sku": "LAY-001", "name": "Layout Khung Ảnh Polaroid Cài Giấy", "qty": 2, "category": "layout", "price": 45000},
      {"sku": "STK-007", "name": "Sticker 3D Mũ Cử Nhân & Ruy Băng", "qty": 2, "category": "sticker", "price": 39000},
      {"sku": "STK-009", "name": "Con Dấu Thị Thực Passport & Airmail", "qty": 1, "category": "sticker", "price": 29000}
    ],
    "description": "Lưu trọn nụ cười ngày tốt nghiệp với layout ghép ảnh Mosaic đa khung hình cho ảnh cả lớp, kết hợp mũ cử nhân 3D nhũ vàng và tem thư chắp cánh tương lai.",
    "canvas_preset": {
      "bg_color": "#f0fdf4",
      "items": [
        {"sku": "LAY-005", "type": "layout", "image": "/static/assets/layouts/lay_005.svg", "name": "Mosaic Tập Thể", "left": 230, "top": 180, "angle": 0, "scale": 0.8, "zIndex": 1},
        {"sku": "LAY-001", "type": "layout", "image": "/static/assets/layouts/lay_001.svg", "name": "Polaroid Cử Nhân", "left": 410, "top": 360, "angle": 6, "scale": 0.8, "zIndex": 2},
        {"sku": "STK-007", "type": "sticker", "image": "/static/assets/stickers/stk_007.svg", "name": "Mũ Cử Nhân 3D", "left": 100, "top": 100, "angle": -12, "scale": 0.8, "zIndex": 10},
        {"sku": "STK-009", "type": "sticker", "image": "/static/assets/stickers/stk_009.svg", "name": "Tem Thư Passport", "left": 450, "top": 120, "angle": 15, "scale": 0.7, "zIndex": 11}
      ]
    },
    "bundle_price": 399000,
    "original_price": 444000
  },
  {
    "id": "insp-006",
    "title": "Nhật Ký Quán Cà Phê Cuối Tuần (Cozy Daily Journal)",
    "concept": "Cozy Daily Coffee",
    "subtitle": "Phong cách tối giản nhẹ nhàng cùng cốc cà phê bốc khói và túi đựng hóa đơn kỷ vật",
    "image": "/static/assets/layouts/insp_006.svg",
    "theme": "Cozy Life / Nhật Ký / Thư Thái",
    "difficulty": "Dễ làm (10 phút)",
    "book_sku": "SCR-004",
    "layout_skus": ["LAY-001", "LAY-004"],
    "sticker_skus": ["STK-004", "STK-011"],
    "components": [
      {"sku": "SCR-004", "name": "Sổ Scrapbook Bìa Vải Linen Cửa Sổ Khung Ảnh", "qty": 1, "category": "scrapbook", "price": 250000},
      {"sku": "LAY-001", "name": "Layout Khung Ảnh Polaroid Cài Giấy", "qty": 1, "category": "layout", "price": 45000},
      {"sku": "LAY-004", "name": "Layout Phong Bì Túi Bí Mật Kèm Thẻ Tag", "qty": 1, "category": "layout", "price": 42000},
      {"sku": "STK-011", "name": "Sticker Cốc Cà Phê & Châm Ngôn Cozy", "qty": 2, "category": "sticker", "price": 30000},
      {"sku": "STK-004", "name": "Băng Dính Washi Tape Pastel Grid", "qty": 1, "category": "sticker", "price": 28000}
    ],
    "description": "Ghi lại những buổi chiều thảnh thơi nhâm nhi cà phê, đọc sách và viết lách. Bìa vải Linen thô mộc kết hợp túi đựng cuống vé xem phim và nhãn dán tách cà phê ấm áp.",
    "canvas_preset": {
      "bg_color": "#fefce8",
      "items": [
        {"sku": "LAY-001", "type": "layout", "image": "/static/assets/layouts/lay_001.svg", "name": "Polaroid Cafe", "left": 160, "top": 180, "angle": -4, "scale": 0.8, "zIndex": 1},
        {"sku": "LAY-004", "type": "layout", "image": "/static/assets/layouts/lay_004.svg", "name": "Túi Kỷ Vật", "left": 370, "top": 330, "angle": 5, "scale": 0.75, "zIndex": 2},
        {"sku": "STK-011", "type": "sticker", "image": "/static/assets/stickers/stk_011.svg", "name": "Sticker Cà Phê", "left": 360, "top": 120, "angle": 10, "scale": 0.75, "zIndex": 10},
        {"sku": "STK-004", "type": "sticker", "image": "/static/assets/stickers/stk_004.svg", "name": "Washi Tape", "left": 140, "top": 420, "angle": -2, "scale": 0.8, "zIndex": 11}
      ]
    },
    "bundle_price": 395000,
    "original_price": 425000
  }
]

with open(os.path.join(DATA_DIR, 'inspirations.json'), 'w', encoding='utf-8') as f:
    json.dump(inspirations, f, ensure_ascii=False, indent=2)

# 3. BLOGS DATA (8 SEO ARTICLES)
blogs = [
  {
    "id": "blog-001",
    "slug": "huong-dan-layering-sticker-3d-chieu-sau-scrapbook",
    "title": "Nghệ Thuật Layering Sticker 3D: Bí Quyết Tạo Chiều Sâu Đa Tầng Cho Cuốn Scrapbook",
    "excerpt": "Khám phá kỹ thuật xếp lớp (layering) kết hợp giữa Sticker Hologram 3D, Washi tape và khung Polaroid giúp trang sổ sống động như tác phẩm triển lãm.",
    "cover_image": "/static/assets/layouts/insp_002.svg",
    "thumbnail": "/static/assets/layouts/insp_002.svg",
    "author": "ScrapCraft Creative Team",
    "published_date": "2026-08-20",
    "read_time": "6 phút đọc",
    "category": "Kỹ Thuật Thủ Công",
    "tags": ["Layering", "Sticker 3D", "Scrapbook Tips", "Thủ Công Giấy", "Hologram"],
    "keywords": "kỹ thuật làm scrapbook, layering sticker 3d, cách trang trí sổ lưu niệm, sticker hologram handmade, dán sổ scrapbook đẹp",
    "is_featured": True,
    "content_sections": [
      {
        "heading": "1. Hiểu Về Nguyên Tắc Tầng Lớp (Background - Midground - Foreground)",
        "text": "Trong mỹ thuật thị giác scrapbook, một trang sổ cuốn hút luôn sở hữu 3 tầng không gian rõ rệt. Lớp nền (Background) thường là các mảng giấy Kraft hoặc băng dính Washi Tape (STK-004) dán caro nhẹ nhàng. Lớp giữa (Midground) là nơi đặt khung ảnh chính như Polaroid (LAY-001) hoặc dải phim 35mm (LAY-002). Cuối cùng, lớp tiền cảnh (Foreground) là nơi những chiếc Sticker 3D dập nổi (STK-001, STK-005) tỏa sáng rực rỡ."
      },
      {
        "heading": "2. Đòn Bẩy Ánh Sáng Với Sticker 3D Hologram & Ép Kim",
        "text": "Khác với sticker in phẳng thông thường, sticker 3D phủ bóng epoxy (STK-003) hoặc mạ vàng kim metallic (STK-005) có khả năng bắt sáng đa chiều. Khi đặt sticker hơi đè lên góc của tấm ảnh với góc nghiêng 10-15 độ, bạn sẽ tạo ra hiệu ứng đổ bóng tự nhiên, khiến bức ảnh như đang bật ra khỏi mặt trang sổ."
      },
      {
        "heading": "3. Ứng Dụng Xưởng Thiết Kế 2D & Trình Xem 3D",
        "text": "Trước khi dán trực tiếp lên sổ thật, bạn hoàn toàn có thể sử dụng Xưởng Thiết Kế Trực Tuyến (/studio) của ScrapCraft. Hệ thống cho phép bạn kéo thả thử các mã định danh linh kiện, xoay góc và mở chế độ 3D 360 độ để quan sát hiệu ứng ánh sáng trước khi hoàn thiện."
      }
    ],
    "related_skus": ["STK-001", "LAY-001", "STK-004", "SCR-002"]
  },
  {
    "id": "blog-002",
    "slug": "cach-bao-quan-anh-polaroid-va-giay-kraft-ben-10-nam",
    "title": "Bảo Quản Ảnh Polaroid & Giấy Thủ Công: Giữ Ký Ức Sắc Nét Suốt Hơn 10 Năm",
    "excerpt": "Ảnh polaroid và giấy thủ công có dễ bị ố vàng hay phai màu? Xem ngay cẩm nang chọn keo dán không axit (Acid-Free) và bìa sổ chuẩn bảo tàng.",
    "cover_image": "/static/assets/layouts/insp_001.svg",
    "thumbnail": "/static/assets/layouts/insp_001.svg",
    "author": "Minh Thư - Chuyên Gia Giấy",
    "published_date": "2026-08-15",
    "read_time": "5 phút đọc",
    "category": "Cẩm Nang Bảo Quản",
    "tags": ["Bảo Quản Ảnh", "Polaroid", "Giấy Kraft", "Acid-Free", "Kỷ Niệm"],
    "keywords": "bảo quản ảnh polaroid, chống ố vàng sổ scrapbook, keo dán acid free, giấy thủ công không phai màu, sổ lưu niệm bền đẹp",
    "is_featured": True,
    "content_sections": [
      {
        "heading": "1. Kẻ Thù Số Một Của Ảnh: Keo Dán Chứa Axit",
        "text": "Các loại hồ dán công nghiệp rẻ tiền thường có tính axit cao, sau 6-12 tháng sẽ làm ảnh polaroid bị ố vàng loang lổ. Giải pháp tối ưu là sử dụng layout cài góc giấy (LAY-001) hoặc băng dính Washi Tape tự nhiên (STK-004) có keo acrylic trung tính Acid-Free."
      },
      {
        "heading": "2. Lựa Chọn Sổ Bìa Cứng Chống Ẩm Nhiệt Đới",
        "text": "Khí hậu nhiệt đới ẩm tại Việt Nam đòi hỏi cuốn sổ scrapbook cần có bìa carton bồi dày trên 1800gsm như dòng SCR-001 hoặc bọc da PU chống nước SCR-002. Hãy bảo quản sổ trong hộp quà có lót giấy nến bảo vệ bề mặt."
      }
    ],
    "related_skus": ["SCR-001", "LAY-001", "STK-002"]
  },
  {
    "id": "blog-003",
    "slug": "top-10-y-tuong-scrapbook-ky-yeu-gen-z-cuc-chat",
    "title": "Top 10 Ý Tưởng Tự Làm Scrapbook Kỷ Yếu & Tình Bạn Khiến Cả Lớp Trầm Trồ",
    "excerpt": "Biến những trò đùa giỡn, meme bắt trend và khoảnh khắc thanh xuân vườn trường thành cuốn sổ kỷ yếu độc nhất vô nhị đậm chất Gen Z.",
    "cover_image": "/static/assets/layouts/insp_005.svg",
    "thumbnail": "/static/assets/layouts/insp_005.svg",
    "author": "Alex Vũ - Creative Director",
    "published_date": "2026-08-10",
    "read_time": "7 phút đọc",
    "category": "Ý Tưởng Sáng Tạo",
    "tags": ["Kỷ Yếu", "Gen Z", "Tình Bạn", "Thanh Xuân", "Meme Doodles"],
    "keywords": "sổ kỷ yếu gen z, tự làm scrapbook tặng bạn thân, ý tưởng trang trí sổ lớp học, scrapbook tình bạn, sổ handmade thanh xuân",
    "is_featured": True,
    "content_sections": [
      {
        "heading": "1. Trang Trí Bằng Sticker Meme Slang & Doodle Nổi 3D",
        "text": "Đừng làm kỷ yếu theo khuôn mẫu nhàm chán! Hãy dán những câu cửa miệng viral của nhóm bạn bằng bộ Sticker 3D Doodle Slang (STK-003) và ngôi sao Y2K (STK-001). Cảm giác dập nổi thạch dẻo sẽ khiến bạn bè thích thú chạm tay vào trang sổ."
      },
      {
        "heading": "2. Dàn Trang Ghép Ảnh Mosaic & Khung Tốt Nghiệp",
        "text": "Sử dụng layout ghép ảnh Mosaic (LAY-005) để gom ảnh dìm và ảnh nghiêm túc của cả nhóm vào cùng một khung hình. Điểm xuyết thêm Sticker Mũ Cử Nhân (STK-007) trang trọng để đánh dấu cột mốc trưởng thành."
      }
    ],
    "related_skus": ["STK-003", "STK-007", "LAY-005", "SCR-001"]
  },
  {
    "id": "blog-004",
    "slug": "scrapbook-la-gi-huong-dan-nguoi-moi-bat-dau-a-z",
    "title": "Scrapbook Là Gì? Hướng Dẫn Tự Làm Cuốn Sổ Lưu Niệm Đầu Tiên Từ A Đến Z",
    "excerpt": "Tất cả những gì bạn cần biết về nghệ thuật làm sổ thủ công Scrapbook: từ dụng cụ cơ bản, chọn phôi sổ, in ảnh đến cách bố cục cân đối.",
    "cover_image": "/static/assets/layouts/insp_001.svg",
    "thumbnail": "/static/assets/layouts/insp_001.svg",
    "author": "ScrapCraft Academy",
    "published_date": "2026-08-05",
    "read_time": "8 phút đọc",
    "category": "Cẩm Nang Nhập Môn",
    "tags": ["Scrapbook Là Gì", "Nhập Môn", "Hướng Dẫn", "DIY", "Thủ Công Giấy"],
    "keywords": "scrapbook là gì, cách làm scrapbook, scrapbook handmade, ý tưởng scrapbook, sticker scrapbook, layout scrapbook, quà handmade",
    "is_featured": False,
    "content_sections": [
      {
        "heading": "1. Định Nghĩa Scrapbook Trong Thời Đại Số",
        "text": "Scrapbook là hình thức lưu giữ kỷ niệm bằng cách kết hợp hình ảnh, câu chuyện viết tay, nhãn dán trang trí và kỷ vật thực tế trên các trang giấy thủ công. Khác với album ảnh số, scrapbook mang lại giá trị xúc giác và cảm xúc chân thật không thể thay thế."
      },
      {
        "heading": "2. Ba Bước Đơn Giản Cho Người Mới Bắt Đầu",
        "text": "Bước 1: Chọn một chủ đề cụ thể (chuyến du lịch, tình bạn hoặc kỷ niệm 1 năm). Bước 2: Chuẩn bị 15-20 bức ảnh in rửa kích thước 5x7cm hoặc 6x9cm. Bước 3: Sử dụng các layout có sẵn (LAY-001, LAY-004) để định vị khung hình trước khi trang trí sticker."
      }
    ],
    "related_skus": ["SCR-001", "LAY-001", "STK-002", "STK-004"]
  },
  {
    "id": "blog-005",
    "slug": "y-tuong-scrapbook-tinh-yeu-anniversary-lang-man",
    "title": "Gợi Ý 5 Ý Tưởng Scrapbook Tình Yêu Khiến Nửa Kia Rung Động Dịp Kỷ Niệm",
    "excerpt": "Tự tay làm cuốn album lưu giữ hành trình 365 ngày yêu nhau với cấu trúc Accordion mở rộng, con dấu sáp niêm phong và thư tay bí mật.",
    "cover_image": "/static/assets/layouts/insp_004.svg",
    "thumbnail": "/static/assets/layouts/insp_004.svg",
    "author": "Linh Đan - Tình Yêu & Sáng Tạo",
    "published_date": "2026-07-28",
    "read_time": "5 phút đọc",
    "category": "Ý Tưởng Sáng Tạo",
    "tags": ["Tình Yêu", "Anniversary", "Valentine", "Quà Tặng", "Accordion"],
    "keywords": "scrapbook tình yêu, quà tặng người yêu handmade, album kỷ niệm 1 năm yêu nhau, sổ scrapbook lãng mạn, quà valentine tự làm",
    "is_featured": False,
    "content_sections": [
      {
        "heading": "1. Bố Cục Gấp Xếp Accordion Chứa 8 Khoảnh Khắc Bất Ngờ",
        "text": "Cấu trúc Accordion 3D (LAY-003) buộc nơ ruy băng khi mở bung ra sẽ hé lộ chuỗi 8 bức ảnh hẹn hò ngọt ngào từ ngày đầu tiên gặp gỡ đến hiện tại."
      },
      {
        "heading": "2. Niêm Phong Thư Tay Bằng Dấu Sáp Đỏ Burgundy Hoàng Gia",
        "text": "Tạo nét trang trọng và huyền bí bằng cách gắn phong bì bí mật (LAY-004) và niêm phong bằng con dấu sáp đúc nổi 3D (STK-010). Đối phương sẽ vô cùng hồi hộp khi mở lá thư tay của bạn."
      }
    ],
    "related_skus": ["SCR-002", "LAY-003", "STK-006", "STK-010"]
  },
  {
    "id": "blog-006",
    "slug": "cach-phoi-mau-scrapbook-vintage-kraft-chuan-aesthetic",
    "title": "Bí Quyết Phối Màu Sổ Vintage & Giấy Kraft Đậm Chất Cổ Điển Hoài Niệm",
    "excerpt": "Học cách kết hợp bảng màu Nâu Kraft, Cam Đất, Xanh Olive và Nhũ Vàng để cuốn sổ luôn giữ được sự ấm cúng, sang trọng và không bị rối mắt.",
    "cover_image": "/static/assets/layouts/insp_001.svg",
    "thumbnail": "/static/assets/layouts/insp_001.svg",
    "author": "Hoàng Nam - Art Director",
    "published_date": "2026-07-20",
    "read_time": "6 phút đọc",
    "category": "Kỹ Thuật Thủ Công",
    "tags": ["Phối Màu", "Vintage", "Kraft", "Aesthetic", "Màu Sắc"],
    "keywords": "phối màu scrapbook, sổ kraft vintage đẹp, cách trang trí sổ màu ấm, hoa khô dán sổ, tone màu hoài niệm",
    "is_featured": False,
    "content_sections": [
      {
        "heading": "1. Nguyên Tắc 60-30-10 Trong Phối Màu Thủ Công",
        "text": "Áp dụng tỷ lệ vàng: 60% diện tích là tone nền nâu Kraft tự nhiên (SCR-001), 30% là các mảng ảnh Polaroid trắng ngà (LAY-001), và 10% là điểm nhấn hoa cỏ cam đất (STK-002) hoặc nhũ vàng metallic (STK-005)."
      }
    ],
    "related_skus": ["SCR-001", "STK-002", "STK-005", "LAY-007"]
  },
  {
    "id": "blog-007",
    "slug": "tao-scrapbook-anh-film-35mm-dark-mode-chat-lu",
    "title": "Biến Những Cuộn Film 35mm Thành Tác Phẩm Nghệ Thuật Dark Academia",
    "excerpt": "Hướng dẫn lưu giữ ảnh film cuộn trên nền sổ đen mỹ thuật với dải phim liên hoàn và sticker máy ảnh analog dập nổi tinh tế.",
    "cover_image": "/static/assets/layouts/insp_003.svg",
    "thumbnail": "/static/assets/layouts/insp_003.svg",
    "author": "Đức Anh - Film Photographer",
    "published_date": "2026-07-15",
    "read_time": "5 phút đọc",
    "category": "Ý Tưởng Sáng Tạo",
    "tags": ["Ảnh Film", "Film 35mm", "Dark Mode", "Analog", "Nhiếp Ảnh"],
    "keywords": "album ảnh film 35mm, scrapbook giấy đen, dark academia aesthetic, sổ dán ảnh film đẹp, máy ảnh film hoài niệm",
    "is_featured": False,
    "content_sections": [
      {
        "heading": "1. Tận Dụng Độ Tương Phản Của Giấy Black Cardstock",
        "text": "Nền giấy đen (SCR-003) có khả năng làm nổi bật màu sắc ấm áp và hạt grain đặc trưng của ảnh film 35mm. Hãy kết hợp cùng layout dải phim (LAY-002) để tái hiện không khí của một phòng tối rọi ảnh."
      }
    ],
    "related_skus": ["SCR-003", "LAY-002", "STK-008", "STK-012"]
  },
  {
    "id": "blog-008",
    "slug": "huong-dan-su-dung-ai-thiet-ke-bo-cuc-scrapbook",
    "title": "Cách Dùng AI Design Assistant Để Tự Động Gợi Ý Bố Cục Scrapbook Chuẩn Xác",
    "excerpt": "Khám phá cách công nghệ AI tại Xưởng Thiết Kế ScrapCraft giúp bạn phân tích cảm xúc, chọn lựa đúng mã phụ kiện và sắp đặt tọa độ hoàn hảo.",
    "cover_image": "/static/assets/layouts/insp_002.svg",
    "thumbnail": "/static/assets/layouts/insp_002.svg",
    "author": "Tech & Craft Team",
    "published_date": "2026-07-10",
    "read_time": "4 phút đọc",
    "category": "Công Nghệ & AI",
    "tags": ["AI Assistant", "Xưởng Thiết Kế", "Bố Cục AI", "Công Nghệ", "Studio 3D"],
    "keywords": "ai gợi ý bố cục scrapbook, thiết kế scrapbook bằng ai, xưởng thiết kế 3d, công cụ làm scrapbook online, bố cục tự động",
    "is_featured": False,
    "content_sections": [
      {
        "heading": "1. AI Phân Tích Ý Định Từ Câu Lệnh Tự Nhiên",
        "text": "Khi bạn nhập câu lệnh như 'Làm scrapbook tặng bạn thân nhân dịp tốt nghiệp tone ấm', trợ lý AI sẽ tự động trích xuất các thuộc tính: occasion=graduation, relationship=friendship, style=warm. Sau đó, AI sẽ truy vấn trực tiếp vào cơ sở dữ liệu để tìm ra các mã SKU như STK-007, LAY-005 và SCR-001."
      },
      {
        "heading": "2. Tính Toán Tọa Độ Cân Đối Thị Giác Trên Canvas",
        "text": "Không chỉ đề xuất danh sách, AI còn tính toán góc nghiêng tự nhiên (-5 đến +8 độ) và xếp tầng layer zIndex hợp lý, cho phép bạn áp dụng ngay lên canvas chỉ với một cú click."
      }
    ],
    "related_skus": ["STK-007", "LAY-005", "SCR-001", "STK-001"]
  }
]

with open(os.path.join(DATA_DIR, 'blogs.json'), 'w', encoding='utf-8') as f:
    json.dump(blogs, f, ensure_ascii=False, indent=2)

company_info = {
  "brand_name": "ScrapCraft Studio",
  "tagline": "Thương hiệu phụ kiện trang trí & Xưởng thiết kế Scrapbook thủ công Gen Z",
  "sub_tagline": "Kết hợp công nghệ WebGL 3D 360 độ và AI gợi ý bố cục thông minh",
  "story": {
    "mission": "Mang ký ức số trong điện thoại trở về thế giới vật lý ấm áp, nơi từng bức ảnh polaroid và chi tiết dập nổi có thể chạm vào được bằng tay.",
    "vision": "Trở thành hệ sinh thái DIY Scrapbook trực tuyến số 1 tại Việt Nam, chuẩn hóa mã định danh linh kiện.",
    "milestones": [
      {
        "year": "2023",
        "title": "Thành Lập Xưởng Thủ Công",
        "desc": "Khởi xướng dự án DIY Scrapbook tại TP. Hồ Chí Minh với 100% giấy chuẩn FSC Acid-Free."
      },
      {
        "year": "2024",
        "title": "Ra Mắt Dòng Sticker 3D Dập Nổi",
        "desc": "Nghiên cứu thành công kỹ thuật phủ màng Hologram laser và dập nổi viền sắc nét 0.8mm."
      },
      {
        "year": "2025",
        "title": "Tích Hợp Xưởng 3D & Trợ Lý AI",
        "desc": "Tiên phong ứng dụng mô phỏng 3D WebGL và AI gợi ý dàn trang trực quan trên trình duyệt."
      }
    ],
    "craft_pillars": [
      {
        "icon": "FSC",
        "title": "Giấy Mỹ Thuật Chuẩn FSC",
        "desc": "100% nguyên liệu giấy nhập khẩu không axit (Acid-Free) bảo vệ ảnh vĩnh cửu."
      },
      {
        "icon": "3D",
        "title": "Kỹ Thuật Dập Nổi 3D & Ép Kim",
        "desc": "Hiệu ứng xúc chạm sống động, phản chiếu ánh kim đa sắc."
      },
      {
        "icon": "POL",
        "title": "Khung Cài Thông Minh Không Hỏng Ảnh",
        "desc": "Dễ dàng thay đổi ảnh polaroid mà không cần dùng keo dính trực tiếp."
      },
      {
        "icon": "SKU",
        "title": "Mã Định Danh Chuẩn Hóa",
        "desc": "Đồng bộ tuyệt đối giữa mô hình 3D trên web và phụ kiện trong kho."
      }
    ]
  },
  "contact": {
    "address": "Số 88/12 Đường Nguyễn Huệ, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh",
    "hotline": "0988.246.810 (Zalo Hỗ Trợ 24/7)",
    "email": "hello@scrapcraft.studio",
    "working_hours": "08:30 - 21:00 (Thứ 2 - Chủ Nhật)",
    "socials": {
      "tiktok": "https://tiktok.com/@scrapcraft.studio",
      "instagram": "https://instagram.com/scrapcraft.studio",
      "facebook": "https://facebook.com/scrapcraft.studio.vn",
      "shopee": "https://shopee.vn/scrapcraft.studio"
    }
  },
  "policies": {
    "privacy": {
      "title": "Chính Sách Bảo Mật Hình Ảnh Cá Nhân Tuyệt Đối",
      "detail": "Mọi hình ảnh cá nhân bạn tải lên Xưởng Thiết Kế chỉ được lưu trữ tạm thời trong bộ nhớ đệm (Local Session) để phục vụ việc xem trước 2D/3D. Chúng tôi cam kết 100% không lưu trữ, không sử dụng cho mục đích quảng cáo hoặc chia sẻ cho bên thứ ba."
    },
    "copyright": {
      "title": "Bản Quyền Tác Phẩm & Quyền Sở Hữu Thiết Kế",
      "detail": "Khách hàng nắm giữ 100% quyền sở hữu trí tuệ đối với các bố cục, tác phẩm và nội dung nhật ký được sáng tạo trên nền tảng. ScrapCraft Studio chỉ cung cấp nguyên vật liệu và công cụ gia công."
    },
    "shipping": {
      "title": "Chính Sách Vận Chuyển & Đóng Gói Chuyên Dụng",
      "detail": "Đơn hàng phụ kiện được đóng gói 3 lớp với màng xốp khí chống sốc và bìa carton bảo vệ góc sổ. Miễn phí vận chuyển toàn quốc cho đơn hàng từ 350.000đ."
    },
    "warranty": {
      "title": "Chính Sách Đổi Trả & Bảo Hành 1-Đổi-1",
      "detail": "Cam kết đổi mới 1-đổi-1 miễn phí trong vòng 7 ngày nếu phát hiện bất kỳ lỗi sản xuất nào như gãy còng sổ, móp góc bìa hoặc sticker bong tróc màng hologram."
    }
  }
}

with open(os.path.join(DATA_DIR, 'company_info.json'), 'w', encoding='utf-8') as f:
    json.dump(company_info, f, ensure_ascii=False, indent=2)

print('All products, inspirations, blogs, and company_info datasets successfully saved!')

# Create templates/components/carousel.html
os.makedirs(os.path.join(BASE_DIR, 'templates', 'components'), exist_ok=True)
carousel_macro = '''{# Reusable Unified Page Carousel Component #}
{% macro render_carousel(carousel_id, slides) %}
<section class="relative overflow-hidden bg-gradient-to-b from-amber-50/70 via-rose-50/30 to-[#fdfbf7] py-10 md:py-16 border-b-2 border-black">
  <div class="absolute inset-0 bg-grid-pattern opacity-30 pointer-events-none"></div>

  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative">
    <div id="{{ carousel_id }}" class="unified-carousel relative min-h-[420px]" data-current="0">
      
      {% for slide in slides %}
      <div class="carousel-slide-item {% if not loop.first %}hidden opacity-0{% else %}opacity-100{% endif %} transition-opacity duration-500 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center" data-index="{{ loop.index0 }}">
        
        <!-- Text Column -->
        <div class="lg:col-span-7 space-y-5 text-center lg:text-left">
          {% if slide.badge %}
          <div class="inline-flex items-center gap-2 bg-amber-300 border-2 border-black px-4 py-1 rounded-full shadow-neo text-xs font-black uppercase tracking-wider text-stone-900">
            <span>{{ slide.badge }}</span>
          </div>
          {% endif %}
          
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-black leading-tight text-stone-900">
            {{ slide.title | safe }}
          </h1>
          
          <p class="text-sm sm:text-base text-stone-700 font-medium max-w-xl mx-auto lg:mx-0 leading-relaxed">
            {{ slide.desc | safe }}
          </p>
          
          {% if slide.buttons %}
          <div class="flex flex-wrap items-center justify-center lg:justify-start gap-4 pt-2">
            {% for btn in slide.buttons %}
              {% if btn.primary %}
              <a href="{{ btn.url }}" class="bg-rose-800 hover:bg-rose-900 text-white font-heading font-black text-sm sm:text-base px-7 py-3.5 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all flex items-center gap-2">
                <span>{{ btn.text }}</span>
                <span class="text-amber-300 font-mono font-bold">→</span>
              </a>
              {% else %}
              <a href="{{ btn.url }}" class="bg-white hover:bg-stone-50 text-stone-900 font-heading font-bold text-sm sm:text-base px-6 py-3.5 rounded-2xl border-2 border-black shadow-neo shadow-neo-hover transition-all">
                {{ btn.text }}
              </a>
              {% endif %}
            {% endfor %}
          </div>
          {% endif %}
        </div>

        <!-- Visual Mockup Column -->
        <div class="lg:col-span-5 relative flex justify-center">
          <div class="w-full max-w-md bg-white border-2 border-black rounded-3xl p-5 shadow-neo relative transform hover:rotate-1 transition-transform">
            <div class="washi-tape-top"></div>
            <img src="{{ slide.image }}" alt="{{ slide.badge or 'Mockup' }}" class="w-full h-56 sm:h-64 object-contain rounded-2xl bg-amber-50/30 p-2 border border-stone-200">
            
            {% if slide.corner_badge %}
            <div class="absolute -bottom-3 -right-3 bg-amber-300 border-2 border-black rounded-xl px-3 py-1 font-heading font-black text-xs text-stone-900 shadow-neo">
              {{ slide.corner_badge }}
            </div>
            {% endif %}
          </div>
        </div>

      </div>
      {% endfor %}

    </div>

    <!-- Carousel Nav Controls -->
    <div class="flex items-center justify-between mt-8 max-w-xs mx-auto">
      <button onclick="navigateCarousel('{{ carousel_id }}', -1)" class="w-9 h-9 rounded-xl bg-white hover:bg-amber-300 border-2 border-black font-black flex items-center justify-center shadow-neo text-stone-900 transition-colors" aria-label="Slide truoc">
        ←
      </button>
      
      <!-- Dots -->
      <div class="flex items-center gap-2.5">
        {% for slide in slides %}
        <button onclick="goToCarouselSlide('{{ carousel_id }}', {{ loop.index0 }})" class="carousel-dot-btn w-3 h-3 rounded-full border border-black transition-all {% if loop.first %}w-7 bg-rose-800{% else %}bg-stone-300 hover:bg-amber-300{% endif %}" data-dot-index="{{ loop.index0 }}" aria-label="Slide {{ loop.index }}"></button>
        {% endfor %}
      </div>

      <button onclick="navigateCarousel('{{ carousel_id }}', 1)" class="w-9 h-9 rounded-xl bg-white hover:bg-amber-300 border-2 border-black font-black flex items-center justify-center shadow-neo text-stone-900 transition-colors" aria-label="Slide tiep theo">
        →
      </button>
    </div>

  </div>
</section>
{% endmacro %}
'''
with open(os.path.join(BASE_DIR, 'templates', 'components', 'carousel.html'), 'w', encoding='utf-8') as f:
    f.write(carousel_macro)
print('templates/components/carousel.html generated successfully!')

# ==================== AUTOMATED VERIFICATION SUITE ====================
print('\nRunning Automated Route & API Verification Tests...')
from app import app

client = app.test_client()

routes = [
    ('/', 200),
    ('/about', 200),
    ('/products', 200),
    ('/products?category=sticker', 200),
    ('/products?category=layout', 200),
    ('/products?category=scrapbook', 200),
    ('/products?is_3d=true', 200),
    ('/products?sort=price_asc', 200),
    ('/product/STK-001', 200),
    ('/product/LAY-001', 200),
    ('/product/SCR-001', 200),
    ('/inspiration', 200),
    ('/inspirations', 200),
    ('/guide', 200),
    ('/handbook', 200),
    ('/guide/huong-dan-layering-sticker-3d-chieu-sau-scrapbook', 200),
    ('/contact', 200),
    ('/studio', 200),
    ('/studio?remix=insp_001', 200),
    ('/studio?sku=STK-001', 200),
    ('/cart', 200),
    ('/order-tracking', 200),
    ('/api/products', 200),
    ('/api/inspirations', 200),
    ('/api/blogs', 200)
]

all_passed = True
for r, expected_status in routes:
    res = client.get(r)
    if res.status_code != expected_status:
        print(f'[FAIL] GET {r} -> {res.status_code} (expected {expected_status})')
        all_passed = False
    else:
        print(f'[PASS] GET {r} -> {res.status_code}')

# Test AI Suggestion API
ai_res = client.post('/api/ai-suggest', json={'prompt': 'kỷ yếu bạn thân phong cách vintage'})
if ai_res.status_code == 200 and ai_res.json.get('status') == 'success':
    ai_data = ai_res.json
    book_sku = ai_data.get('book', {}).get('sku')
    layout_skus = [l.get('sku') for l in ai_data.get('layouts', [])]
    sticker_skus = [s.get('sku') for s in ai_data.get('stickers', [])]
    print(f'[PASS] POST /api/ai-suggest -> Book: {book_sku}, Layouts: {layout_skus}, Stickers: {sticker_skus}')
else:
    print(f'[FAIL] POST /api/ai-suggest -> {ai_res.status_code}')
    all_passed = False

# Test Orders Creation API
order_res = client.post('/api/orders', json={
    'name': 'Nguyễn Linh Nhi',
    'phone': '0988246810',
    'address': 'Quận Cầu Giấy, Hà Nội',
    'note': 'Gói nơ quà tặng kèm thiệp',
    'items': [{'sku': 'STK-001', 'name': 'Sticker 3D Y2K', 'price': 35000, 'quantity': 2}],
    'total_amount': 70000,
    'discount_amount': 7000,
    'final_amount': 93000
})
if order_res.status_code == 200 and order_res.json.get('status') == 'success':
    order_code = order_res.json['order']['order_code']
    print(f'[PASS] POST /api/orders -> Created Order {order_code}')
    
    # Query Tracking
    track_res = client.get(f'/api/orders?q={order_code}')
    if track_res.status_code == 200 and len(track_res.json.get('orders', [])) > 0:
        print(f'[PASS] GET /api/orders?q={order_code} -> Found active order')
    else:
        print(f'[FAIL] Querying order {order_code}')
        all_passed = False
else:
    print(f'[FAIL] POST /api/orders -> {order_res.status_code}')
    all_passed = False

if all_passed:
    print('\n' + '='*50)
    print('ALL ENDPOINTS & ENGINE TESTS PASSED 100% PERFECTLY!')
    print('='*50)
else:
    print('\nSOME TESTS FAILED!')

