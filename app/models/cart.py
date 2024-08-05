from . import BASE
from sqlalchemy import Column, Integer, ForeignKey


class Cart(BASE):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey("user.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)