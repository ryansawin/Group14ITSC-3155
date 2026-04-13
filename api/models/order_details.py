from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    amount = Column(Integer, index=True, nullable=False)
    order_status = Column(String, nullable=False)
    total_price = Column(DECIMAL(precision=10, scale=2), nullable=False)

    sandwich = relationship("Sandwich", back_populates="order_details")
    order = relationship("Order", foreign_keys=[order_id])
