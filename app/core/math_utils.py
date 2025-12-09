import math

def compress_atan_01(x: float, scale: float = 1.0) -> float:
    """Compress to 0..1 using arctan soft cap."""
    try:
        return float((math.atan(x * scale) * 2) / math.pi)
    except Exception:
        return 0.0
