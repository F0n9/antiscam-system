# MÁY CHỦ ỨNG DỤNG BACKEND (FASTAPI)

Thành phần xử lý nghiệp vụ trung tâm cho Hệ thống AntiScam (do **Module A - Đặng Quang Tiến** và **Module B - Hoàng Khang** phụ trách).

---

## 1. Yêu cầu môi trường
* Python 3.11+
* Docker & Docker Compose (nếu chạy cơ sở dữ liệu qua container)

---

## 2. Hướng dẫn cài đặt và chạy máy chủ cục bộ

### Cách 1: Chạy trực tiếp trên máy (Khuyên dùng khi lập trình API)
1. **Di chuyển vào thư mục backend:**
   ```bash
   cd backend
   ```
2. **Khởi tạo môi trường ảo Python (virtual environment):**
   ```bash
   python -m venv .venv
   # Kích hoạt trên Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # Kích hoạt trên Linux/macOS:
   source .venv/bin/activate
   ```
3. **Cài đặt các gói phụ thuộc:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. **Khởi chạy máy chủ FastAPI với tính năng tự động tải lại (hot-reload):**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```
5. **Truy cập tài liệu API tự động sinh (Swagger UI):**
   Mở trình duyệt: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Cách 2: Chạy thông qua Docker Compose từ thư mục gốc
Tại thư mục gốc `antiscam-system`:
```bash
docker compose up -d backend
```

---

## 3. Cấu trúc mã nguồn `backend/`
* `app/api/v1/`: Chứa các router API phân chia theo phân hệ (`auth`, `verify`, `reports`, `sos`, `graph`).
* `app/core/`: Chứa cấu hình đọc từ `.env`, cài đặt bảo mật JWT, kết nối database.
* `app/models/`: Định nghĩa các Pydantic schemas (Request/Response validation) và SQLAlchemy Models.
* `app/services/`: Chứa nghiệp vụ chuyên sâu:
  * `neo4j_service.py`: Thực thi câu lệnh Cypher, duyệt đồ thị 3 bước.
  * `scoring_service.py`: Tính điểm tín nhiệm rủi ro theo công thức 4 trọng số.
  * `phash_service.py`: Tính toán mã băm tri giác và so sánh khoảng cách Hamming ảnh.

