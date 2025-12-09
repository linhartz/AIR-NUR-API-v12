from app.domain.cycles.model import CyclesInputModel

def compute_cycles(inp: CyclesInputModel) -> float:
    try:
        score = (inp.economic + inp.social + inp.institutional) / 3.0
        return round(float(score), 6)
    except Exception:
        return 0.0
