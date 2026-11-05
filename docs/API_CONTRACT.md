# ĐẶC TẢ GIAO DIỆN LẬP TRÌNH ỨNG DỤNG (API CONTRACT)

Tài liệu này xác lập hợp đồng dữ liệu giữa **Backend (Module A & B)** với **Web Frontend (Module C)** và **Android App (Module D)**. Tất cả các bên tuân thủ nghiêm ngặt định dạng dữ liệu bên dưới để triển khai độc lập mà không bị phụ thuộc tiến độ.

* **Base URL cục bộ:** `http://localhost:8000/api/v1`
* **Content-Type:** `application/json` (trừ các endpoint tải tệp dùng `multipart/form-data`)
* **Xác thực:** Bearer Token trong header `Authorization: Bearer <access_token>`

---

## 1. Chuẩn hóa phản hồi chung

### Phản hồi thành công (HTTP 200, 201)
```json
{
  "success": true,
  "data": { ... },
  "message": "Mô tả kết quả thực thi"
}
```

### Phản hồi thất bại (HTTP 400, 401, 403, 404, 500)
```json
{
  "success": false,
  "error": {
    "code": "MA_LOI_HE_THONG",
    "message": "Nội dung thông báo lỗi chi tiết"
  }
}
```

---

## 2. Danh mục các Endpoint cốt lõi

### 2.1. Phân hệ Xác thực (Module A)

#### `POST /auth/register`
* **Mô tả:** Đăng ký tài khoản người dùng hoặc người bảo hộ.
* **Request:**
```json
{
  "full_name": "Nguyễn Văn A",
  "phone": "0912345678",
  "email": "vana@example.com",
  "password": "Password123@",
  "role": "user" // "user" hoặc "guardian"
}
```
* **Response (HTTP 201):**
```json
{
  "success": true,
  "data": {
    "user_id": "uuid-v4-string",
    "phone": "0912345678",
    "role": "user",
    "created_at": "2026-11-06T08:00:00Z"
  },
  "message": "Đăng ký tài khoản thành công"
}
```

