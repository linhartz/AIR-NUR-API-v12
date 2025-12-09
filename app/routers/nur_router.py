from fastapi import APIRouter
from app.domain.nur import service

router = APIRouter(prefix="/nur", tags=["nur"])

@router.get("/")
def get_nur_data():
    return {"message": "NUR data endpoint"}
