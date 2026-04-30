from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from .order_details import OrderDetail


class OrderBase(BaseModel):
    customer_name: str
    customer_id: int
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_id: Optional[int] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
