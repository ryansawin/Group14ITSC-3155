from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .customers import Customer
from .recipes import Recipe


class ReviewBase(BaseModel):
    rating: int
    comment: Optional[str] = None


class ReviewCreate(ReviewBase):
    customer_id: int
    recipe_id: int


class ReviewUpdate(BaseModel):
    customer_id: Optional[int] = None
    recipe_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None


class Review(ReviewBase):
    id: int
    created_at: datetime
    customer: Customer = None
    recipe: Recipe = None

    class ConfigDict:
        from_attributes = True
