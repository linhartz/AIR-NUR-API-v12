from fastapi import APIRouter
from app.domain.cycles import service

router = APIRouter(prefix="/cycles", tags=["cycles"])

@router.get("/")
def get_cycles_data():
    return {"message": "Cycles data endpoint"}
