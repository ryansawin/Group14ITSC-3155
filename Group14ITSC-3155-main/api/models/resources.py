from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False, default=0.0)
    unit = Column(String(20), nullable=False)

    recipes = relationship("Recipe", back_populates="resource")
