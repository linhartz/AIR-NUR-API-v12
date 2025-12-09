from pydantic import BaseModel, Field

class AIRInputModel(BaseModel):
    hhi: float = Field(0.0, ge=0.0, le=1.0)
    nur: float = Field(0.0, ge=0.0, le=1.0)
    rsz: float = Field(0.0, ge=0.0, le=1.0)
    cycles: float = Field(0.0, ge=0.0, le=1.0)
    hope: float = Field(0.0, ge=0.0, le=1.0)
    cr: float = Field(0.0, ge=0.0, le=1.0)
