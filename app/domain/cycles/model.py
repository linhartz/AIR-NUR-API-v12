from pydantic import BaseModel, Field

class CyclesInputModel(BaseModel):
    economic: float = Field(0.0, ge=0.0, le=1.0)
    social: float = Field(0.0, ge=0.0, le=1.0)
    institutional: float = Field(0.0, ge=0.0, le=1.0)
