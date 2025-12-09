from pydantic import BaseModel, Field

class CRInputModel(BaseModel):
    institutional_intensity: float = Field(0.0, ge=0.0)
    individual_intensity: float = Field(0.0, ge=0.0)
    confidence: float = Field(0.0, ge=0.0, le=1.0)
    vector_coherence: float = Field(0.0, ge=0.0, le=1.0)
