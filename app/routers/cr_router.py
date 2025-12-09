from fastapi import APIRouter
from app.domain.cr.model import CRInputModel
from app.domain.cr.service import compute_cr

router = APIRouter(prefix="/cr", tags=["cr"])

@router.post("/compute", summary="Compute Chaotic Risk")
def compute(payload: CRInputModel):
    val = compute_cr(payload)
    return {"chaotic_risk": val}
