from fastapi import APIRouter
from app.domain.cycles.model import CyclesInputModel
from app.domain.cycles.service import compute_cycles

router = APIRouter(prefix="/cycles", tags=["cycles"])

@router.post("/compute", summary="Compute Cycles index")
def compute(payload: CyclesInputModel):
    val = compute_cycles(payload)
    return {"cycles": val}
