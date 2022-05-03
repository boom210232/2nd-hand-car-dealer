from sqlalchemy import Integer, Column, Text, ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base

from .base import Base


class ItemDetail(Base):
    __tablename__ = "item_detail"
    items_id = Column(Integer, primary_key=True)
    item_name = Column(Text)
    material = Column(Text)
    label = Column(Text)

    item_detail = relationship("Market", back_populates="market")

    def __repr__(self):
        return f"ItemsDetail(item_id={self.items_id}, item_name={self.item_name}, types={self.material}, label={self.label})"
