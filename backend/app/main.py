from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AntiScam Platform API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "healthy",
        "service": "antiscam-backend",
        "version": "1.0.0"
    }

@app.get("/api/v1/mock/verify-demo", tags=["Mock"])
async def mock_verify_demo(account_number: str = "1029384756"):
    return {
        "success": True,
        "data": {
            "entity_value": account_number,
            "entity_type": "bank_account",
            "credit_score": 18.5,
            "risk_level": "CRITICAL",
            "penalty_breakdown": {
                "graph_penalty": 40.0,
                "payment_penalty": 25.0,
                "psychology_penalty": 16.5,
                "image_penalty": 0.0
            },
            "what_if_scenarios": [
                "Bước 1: Đối tượng tạo áp lực khan hiếm phòng trọ, yêu cầu chuyển cọc 1 triệu trong 15 phút.",
                "Bước 2: Sau khi nạn nhân chuyển khoản, đối tượng cắt liên lạc hoặc yêu cầu nạp thêm tiền làm hợp đồng.",
                "Bước 3: Chặn số điện thoại, khóa tài khoản Facebook/Zalo và xóa toàn bộ tin nhắn."
            ]
        }
    }
