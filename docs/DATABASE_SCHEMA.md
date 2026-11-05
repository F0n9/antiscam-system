# THIẾT KẾ CƠ SỞ DỮ LIỆU (DATABASE SCHEMA)

Hệ thống kết hợp mô hình lưu trữ kép (Hybrid Database Architecture):
1. **PostgreSQL 16:** Lưu trữ dữ liệu quan hệ, thông tin tài khoản, phân quyền, hàng đợi kiểm duyệt và lịch sử báo cáo.
2. **Neo4j 5.18:** Lưu trữ mạng lưới đồ thị liên kết thực thể, phục vụ truy vết đa bước và thuật toán tính điểm tín nhiệm.

---

## 1. Cơ sở dữ liệu quan hệ (PostgreSQL)

```sql
-- Kích hoạt extension UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Bảng người dùng
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user' CHECK (role IN ('user', 'guardian', 'admin')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bảng liên kết người bảo hộ gia đình (Family SOS)
CREATE TABLE family_guardians (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    guardian_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    relationship VARCHAR(50) NOT NULL, -- "Cha/Mẹ", "Con cái", "Vợ/Chồng"
    is_confirmed BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_guardian UNIQUE(user_id, guardian_id)
);

-- 3. Bảng báo cáo lừa đảo (Tố cáo từ cộng đồng)
CREATE TABLE scam_reports (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    reporter_id UUID REFERENCES users(id) ON DELETE SET NULL,
    entity_type VARCHAR(30) NOT NULL CHECK (entity_type IN ('bank_account', 'phone_number', 'social_profile')),
    entity_value VARCHAR(100) NOT NULL,
    bank_code VARCHAR(20), -- Mã định danh ngân hàng nếu entity_type = bank_account
    incident_type VARCHAR(50) NOT NULL CHECK (incident_type IN ('DEPOSIT_SCAM', 'RECRUIT_SCAM', 'IMPERSONATION_SCAM')),
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    evidence_image_url TEXT NOT NULL, -- Bắt buộc có ủy nhiệm chi
    status VARCHAR(30) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'APPROVED', 'REJECTED', 'DISPUTED')),
    reviewer_id UUID REFERENCES users(id),
    reviewed_at TIMESTAMP WITH TIME ZONE,
    lat DOUBLE PRECISION,
    lng DOUBLE PRECISION,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Bảng mã băm tri giác hình ảnh (pHash index)
CREATE TABLE image_hashes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_id UUID NOT NULL REFERENCES scam_reports(id) ON DELETE CASCADE,
    phash VARCHAR(64) NOT NULL, -- Chuỗi hex 64-bit của pHash
    image_url TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Bảng khiếu nại & minh oan
CREATE TABLE disputes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_id UUID NOT NULL REFERENCES scam_reports(id) ON DELETE CASCADE,
    applicant_name VARCHAR(100) NOT NULL,
    applicant_phone VARCHAR(20) NOT NULL,
    reason TEXT NOT NULL,
    citizen_id_front_url TEXT NOT NULL,
    citizen_id_back_url TEXT NOT NULL,
    status VARCHAR(30) DEFAULT 'PROCESSING' CHECK (status IN ('PROCESSING', 'ACCEPTED', 'REJECTED')),
    resolved_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Tạo chỉ mục tìm kiếm
CREATE INDEX idx_reports_entity ON scam_reports(entity_type, entity_value);
CREATE INDEX idx_reports_location ON scam_reports(lat, lng);
CREATE INDEX idx_image_hashes_phash ON image_hashes(phash);
```

---

## 2. Cơ sở dữ liệu đồ thị (Neo4j)

### 2.1. Nhãn nút (Node Labels)
* `:PhoneNumber` { `phone`: String, `carrier`: String, `risk_score`: Float }
* `:BankAccount` { `account_number`: String, `bank_bin`: String, `bank_name`: String, `account_name`: String }
* `:ScamReport` { `report_id`: String, `incident_type`: String, `is_verified`: Boolean, `created_at`: String }
* `:ImagePhash` { `hash_value`: String }

### 2.2. Quan hệ (Relationships)
* `(:PhoneNumber)-[:USED_TO_RECEIVE]->(:BankAccount)`
* `(:ScamReport)-[:TARGETS_ACCOUNT]->(:BankAccount)`
* `(:ScamReport)-[:TARGETS_PHONE]->(:PhoneNumber)`
* `(:ScamReport)-[:CONTAINS_IMAGE]->(:ImagePhash)`
* `(:PhoneNumber)-[:SHARED_CONTACT]->(:PhoneNumber)`

### 2.3. Lệnh tạo ràng buộc & Chỉ mục (Cypher DDL)
Chạy các lệnh này trong Neo4j Browser (`http://localhost:7474`):

```cypher
// Ràng buộc duy nhất (Unique Constraints)
CREATE CONSTRAINT unique_phone IF NOT EXISTS
FOR (p:PhoneNumber) REQUIRE p.phone IS UNIQUE;

CREATE CONSTRAINT unique_bank_account IF NOT EXISTS
FOR (b:BankAccount) REQUIRE (b.account_number, b.bank_bin) IS UNIQUE;

CREATE CONSTRAINT unique_report IF NOT EXISTS
FOR (r:ScamReport) REQUIRE r.report_id IS UNIQUE;

CREATE CONSTRAINT unique_phash IF NOT EXISTS
FOR (i:ImagePhash) REQUIRE i.hash_value IS UNIQUE;
```

### 2.4. Mẫu truy vấn Cypher cốt lõi

#### Truy vết liên kết đến nút vi phạm trong phạm vi 3 bước (Bán kính duyệt đồ thị)
```cypher
MATCH (start:BankAccount {account_number: $account_number, bank_bin: $bank_bin})
MATCH path = shortestPath((start)-[*..3]-(scam:ScamReport {is_verified: true}))
RETURN path, length(path) AS hops, scam.report_id AS report_id
ORDER BY hops ASC
LIMIT 1;
```

#### Xuất toàn bộ cụm đồ thị liên kết phục vụ vẽ cây Cytoscape.js
```cypher
MATCH (target:BankAccount {account_number: $account_number})
CALL apoc.path.subgraphAll(target, {maxLevel: 2})
YIELD nodes, relationships
RETURN nodes, relationships;
```
