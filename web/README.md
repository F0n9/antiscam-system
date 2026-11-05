# GIAO DIỆN WEB QUẢN TRỊ & TRA CỨU (NEXT.JS)

Thành phần giao diện người dùng trên nền tảng Web của Hệ thống AntiScam (do **Module C - Trương Bảo Nguyên** phụ trách).

---

## 1. Công nghệ sử dụng
* **Framework:** Next.js 14 (React 18, TypeScript)
* **CSS:** TailwindCSS
* **Thư viện đồ thị:** Cytoscape.js (vẽ mạng lưới thực thể liên kết tương tác)
* **Giao tiếp API:** Axios

---

## 2. Hướng dẫn khởi chạy cục bộ

1. **Di chuyển vào thư mục web:**
   ```bash
   cd web
   ```
2. **Cài đặt các gói npm:**
   ```bash
   npm install
   ```
3. **Cấu hình biến môi trường:**
   Tạo tệp `.env.local` tại thư mục `web/`:
   ```bash
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1
   ```
4. **Chạy máy chủ phát triển:**
   ```bash
   npm run dev
   ```
5. **Truy cập ứng dụng:** Mở trình duyệt tại [http://localhost:3000](http://localhost:3000).

---

## 3. Các trang chức năng chính cần xây dựng
* `/`: Trang chủ tra cứu nhanh (nhập số tài khoản, số điện thoại hoặc tải ảnh phòng trọ).
* `/graph`: Bảng trực quan hóa cây đồ thị liên kết thực thể (tích hợp Cytoscape.js).
* `/map`: Bản đồ phát sóng cảnh báo lừa đảo xung quanh theo bán kính 3 km.
* `/report`: Biểu mẫu tiếp nhận tố cáo lừa đảo kèm tải lên chứng từ ủy nhiệm chi ngân hàng.
* `/admin`: Bảng điều khiển dành cho Quản trị viên kiểm duyệt tranh chấp và tố cáo.

