# Deploy MEMOUR lên Cloudflare (gói miễn phí)

Website dùng Cloudflare Python Workers cho Flask và Static Assets cho toàn bộ
ảnh, CSS, JavaScript. URL `/static/...` được giữ nguyên, vì vậy không cần sửa
link cũ, canonical URL hay Google Analytics (`G-EH7LKGCKHH`).

## 1. Chuẩn bị công cụ

Yêu cầu Node.js và `uv`, sau đó đăng nhập Cloudflare:

```powershell
npx wrangler login
uv sync
```

## 2. Tạo D1 miễn phí cho đơn hàng

```powershell
npx wrangler d1 create memour-orders
```

Sao chép `database_id` mà lệnh trả về vào `wrangler.jsonc`, thay cho
`REPLACE_WITH_D1_DATABASE_ID`, rồi chạy migration:

```powershell
npx wrangler d1 migrations apply memour-orders --remote
```

Không bỏ qua bước D1: Cloudflare Workers không lưu bền file `orders.json`.

## 3. Chạy thử và deploy

```powershell
uv run pywrangler dev
uv run pywrangler deploy
```

Kiểm tra trang chủ, `/robots.txt`, `/sitemap.xml`, giỏ hàng và tra cứu đơn hàng
trên URL `workers.dev` trước khi nối tên miền.

## 4. Nối tên miền mà không mất GA4/SEO

Trong Cloudflare Dashboard, mở Worker vừa deploy, vào **Settings > Domains &
Routes > Add > Custom Domain** và thêm `memourscrapbook.com` (thêm cả
`www.memourscrapbook.com` nếu đang sử dụng). Chỉ chuyển DNS sau khi URL thử đã
hoạt động.

Mã GA4 nằm trong `templates/base.html` và không thay đổi. Dữ liệu cũ trong GA4
vẫn thuộc cùng property/data stream; đổi hosting không xóa dữ liệu. Sau khi nối
domain, mở **GA4 Realtime** và truy cập website bằng cửa sổ ẩn danh để xác nhận
có lượt xem mới.

Không cần xóa project Vercel ngay. Giữ lại để rollback; khi Cloudflare chạy ổn,
gỡ custom domain khỏi Vercel để tránh cấu hình trùng. URL Vercel cũ đã được code
chuyển 308 về domain chính khi còn hoạt động.

## Lưu ý vận hành

- Static Assets được phục vụ trước Worker, giảm đáng kể request và băng thông
  động; không đặt `run_worker_first` thành `true`.
- Không chạy bot tăng traffic trên domain production. Cloudflare Free vẫn có
  giới hạn request Worker dù Static Assets được phục vụ riêng.
- API thêm/xóa sticker lúc runtime bị tắt trên Cloudflare vì asset deploy là chỉ
  đọc. Hãy sửa asset trong Git rồi deploy lại.
- API phân tích sticker bằng OpenCV chỉ dành cho môi trường quản trị/local.
