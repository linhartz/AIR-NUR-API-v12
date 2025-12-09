from app.domain.air.model import AIRInputModel
from app.core.coeffs import COEFFICIENTS

def compute_air(inp: AIRInputModel) -> float:
    w = COEFFICIENTS.get("air_weights", {})
    score = (
        w.get("hhi", 0.2) * float(inp.hhi or 0.0) +
        w.get("nur", 0.15) * float(inp.nur or 0.0) +
        w.get("rsz", 0.10) * float(inp.rsz or 0.0) +
        w.get("cycles", 0.15) * float(inp.cycles or 0.0) +
        w.get("hope", 0.20) * float(inp.hope or 0.0) +
        w.get("cr", 0.20) * float(inp.cr or 0.0)
    )
    return round(float(max(0.0, min(1.0, score))), 6)
