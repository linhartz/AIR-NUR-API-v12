from fastapi import APIRouter
from app.domain.rsz import service

router = APIRouter(prefix="/rsz", tags=["rsz"])

@router.get("/")
def get_rsz_data():
    return {"message": "RSZ data endpoint"}
