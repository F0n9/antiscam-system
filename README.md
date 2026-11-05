# HỆ THỐNG KIỂM CHỨNG VÀ CẢNH BÁO LỪA ĐẢO TRỰC TUYẾN BẰNG ĐỒ THỊ LIÊN KẾT THỰC THỂ

* **Môn học:** Nhập môn Công nghệ Phần mềm
* **Lớp học phần:** 24_31
* **Nhóm thực hiện:** Nhóm 03
* **Đơn vị:** Khoa Công nghệ Thông tin, Trường Đại học Khoa học Tự nhiên – ĐHQG-HCM
* **Giảng viên hướng dẫn:** ThS. Ngô Ngọc Đăng Khoa

---

## 1. Thành viên nhóm & Phân công trách nhiệm

| MSSV | Họ và tên | Module phụ trách | Vai trò chính |
| :---: | :--- | :--- | :--- |
| **24120149** | **Đặng Quang Tiến** | Module A | Kỹ sư Hệ thống phía máy chủ & Quản trị (FastAPI, PostgreSQL, Auth, Quản trị tố cáo) |
| **24120334** | **Hoàng Khang** | Module B | Kỹ sư Dữ liệu đồ thị (Neo4j, Cypher, Thuật toán tính điểm tín nhiệm rủi ro) |
| **24120397** | **Trương Bảo Nguyên** | Module C | Kỹ sư Giao diện Web (Next.js, Trực quan hóa cây đồ thị Cytoscape, Bản đồ cảnh báo) |
| **24120425** | **Sỉn Thăng Quyền** | Module D | Kỹ sư Di động & AI (Android native, CallScreening, NotificationListener, SOS khẩn cấp, VietQR) |

---

## 2. Kiến trúc tổng thể hệ thống

Hệ thống được thiết kế theo kiến trúc 3 tầng:

1. **Tầng Client:**
   * **Web Application (`/web`):** Next.js (React, TypeScript, TailwindCSS), trực quan hóa mạng lưới đồ thị với Cytoscape.js.
   * **Mobile Application (`/mobile`):** Android native (Kotlin), tích hợp `CallScreeningService` (lọc số lạ) và `NotificationListenerService` (lắng nghe thụ động thông báo Zalo/Messenger/SMS), cơ chế SOS gia đình.
2. **Tầng Server (`/backend`):**
   * Python 3.11 với FastAPI xử lý bất đồng bộ (async).
   * Dịch vụ bóc tách VietQR, tính mã băm tri giác ảnh (pHash) và NLP nhận diện đòn tâm lý.
   * Firebase Admin SDK gửi thông báo đẩy SOS và cảnh báo khu vực.
3. **Tầng Lưu trữ (Database):**
   * **Neo4j Community (5.18):** Quản trị mạng lưới đồ thị liên kết các thực thể (*Số điện thoại, Tài khoản ngân hàng, Mã băm ảnh, Báo cáo lừa đảo*).
   * **PostgreSQL (16):** Lưu trữ tài khoản người dùng, phân quyền, lịch sử phiên, chứng từ ủy nhiệm chi.

---

## 3. Cấu trúc thư mục mã nguồn

```text
antiscam-system/
├── .github/                   # Cấu hình GitHub, mẫu PR và Issue
├── backend/                   # [Module A & B] FastAPI, SQLAlchemy, Neo4j Driver
│   ├── app/
│   │   ├── api/v1/endpoints/  # Các router API (auth, verify, reports, sos, graph)
│   │   ├── core/              # Config, Security, DB connection
│   │   ├── models/            # Schema Pydantic và Model DB
│   │   └── services/          # Logic đồ thị, thuật toán tính điểm, pHash
│   ├── init-db/               # Script SQL tự động chạy khi khởi tạo PostgreSQL
│   ├── tests/                 # Unit test cho tính điểm và API
│   ├── Dockerfile
│   └── requirements.txt
├── web/                       # [Module C] Frontend Next.js & Cytoscape
├── mobile/                    # [Module D] Ứng dụng Android (Kotlin)
├── scripts/                   # Script nạp dữ liệu mồi Neo4j/Postgres (seed_data.py)
├── docs/                      # Tài liệu kỹ thuật dự án
│   ├── PROPOSAL.md            # Đề xuất dự án & Phân công trách nhiệm
│   ├── API_CONTRACT.md        # Đặc tả chi tiết RESTful API giữa các module
│   ├── DATABASE_SCHEMA.md     # Lược đồ Neo4j & PostgreSQL
│   ├── GIT_WORKFLOW.md        # Quy chuẩn Git, nhánh và nhịp sinh hoạt tuần
│   └── WEEKLY_PLAN.md         # Kế hoạch tiến độ 12 tuần (Sprint 0 - Sprint 4)
├── docker-compose.yml         # Khởi tạo PostgreSQL + Neo4j + Backend
├── .env.example               # Mẫu biến môi trường
└── .gitignore                 # Loại trừ file rác, cache, secrets
```

---

## 4. Hướng dẫn khởi chạy nhanh môi trường cục bộ (Quick Start)

### Yêu cầu tiên quyết
* Đã cài đặt [Docker](https://www.docker.com/) và Docker Compose.
* Đã cài đặt Git.

### Các bước thực hiện:

1. **Clone mã nguồn:**
   ```bash
   git clone <URL_REPO_CUA_NHOM>
   cd antiscam-system
   ```

2. **Thiết lập biến môi trường:**
   ```bash
   cp .env.example .env
   # Điều chỉnh lại mật khẩu nếu cần trong tệp .env
   ```

3. **Khởi chạy hạ tầng cơ sở dữ liệu và Backend qua Docker:**
   ```bash
   docker compose up -d
   ```

4. **Kiểm tra trạng thái các dịch vụ:**
   * **FastAPI Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
   * **Neo4j Browser UI:** [http://localhost:7474](http://localhost:7474) (User: `neo4j` / Password: `antiscam_neo4j_pass`)
   * **PostgreSQL:** Port `5432`

---

## 5. Tài liệu kỹ thuật chi tiết
* [Đề xuất dự án & Phân công trách nhiệm](docs/PROPOSAL.md)
* [Đặc tả API Contract giữa các bên](docs/API_CONTRACT.md)
* [Quy định nhánh Git & Nhịp làm việc hàng tuần](docs/GIT_WORKFLOW.md)
* [Đặc tả lược đồ CSDL Neo4j & PostgreSQL](docs/DATABASE_SCHEMA.md)
* [Kế hoạch chi tiết 12 tuần của nhóm](docs/WEEKLY_PLAN.md)

