"""
Kiểm thử đơn vị (Unit Test) cho công thức tính Điểm tín nhiệm rủi ro.
Công thức theo Proposal:
Score = 100 - min(100, W_g * S_g + W_p * S_p + W_i * S_i + W_s * S_s)
Trọng số: W_g = 0.40, W_p = 0.25, W_s = 0.20, W_i = 0.15
"""

def calculate_credit_score(s_g: float, s_p: float, s_s: float, s_i: float) -> tuple[float, str]:
    w_g, w_p, w_s, w_i = 0.40, 0.25, 0.20, 0.15
    total_penalty = w_g * s_g + w_p * s_p + w_s * s_s + w_i * s_i
    score = round(max(0.0, 100.0 - min(100.0, total_penalty)), 1)
    
    if score >= 80.0:
        level = "SAFE"
    elif score >= 50.0:
        level = "CAUTION"
    elif score >= 25.0:
        level = "HIGH_RISK"
    else:
        level = "CRITICAL"
        
    return score, level

def test_perfect_safe_entity():
    """Trường hợp thực thể hoàn toàn trong sạch, không có điểm phạt nào."""
    score, level = calculate_credit_score(s_g=0, s_p=0, s_s=0, s_i=0)
    assert score == 100.0
    assert level == "SAFE"

def test_critical_scam_ring():
    """Trường hợp dính toàn bộ vi phạm nặng nhất."""
    score, level = calculate_credit_score(s_g=100, s_p=100, s_s=100, s_i=100)
    assert score == 0.0
    assert level == "CRITICAL"

def test_caution_threshold():
    """Trường hợp điểm phạt trung bình (chỉ bị trừ điểm bất thường thanh toán và kịch bản nhẹ)."""
    # S_p = 60, S_s = 50 -> Penalty = 0.25*60 + 0.20*50 = 15 + 10 = 25 -> Score = 75.0
    score, level = calculate_credit_score(s_g=0, s_p=60, s_s=50, s_i=0)
    assert score == 75.0
    assert level == "CAUTION"

def test_high_risk_threshold():
    """Trường hợp có dấu hiệu nguy cơ cao (liên kết gián tiếp 2-3 bước trên đồ thị)."""
    # S_g = 80, S_p = 80 -> Penalty = 0.40*80 + 0.25*80 = 32 + 20 = 52 -> Score = 48.0
    score, level = calculate_credit_score(s_g=80, s_p=80, s_s=0, s_i=0)
    assert score == 48.0
    assert level == "HIGH_RISK"
