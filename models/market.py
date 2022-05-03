from sqlalchemy import Integer, Column, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from .base import Base
# Base = declarative_base()


class Market(Base):
    __tablename__ = "market"
    username_id = Column(Integer, primary_key=True)
    username = Column(Text)
    items_id = Column(Integer, ForeignKey("item_detail.items_id"), nullable=False)

    market = relationship("ItemDetail", back_populates="item_detail")

    def __repr__(self):
        return f"ItemsDetail(user_id={self.username_id}, username={self.username}, buy_id={self.items_id})"
