# Thiết kế cơ sở dữ liệu (Database Schema)

Hệ thống kết hợp mô hình lưu trữ kép:
1. **PostgreSQL 16:** Quản lý dữ liệu người dùng, thiết bị, liên kết gia đình SOS, tố cáo và nhật ký sự cố.
2. **Neo4j 5.18:** Mô hình hóa đồ thị liên kết thực thể (*Số điện thoại, Số tài khoản, Mạng xã hội, Mã băm ảnh, Báo cáo vi phạm*).

---

## 1. Cơ sở dữ liệu quan hệ (PostgreSQL)

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

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

CREATE TABLE user_devices (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    fcm_token TEXT NOT NULL UNIQUE,
    device_model VARCHAR(100),
    os_version VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE family_guardians (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    guardian_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    relationship VARCHAR(50) NOT NULL,
    is_confirmed BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_guardian UNIQUE(user_id, guardian_id)
);

CREATE TABLE sos_alerts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    guardian_id UUID REFERENCES users(id) ON DELETE SET NULL,
    trigger_reason VARCHAR(100) NOT NULL,
    suspicious_value VARCHAR(100) NOT NULL,
    risk_score DOUBLE PRECISION NOT NULL,
    lat DOUBLE PRECISION,
    lng DOUBLE PRECISION,
    status VARCHAR(30) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'ACKNOWLEDGED', 'RESOLVED', 'FALSE_ALARM')),
    acknowledged_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scam_reports (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    reporter_id UUID REFERENCES users(id) ON DELETE SET NULL,
    entity_type VARCHAR(30) NOT NULL CHECK (entity_type IN ('bank_account', 'phone_number', 'social_profile')),
    entity_value VARCHAR(100) NOT NULL,
    bank_code VARCHAR(20),
    incident_type VARCHAR(50) NOT NULL CHECK (incident_type IN ('DEPOSIT_SCAM', 'RECRUIT_SCAM', 'IMPERSONATION_SCAM')),
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    evidence_image_url TEXT NOT NULL,
    status VARCHAR(30) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'APPROVED', 'REJECTED', 'DISPUTED')),
    reviewer_id UUID REFERENCES users(id),
    reviewed_at TIMESTAMP WITH TIME ZONE,
    lat DOUBLE PRECISION,
    lng DOUBLE PRECISION,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE image_hashes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_id UUID NOT NULL REFERENCES scam_reports(id) ON DELETE CASCADE,
    phash VARCHAR(64) NOT NULL,
    image_url TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

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

CREATE TABLE lookup_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    entity_type VARCHAR(30) NOT NULL,
    entity_value VARCHAR(100) NOT NULL,
    risk_score DOUBLE PRECISION NOT NULL,
    risk_level VARCHAR(20) NOT NULL,
    lat DOUBLE PRECISION,
    lng DOUBLE PRECISION,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_reports_entity ON scam_reports(entity_type, entity_value);
CREATE INDEX idx_reports_location ON scam_reports(lat, lng);
CREATE INDEX idx_image_hashes_phash ON image_hashes(phash);
CREATE INDEX idx_user_devices_token ON user_devices(fcm_token);
CREATE INDEX idx_sos_alerts_user ON sos_alerts(user_id, status);
CREATE INDEX idx_lookup_history_entity ON lookup_history(entity_value);
```

---

## 2. Cơ sở dữ liệu đồ thị (Neo4j)

### 2.1. Nhãn nút (Node Labels)
* `:PhoneNumber` { `phone`, `carrier`, `risk_score` }
* `:BankAccount` { `account_number`, `bank_bin`, `bank_name`, `account_name` }
* `:SocialProfile` { `profile_id`, `platform`, `profile_name`, `profile_url` }
* `:ScamReport` { `report_id`, `incident_type`, `is_verified`, `created_at` }
* `:ImagePhash` { `hash_value` }

### 2.2. Quan hệ (Relationships)

```mermaid
erDiagram
    PhoneNumber ||--o{ BankAccount : "USED_TO_RECEIVE"
    SocialProfile ||--o{ BankAccount : "USES_ACCOUNT"
    SocialProfile ||--o{ PhoneNumber : "USES_PHONE"
    PhoneNumber ||--o{ PhoneNumber : "SHARED_CONTACT"
    ScamReport ||--o{ BankAccount : "TARGETS_ACCOUNT"
    ScamReport ||--o{ PhoneNumber : "TARGETS_PHONE"
    ScamReport ||--o{ SocialProfile : "TARGETS_PROFILE"
    ScamReport ||--o{ ImagePhash : "CONTAINS_IMAGE"
```

### 2.3. Ràng buộc toàn vẹn (Cypher DDL)

```cypher
CREATE CONSTRAINT unique_phone IF NOT EXISTS
FOR (p:PhoneNumber) REQUIRE p.phone IS UNIQUE;

CREATE CONSTRAINT unique_bank_account IF NOT EXISTS
FOR (b:BankAccount) REQUIRE (b.account_number, b.bank_bin) IS UNIQUE;

CREATE CONSTRAINT unique_social_profile IF NOT EXISTS
FOR (s:SocialProfile) REQUIRE s.profile_id IS UNIQUE;

CREATE CONSTRAINT unique_report IF NOT EXISTS
FOR (r:ScamReport) REQUIRE r.report_id IS UNIQUE;

CREATE CONSTRAINT unique_phash IF NOT EXISTS
FOR (i:ImagePhash) REQUIRE i.hash_value IS UNIQUE;
```

### 2.4. Mẫu truy vấn chính

#### Truy vết đường đi ngắn nhất đến mắt xích lừa đảo trong phạm vi 3 bước
```cypher
MATCH (start:BankAccount {account_number: $account_number, bank_bin: $bank_bin})
MATCH path = shortestPath((start)-[*..3]-(scam:ScamReport {is_verified: true}))
RETURN path, length(path) AS hops, scam.report_id AS report_id
ORDER BY hops ASC
LIMIT 1;
```

#### Xuất mạng lưới phục vụ vẽ đồ thị Cytoscape.js
```cypher
MATCH (target:BankAccount {account_number: $account_number, bank_bin: $bank_bin})
CALL apoc.path.subgraphAll(target, {maxLevel: 2})
YIELD nodes, relationships
RETURN nodes, relationships;
```
