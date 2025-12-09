from fastapi import APIRouter
from app.domain.nur.model import NURInputModel
from app.domain.nur.service import compute_nur

router = APIRouter(prefix="/nur", tags=["nur"])

@router.post("/compute", summary="Compute NUR index")
def compute(payload: NURInputModel):
    val = compute_nur(payload)
    return {"nur": val}
