# KẾ HOẠCH PHÁT TRIỂN 12 TUẦN (WEEKLY SPRINT PLAN)

Dự án kéo dài trong 12 tuần của môn học, được chia thành 5 Sprint theo quy trình Scrum.

---

## Sprint 0: Khảo sát, Đặc tả yêu cầu & Thiết kế kiến trúc (Tuần 1 – Tuần 2)

* **Tuần 1:**
  * Khảo sát các kịch bản lừa cọc phòng trọ sinh viên, tuyển dụng việc làm online và lừa đảo mạo danh người cao tuổi.
  * Hoàn thiện tài liệu Project Proposal.
  * Lập bảng câu chuyện người dùng (User Stories) và danh mục chức năng F1 đến F5.
* **Tuần 2:**
  * Biên soạn tài liệu Đặc tả yêu cầu phần mềm (**SRS**) theo chuẩn IEEE 830.
  * Thiết kế Wireframe và Mockup giao diện Web & Android trên Figma.
  * Thiết lập GitHub Repository, Docker Compose, `.gitignore`, bảng Kanban.
* **Kết quả bàn giao (Deliverables):** Tài liệu Proposal hoàn chỉnh, Tài liệu SRS, Link Figma UI, GitHub Repo khởi tạo.

---

## Sprint 1: Khởi dựng hạ tầng, API cốt lõi & Android MVP 1 (Tuần 3 – Tuần 5)

* **Tuần 3:**
  * [Module A] Dựng container PostgreSQL, viết schema SQLAlchemy và API `/auth/register`, `/auth/login`.
  * [Module B] Cài đặt Neo4j trên Docker, tạo constraint cho các node `:PhoneNumber`, `:BankAccount`, `:ScamReport`.
  * [Module C] Khởi tạo dự án Next.js 14, cài đặt TailwindCSS, dựng layout khung bảng điều khiển.
  * [Module D] Khởi tạo Android Studio, cấu hình quyền Android Manifest cho `CallScreeningService`.
* **Tuần 4:**
  * [Module A] Viết router tiếp nhận báo cáo `/reports/submit` (upload ảnh ủy nhiệm chi).
  * [Module B] Viết script nạp dữ liệu mẫu ban đầu vào Neo4j (Seed data 100 nút).
  * [Module C] Dựng giao diện form tra cứu số điện thoại/tài khoản và form gửi tố cáo trên Web.
  * [Module D] Lập trình `CallScreeningService` chặn cuộc gọi lạ và `NotificationListenerService` đọc chuỗi từ thông báo.
* **Tuần 5:**
  * Tích hợp kiểm tra kết nối API giữa Android/Web và FastAPI Backend.
  * Họp Sprint Review 1, xuất bản file APK thử nghiệm đầu tiên (MVP 1).
* **Kết quả bàn giao:** Tài liệu thiết kế kiến trúc (**SDD**), Bản build APK MVP 1, API Swagger chạy ổn định.

---

## Sprint 2: Đồ thị tri thức, Thuật toán tính điểm & SOS Gia đình (Tuần 6 – Tuần 8)

* **Tuần 6:**
  * [Module B] Viết câu lệnh Cypher tìm kiếm đường đi ngắn nhất đến nút lừa đảo trong phạm vi 3 bước (`shortestPath`).
  * [Module B] Cài đặt công thức tính điểm tín nhiệm (4 thành phần trọng số: $W_g=0.40, W_p=0.25, W_s=0.20, W_i=0.15$).
  * [Module A] Viết API bóc tách mã VietQR và tính mã băm ảnh `pHash` (ngưỡng Hamming $\le 10$).
* **Tuần 7:**
  * [Module A & D] Tích hợp Firebase Cloud Messaging (FCM) gửi thông báo đẩy thời gian thực.
  * [Module D] Lập trình giao diện SOS trên Android: phát âm thanh cảnh báo lớn, tự động bắn tín hiệu SOS lên server.
  * [Module C] Tích hợp thư viện Cytoscape.js hiển thị cây đồ thị quan hệ từ API Backend.
* **Tuần 8:**
  * Kết nối toàn bộ luồng: Android quét VietQR $\rightarrow$ Backend kiểm tra Neo4j $\rightarrow$ Trả kết quả rủi ro $\rightarrow$ Bắn SOS cho tài khoản người thân.
  * Họp Sprint Review 2.
* **Kết quả bàn giao:** Hệ thống MVP 2 hoàn thiện tính năng cảnh báo SOS và truy vấn đồ thị 3 bước.

---

## Sprint 3: Trực quan hóa nâng cao, Cảnh báo khu vực & Kiểm thử (Tuần 9 – Tuần 10)

* **Tuần 9:**
  * [Module C] Hoàn thiện giao diện hiển thị bản đồ cảnh báo lừa đảo trong bán kính 3 km.
  * [Module C] Bổ sung tính năng tương tác với cây đồ thị Cytoscape (zoom, lọc nút vi phạm, xem chi tiết chứng từ).
  * [Module A & B] Tối ưu hóa truy vấn Cypher đạt mốc thời gian đáp ứng dưới 500ms trên tập dữ liệu tối thiểu 1.000 nút.
* **Tuần 10:**
  * Viết Unit Test cho module tính điểm tín nhiệm và parser VietQR (độ phủ kiểm thử > 80%).
  * Kiểm thử toàn diện hệ thống với tập dữ liệu 200 vụ lừa đảo thực tế.
  * Thử nghiệm thực tế tính năng lọc cuộc gọi lạ và thông báo Zalo/SMS trên điện thoại thật bằng SIM phụ.
* **Kết quả bàn giao:** Tài liệu báo cáo kiểm thử (**Test Report**), Tập dữ liệu thử nghiệm 200 vụ việc.

---

## Sprint 4: Đóng gói, Triển khai đám mây & Nghiệm thu (Tuần 11 – Tuần 12)

* **Tuần 11:**
  * Đóng gói toàn bộ hệ thống bằng Docker Compose trên máy chủ ảo đám mây (Ubuntu VPS).
  * Cài đặt Nginx Reverse Proxy, cấu hình tên miền và chứng chỉ SSL/TLS miễn phí qua Let's Encrypt.
  * Ký số và xuất bản tệp `antiscam-v1.0.apk` chính thức.
* **Tuần 12:**
  * Quay video demo minh họa các kịch bản thực tế (lừa cọc trọ, bẫy tuyển dụng, người lớn tuổi bị gọi lừa đảo và cảnh báo SOS).
  * Soạn thảo slide báo cáo nghiệm thu đề tài trước Hội đồng bộ môn.
  * Đóng gói mã nguồn, hồ sơ nghiệm thu cuối kỳ.
* **Kết quả bàn giao:** Đường dẫn Web App trực tuyến, Tệp APK phát hành, Video Demo, Slide thuyết trình và Báo cáo tổng kết.
