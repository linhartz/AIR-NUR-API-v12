from app.domain.nur.model import NURInputModel

def compute_nur(inp: NURInputModel) -> float:
    # (novelty+reflection)/2 * severity
    try:
        score = ((inp.novelty + inp.reflection) / 2.0) * inp.severity
        return round(float(score), 6)
    except Exception:
        return 0.0
