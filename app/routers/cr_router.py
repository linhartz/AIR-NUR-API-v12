from fastapi import APIRouter
from app.domain.cr import service

router = APIRouter(prefix="/cr", tags=["cr"])

@router.get("/")
def get_cr_data():
    return {"message": "CR data endpoint"}
