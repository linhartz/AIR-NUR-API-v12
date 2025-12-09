from pydantic import BaseModel, Field

class RSZInputModel(BaseModel):
    stability: float = Field(0.0, ge=0.0, le=1.0)
    action_weight: float = Field(0.0, ge=0.0, le=1.0)
    cycle_alignment: float = Field(0.0, ge=0.0, le=1.0)
