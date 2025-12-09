from app.domain.cr.model import CRInputModel
from app.core.math_utils import compress_atan_01
from app.core.coeffs import COEFFICIENTS

def compute_cr(inp: CRInputModel) -> dict:
    cfg = COEFFICIENTS.get("cr_config", {})
    w_inst = cfg.get("w_institutional", 1.5)
    w_ind = cfg.get("w_individual", 1.0)
    scale = cfg.get("scale", 0.8)
    damp = cfg.get("global_dampen", 0.9)

    inst = float(inp.institutional_intensity or 0.0) * w_inst
    ind = float(inp.individual_intensity or 0.0) * w_ind
    raw = inst + ind

    norm = compress_atan_01(raw, scale=scale)
    modulated = norm * (1.0 + float(inp.vector_coherence or 0.0)) * (1.0 + float(inp.confidence or 0.0))
    cr_scalar = max(0.0, min(1.0, modulated * damp))

    components = {
        "sum_institutional": round(inst, 6),
        "sum_individual": round(ind, 6),
        "raw": round(raw, 6),
        "normalized": round(norm, 6),
        "modulated": round(modulated, 6),
        "cr_scalar": round(cr_scalar, 6)
    }
    return {"cr_scalar": round(cr_scalar, 6), "components": components}
