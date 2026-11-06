CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Users
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user' CHECK (role IN ('user', 'guardian', 'admin', 'moderator')),
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'suspended', 'banned')),
    avatar_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. User Devices
CREATE TABLE IF NOT EXISTS user_devices (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    device_uuid VARCHAR(100) NOT NULL,
    fcm_token TEXT NOT NULL UNIQUE,
    device_model VARCHAR(100),
    os_name VARCHAR(30) DEFAULT 'android' CHECK (os_name IN ('android', 'ios', 'web')),
    os_version VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    last_active_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Family Guardians
CREATE TABLE IF NOT EXISTS family_guardians (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    guardian_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    relationship VARCHAR(50) NOT NULL,
    is_confirmed BOOLEAN DEFAULT TRUE,
    can_receive_sos BOOLEAN DEFAULT TRUE,
    can_view_history BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_user_guardian UNIQUE(user_id, guardian_id)
);

-- 4. SOS Alerts
CREATE TABLE IF NOT EXISTS sos_alerts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    trigger_source VARCHAR(50) NOT NULL CHECK (trigger_source IN ('CALL_SCREENER', 'MANUAL_BUTTON', 'RISKY_TRANSACTION')),
    suspicious_value VARCHAR(100),
    risk_score DOUBLE PRECISION NOT NULL,
    lat DOUBLE PRECISION,
    lng DOUBLE PRECISION,
    address TEXT,
    status VARCHAR(30) DEFAULT 'ACTIVE' CHECK (status IN ('ACTIVE', 'ACKNOWLEDGED', 'RESOLVED', 'FALSE_ALARM')),
    resolved_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. SOS Alert Recipients
CREATE TABLE IF NOT EXISTS sos_alert_recipients (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    alert_id UUID NOT NULL REFERENCES sos_alerts(id) ON DELETE CASCADE,
    guardian_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    fcm_message_id VARCHAR(100),
    delivery_status VARCHAR(30) DEFAULT 'PENDING' CHECK (delivery_status IN ('PENDING', 'SENT', 'DELIVERED', 'FAILED')),
    delivered_at TIMESTAMP WITH TIME ZONE,
    read_at TIMESTAMP WITH TIME ZONE
);

-- 6. Banks
CREATE TABLE IF NOT EXISTS banks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    bin VARCHAR(10) UNIQUE NOT NULL,
    code VARCHAR(20) UNIQUE NOT NULL,
    short_name VARCHAR(50) NOT NULL,
    name VARCHAR(200) NOT NULL,
    logo_url TEXT,
    is_napas_supported BOOLEAN DEFAULT TRUE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 7. Bank Accounts
CREATE TABLE IF NOT EXISTS bank_accounts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    bank_id UUID NOT NULL REFERENCES banks(id) ON DELETE RESTRICT,
    account_number VARCHAR(50) NOT NULL,
    account_holder_name VARCHAR(150),
    risk_level VARCHAR(20) DEFAULT 'UNKNOWN' CHECK (risk_level IN ('UNKNOWN', 'SAFE', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')),
    total_reports INT DEFAULT 0,
    is_blacklisted BOOLEAN DEFAULT FALSE,
    first_reported_at TIMESTAMP WITH TIME ZONE,
    last_reported_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_bank_account UNIQUE(bank_id, account_number)
);

-- 8. Phone Numbers
CREATE TABLE IF NOT EXISTS phone_numbers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    carrier VARCHAR(50),
    telecom_type VARCHAR(30) DEFAULT 'MOBILE' CHECK (telecom_type IN ('MOBILE', 'LANDLINE', 'VOIP', 'HOTLINE')),
    risk_level VARCHAR(20) DEFAULT 'UNKNOWN' CHECK (risk_level IN ('UNKNOWN', 'SAFE', 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')),
    total_reports INT DEFAULT 0,
    is_blacklisted BOOLEAN DEFAULT FALSE,
    first_reported_at TIMESTAMP WITH TIME ZONE,
    last_reported_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 9. Malicious Domains
CREATE TABLE IF NOT EXISTS malicious_domains (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    domain VARCHAR(255) UNIQUE NOT NULL,
    original_url TEXT,
    threat_type VARCHAR(50) NOT NULL CHECK (threat_type IN ('PHISHING', 'FAKE_BANK', 'MALWARE', 'SCAM_ECOMMERCE')),
    target_brand VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    reported_count INT DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 10. Incident Categories
CREATE TABLE IF NOT EXISTS incident_categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    base_penalty_score DOUBLE PRECISION DEFAULT 25.0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 11. Scam Reports
CREATE TABLE IF NOT EXISTS scam_reports (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    reporter_id UUID REFERENCES users(id) ON DELETE SET NULL,
    category_id UUID REFERENCES incident_categories(id) ON DELETE RESTRICT,
    entity_type VARCHAR(30) NOT NULL CHECK (entity_type IN ('bank_account', 'phone_number', 'domain', 'social_profile')),
    entity_value VARCHAR(255) NOT NULL,
    bank_account_id UUID REFERENCES bank_accounts(id) ON DELETE SET NULL,
    phone_number_id UUID REFERENCES phone_numbers(id) ON DELETE SET NULL,
    domain_id UUID REFERENCES malicious_domains(id) ON DELETE SET NULL,
    title VARCHAR(250) NOT NULL,
    description TEXT NOT NULL,
    scam_amount NUMERIC(15, 2) DEFAULT 0.0,
    status VARCHAR(30) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'APPROVED', 'REJECTED', 'DISPUTED')),
    reviewer_id UUID REFERENCES users(id) ON DELETE SET NULL,
    reviewer_note TEXT,
    reviewed_at TIMESTAMP WITH TIME ZONE,
    lat DOUBLE PRECISION,
    lng DOUBLE PRECISION,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 12. Evidence Attachments
CREATE TABLE IF NOT EXISTS evidence_attachments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_id UUID NOT NULL REFERENCES scam_reports(id) ON DELETE CASCADE,
    file_type VARCHAR(50) NOT NULL CHECK (file_type IN ('BANK_TRANSFER_RECEIPT', 'CHAT_LOG_SCREENSHOT', 'CONTRACT_IMAGE', 'VOICE_RECORDING')),
    file_url TEXT NOT NULL,
    file_size_bytes BIGINT,
    ocr_extracted_text TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 13. Image Hashes
CREATE TABLE IF NOT EXISTS image_hashes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_id UUID NOT NULL REFERENCES scam_reports(id) ON DELETE CASCADE,
    attachment_id UUID REFERENCES evidence_attachments(id) ON DELETE SET NULL,
    phash VARCHAR(64) NOT NULL,
    image_url TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 14. Lookup History
CREATE TABLE IF NOT EXISTS lookup_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    entity_type VARCHAR(30) NOT NULL CHECK (entity_type IN ('bank_account', 'phone_number', 'domain', 'vietqr', 'image')),
    entity_value VARCHAR(255) NOT NULL,
    risk_score DOUBLE PRECISION NOT NULL,
    risk_level VARCHAR(30) NOT NULL CHECK (risk_level IN ('SAFE', 'CAUTION', 'HIGH_RISK', 'CRITICAL')),
    penalty_breakdown JSONB,
    ip_address VARCHAR(45),
    lat DOUBLE PRECISION,
    lng DOUBLE PRECISION,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 15. Disputes
CREATE TABLE IF NOT EXISTS disputes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    report_id UUID NOT NULL REFERENCES scam_reports(id) ON DELETE CASCADE,
    applicant_id UUID REFERENCES users(id) ON DELETE SET NULL,
    applicant_name VARCHAR(100) NOT NULL,
    applicant_phone VARCHAR(20) NOT NULL,
    citizen_id VARCHAR(20) NOT NULL,
    reason TEXT NOT NULL,
    citizen_id_front_url TEXT NOT NULL,
    citizen_id_back_url TEXT NOT NULL,
    bank_confirmation_url TEXT,
    status VARCHAR(30) DEFAULT 'PROCESSING' CHECK (status IN ('PROCESSING', 'ACCEPTED', 'REJECTED')),
    reviewer_id UUID REFERENCES users(id) ON DELETE SET NULL,
    resolution_note TEXT,
    resolved_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 16. Audit Logs
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    actor_id UUID REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(50) NOT NULL,
    target_table VARCHAR(50) NOT NULL,
    target_id UUID NOT NULL,
    old_values JSONB,
    new_values JSONB,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 17. System Configs
CREATE TABLE IF NOT EXISTS system_configs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    config_key VARCHAR(100) UNIQUE NOT NULL,
    config_value VARCHAR(255) NOT NULL,
    value_type VARCHAR(20) DEFAULT 'FLOAT' CHECK (value_type IN ('FLOAT', 'INT', 'STRING', 'BOOLEAN', 'JSON')),
    description TEXT,
    updated_by UUID REFERENCES users(id) ON DELETE SET NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_users_phone ON users(phone);
CREATE INDEX IF NOT EXISTS idx_user_devices_token ON user_devices(fcm_token);
CREATE INDEX IF NOT EXISTS idx_bank_accounts_num ON bank_accounts(account_number);
CREATE INDEX IF NOT EXISTS idx_phone_numbers_num ON phone_numbers(phone_number);
CREATE INDEX IF NOT EXISTS idx_malicious_domains_domain ON malicious_domains(domain);
CREATE INDEX IF NOT EXISTS idx_scam_reports_entity ON scam_reports(entity_type, entity_value);
CREATE INDEX IF NOT EXISTS idx_scam_reports_status ON scam_reports(status);
CREATE INDEX IF NOT EXISTS idx_image_hashes_phash ON image_hashes(phash);
CREATE INDEX IF NOT EXISTS idx_lookup_history_val ON lookup_history(entity_value);
CREATE INDEX IF NOT EXISTS idx_audit_logs_actor ON audit_logs(actor_id);
