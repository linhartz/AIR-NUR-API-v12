from app.domain.rsz.model import RSZInputModel

def compute_rsz(inp: RSZInputModel) -> float:
    try:
        score = inp.stability * (1.0 - inp.action_weight) * inp.cycle_alignment
        return round(float(score), 6)
    except Exception:
        return 0.0
