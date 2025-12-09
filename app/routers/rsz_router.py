from fastapi import APIRouter
from app.domain.rsz.model import RSZInputModel
from app.domain.rsz.service import compute_rsz

router = APIRouter(prefix="/rsz", tags=["rsz"])

@router.post("/compute", summary="Compute RSZ index")
def compute(payload: RSZInputModel):
    val = compute_rsz(payload)
    return {"rsz": val}
