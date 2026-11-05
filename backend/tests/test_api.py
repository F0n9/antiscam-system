"""
Kiểm thử tích hợp các endpoint cơ bản của FastAPI máy chủ.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_endpoint():
    """Kiểm tra endpoint /health hoạt động bình thường."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "antiscam-backend"

def test_mock_verify_demo_endpoint():
    """Kiểm tra endpoint mock dữ liệu trả về đúng cấu trúc chuẩn."""
    response = client.get("/api/v1/mock/verify-demo?account_number=1029384756")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["entity_value"] == "1029384756"
    assert data["data"]["risk_level"] == "CRITICAL"
    assert len(data["data"]["what_if_scenarios"]) >= 3
