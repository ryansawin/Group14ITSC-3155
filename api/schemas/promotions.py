from pydantic import BaseModel
from datetime import date


class PromotionBase(BaseModel):
    code: str
    expiry_date: date


class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    code: str
    expiry_date: date


class Promotion(PromotionBase):
    id: int


    class ConfigDict:
        from_attributes = True