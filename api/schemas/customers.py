from typing import Optional
from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str
    card_type: str
    card_number: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    card_type: Optional[str] = None
    card_number: Optional[str] = None


class Customer(CustomerBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
