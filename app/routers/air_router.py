from fastapi import APIRouter
from app.domain.air.model import AIRInputModel
from app.domain.air.service import compute_air

router = APIRouter(prefix="/air", tags=["air"])

@router.post("/compute", summary="Compute AIR composite score")
def compute(payload: AIRInputModel):
    val = compute_air(payload)
    return {"air": val}
