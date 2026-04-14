from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str


class CustomerCreate(CustomerBase):
    phone: str
    email: str
    address: str
    card_type: str
    card_number: str

class CustomerUpdate(BaseModel):
    name: str
    phone: str
    email: str
    address: str
    card_type: str
    card_number: str


class Customer(CustomerBase):
    id: int


    class ConfigDict:
        from_attributes = True