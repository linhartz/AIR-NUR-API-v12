from fastapi import APIRouter

router = APIRouter(prefix="/debug", tags=["debug"])

@router.get("/")
def debug_info():
    return {"message": "Debug endpoint"}
