from fastapi import APIRouter
from app.domain.air import service

router = APIRouter(prefix="/air", tags=["air"])

@router.get("/")
def get_air_data():
    return {"message": "Air data endpoint"}
