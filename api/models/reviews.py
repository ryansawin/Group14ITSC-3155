from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(300), nullable=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.now)

    customer = relationship("Customer", back_populates="reviews")
    recipe = relationship("Recipe", back_populates="reviews")
