from pydantic import BaseModel, Field

class NURInputModel(BaseModel):
    novelty: float = Field(0.0, ge=0.0, le=1.0, description="novelty 0..1")
    reflection: float = Field(0.0, ge=0.0, le=1.0, description="reflection 0..1")
    severity: float = Field(0.0, ge=0.0, le=1.0, description="severity 0..1")
