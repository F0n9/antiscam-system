-- ============================================================================
-- SCRIPT KHỞI TẠO TỰ ĐỘNG CƠ SỞ DỮ LIỆU POSTGRESQL (ANTISCAM PLATFORM)
-- Tự động chạy khi khởi động container lần đầu tiên
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Bảng người dùng
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user' CHECK (role IN ('user', 'guardian', 'admin')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Bảng thiết bị người dùng (FCM Token phục vụ thông báo SOS)
CREATE TABLE IF NOT EXISTS user_devices (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    fcm_token TEXT NOT NULL UNIQUE,
    device_model VARCHAR(100),
    os_version VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Bảng liên kết bảo hộ gia đình
CREATE TABLE IF NOT EXISTS family_guardians (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    guardian_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    relationship VARCHAR(50) NOT NULL,
    is_confirmed BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_guardian UNIQUE(user_id, guardian_id)
);

-- 4. Bảng nhật ký sự cố khẩn cấp SOS
CREATE TABLE IF NOT EXISTS sos_alerts (
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

-- 5. Bảng báo cáo lừa đảo từ cộng đồng
CREATE TABLE IF NOT EXISTS scam_reports (
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

-- 6. Bảng mã băm tri giác hình ảnh gian lận
CREATE TABLE IF NOT EXISTS image_hashes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_id UUID NOT NULL REFERENCES scam_reports(id) ON DELETE CASCADE,
    phash VARCHAR(64) NOT NULL,
    image_url TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 7. Bảng khiếu nại minh oan chính chủ
CREATE TABLE IF NOT EXISTS disputes (
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

-- 8. Bảng lịch sử tra cứu của người dùng
CREATE TABLE IF NOT EXISTS lookup_history (
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

-- Tạo chỉ mục tìm kiếm
CREATE INDEX IF NOT EXISTS idx_reports_entity ON scam_reports(entity_type, entity_value);
CREATE INDEX IF NOT EXISTS idx_reports_location ON scam_reports(lat, lng);
CREATE INDEX IF NOT EXISTS idx_image_hashes_phash ON image_hashes(phash);
CREATE INDEX IF NOT EXISTS idx_user_devices_token ON user_devices(fcm_token);
CREATE INDEX IF NOT EXISTS idx_sos_alerts_user ON sos_alerts(user_id, status);
CREATE INDEX IF NOT EXISTS idx_lookup_history_entity ON lookup_history(entity_value);
