from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Sandwich(Base):
    __tablename__ = "sandwiches"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=False)
    ingredients = Column(String(500), nullable=False)
    dish = Column(String(100), nullable=False)
    price = Column(DECIMAL(6, 2), nullable=False, server_default="0.0")
    calories = Column(Integer, nullable=False, server_default="0")
    food_category = Column(String(100), nullable=False)

    recipes = relationship("Recipe", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")