#### `POST /auth/login`
* **Mô tả:** Đăng nhập lấy JWT Bearer Token.
* **Request:**
```json
{
  "phone": "0912345678",
  "password": "Password123@"
}
```
* **Response (HTTP 200):**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 86400,
    "user": {
      "user_id": "uuid-v4-string",
      "full_name": "Nguyễn Văn A",
      "phone": "0912345678",
      "role": "user"
    }
  }
}
```

---

### 2.2. Phân hệ Kiểm chứng & Tính điểm tín nhiệm (Module A, B, D)

#### `POST /verify/entity`
* **Mô tả:** Kiểm tra độ an toàn của số điện thoại, tài khoản ngân hàng hoặc chuỗi văn bản trao đổi nghi vấn.
* **Request:**
```json
{
  "entity_type": "bank_account", // "bank_account", "phone_number", "content_text"
  "value": "1029384756",
  "bank_code": "970415", // Mã định danh ngân hàng (Vietinbank) nếu type = bank_account
  "content_text": "Em cọc giữ phòng trước 1 triệu nhé không người khác lấy mất" // Tùy chọn để phân tích NLP
}
```
* **Response (HTTP 200):**
```json
{
  "success": true,
  "data": {
    "entity_value": "1029384756",
    "entity_type": "bank_account",
    "credit_score": 18.5,
    "risk_level": "CRITICAL", // "SAFE" (80-100), "CAUTION" (50-79), "HIGH_RISK" (25-49), "CRITICAL" (<25)
    "penalty_breakdown": {
      "graph_penalty": 40.0,      // W_g * S_g (tối đa 40 điểm)
      "payment_penalty": 25.0,    // W_p * S_p (tối đa 25 điểm)
      "psychology_penalty": 16.5, // W_s * S_s (tối đa 20 điểm)
      "image_penalty": 0.0        // W_i * S_i (tối đa 15 điểm)
    },
    "graph_summary": {
      "has_violation_in_path": true,
      "shortest_path_hops": 1,
      "connected_reports_count": 8
    },
    "what_if_scenarios": [
      "Bước 1: Đối tượng thúc ép chuyển khoản cọc gấp với lý do có nhiều người đang hỏi thuê.",
      "Bước 2: Sau khi nhận tiền, đối tượng viện lý do chưa nhận được hoặc yêu cầu thêm phụ phí hợp đồng.",
      "Bước 3: Chặn toàn bộ liên lạc qua điện thoại và mạng xã hội, xóa tin nhắn hội thoại."
    ]
  }
}
```

#### `POST /verify/vietqr`
* **Mô tả:** Bóc tách chuỗi mã VietQR từ camera Android hoặc ảnh chụp.
* **Request:**
```json
{
  "qr_payload": "00020101021238580010A00000072701280006970415011410293847560208QRIBFTTA5303704540710000005802VN62110807DAT COC6304ABCD"
}
```
* **Response (HTTP 200):**
```json
{
  "success": true,
  "data": {
    "bank_bin": "970415",
    "bank_name": "VietinBank",
    "account_number": "1029384756",
    "amount": 1000000,
    "transfer_content": "DAT COC",
    "credit_score": 18.5,
    "risk_level": "CRITICAL"
  }
}
```

#### `POST /verify/image-phash`
* **Mô tả:** Tải ảnh phòng trọ/tuyển dụng lên để so khớp với kho ảnh lừa đảo đã ghi nhận.
* **Request:** `multipart/form-data`
  * `image`: Tệp ảnh dạng JPEG/PNG.
* **Response (HTTP 200):**
```json
{
  "success": true,
  "data": {
    "calculated_phash": "a3b2c1d4e5f60718",
    "is_duplicate_scam_image": true,
    "min_hamming_distance": 2, // Ngưỡng <= 10 kết luận trùng khớp
    "matched_report_id": "rep_987654",
    "matched_image_url": "https://storage.antiscam.vn/evidence/img_01.jpg"
  }
}
```

---

### 2.3. Phân hệ Trực quan hóa Đồ thị (Module B & C)

#### `GET /graph/entity-tree?entity_value=1029384756&max_depth=3`
* **Mô tả:** Trả về cây đồ thị định dạng chuẩn cho Cytoscape.js hiển thị trên Web Frontend.
* **Response (HTTP 200):**
```json
{
  "success": true,
  "data": {
    "elements": {
      "nodes": [
        { "data": { "id": "acc_1029384756", "label": "Tài khoản: 1029384756", "type": "BankAccount", "is_violation": true } },
        { "data": { "id": "phone_0987654321", "label": "SĐT: 0987654321", "type": "PhoneNumber", "is_violation": false } },
        { "data": { "id": "report_001", "label": "Báo cáo cọc trọ lừa đảo", "type": "ScamReport", "is_violation": true } }
      ],
      "edges": [
        { "data": { "id": "e1", "source": "phone_0987654321", "target": "acc_1029384756", "label": "USED_TO_RECEIVE" } },
        { "data": { "id": "e2", "source": "report_001", "target": "acc_1029384756", "label": "REPORTED_AGAINST" } }
      ]
    }
  }
}
```

---

### 2.4. Phân hệ Cảnh báo Khẩn cấp SOS & Phát sóng khu vực (Module A & D)

#### `POST /sos/link-guardian`
* **Mô tả:** Liên kết tài khoản người dùng với người bảo hộ trong gia đình.
* **Request:**
```json
{
  "user_phone": "0912345678",
  "guardian_phone": "0988776655",
  "relationship": "Con trai"
}
```

#### `POST /sos/trigger`
* **Mô tả:** Ứng dụng Android tự động kích hoạt báo động gửi thông báo đẩy đến người bảo hộ khi phát hiện người dùng thao tác giao dịch nguy cơ cực cao.
* **Request:**
```json
{
  "user_id": "uuid-v4-string",
  "suspicious_entity": "1029384756",
  "risk_score": 15.0,
  "incident_type": "HIGH_RISK_CALL_OR_TRANSFER",
  "lat": 10.762622,
  "lng": 106.682333
}
```
* **Response (HTTP 200):**
```json
{
  "success": true,
  "message": "Đã phát tín hiệu SOS đến 2 người bảo hộ liên kết thành công",
  "sent_time": "2026-11-06T08:05:01Z"
}
```

#### `GET /alerts/nearby?lat=10.762622&lng=106.682333&radius_km=3`
* **Mô tả:** Lấy danh sách các vụ việc lừa đảo được xác nhận gần vị trí hiện tại (phục vụ hiển thị trên Web và bắn notification cho Android).
* **Response (HTTP 200):**
```json
{
  "success": true,
  "data": [
    {
      "id": "rep_102",
      "title": "Lừa cọc phòng trọ hẻm 227 Nguyễn Văn Cừ",
      "distance_meters": 450,
      "reported_at": "2026-11-05T14:20:00Z",
      "risk_level": "CRITICAL"
    }
  ]
}
```

---

### 2.5. Phân hệ Tiếp nhận Tố cáo & Khiếu nại (Module A)

#### `POST /reports/submit`
* **Mô tả:** Gửi báo cáo tố cáo kèm ảnh biên lai ngân hàng.
* **Request:** `multipart/form-data`
  * `entity_type`: "bank_account" hoặc "phone_number"
  * `entity_value`: Giá trị bị tố cáo
  * `incident_type`: "DEPOSIT_SCAM" (Lừa cọc) hoặc "RECRUIT_SCAM" (Tuyển dụng)
  * `description`: Mô tả chi tiết hành vi
  * `evidence_image`: File ảnh ủy nhiệm chi (Bắt buộc)
* **Response (HTTP 201):**
```json
{
  "success": true,
  "data": {
    "report_id": "rep_550e8400",
    "status": "PENDING_VERIFICATION",
    "message": "Báo cáo đã được tiếp nhận và chuyển đến hàng đợi thẩm định"
  }
}
```
