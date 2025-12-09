from fastapi import APIRouter
from app.core.coeffs import COEFFICIENTS

router = APIRouter(prefix="/debug", tags=["debug"])

@router.get("/coefficients", summary="Show model coefficients and weights")
def coefficients():
    return COEFFICIENTS
