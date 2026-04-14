from sqlalchemy import Column, Integer, String, Date
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True)
    code = Column(String(50), nullable=False)
    expiry_date = Column(Date, nullable=False)
