from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class PromotionBase(BaseModel):
    code: str
    expiry_date: date


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    expiry_date: Optional[date] = None


class PromotionGenerate(BaseModel):
    prefix: str = Field(default="RETURN", min_length=1, max_length=20)
    days_valid: int = Field(default=30, ge=1, le=365)
    code_length: int = Field(default=6, ge=4, le=12)


class Promotion(PromotionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
