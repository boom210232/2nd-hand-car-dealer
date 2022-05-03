from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from .base import Base
# Base = declarative_base()


class Market(Base):
    __tablename__ = "market"
    username_id = Column(Integer, primary_key=True)
    username = Column(Text)
    buy_list = Column(Integer)

    market = relationship("ItemDetail", back_populates="item_detail")

    def __repr__(self):
        return f"ItemsDetail(user_id={self.username_id}, username={self.username}, buy_id={self.buy_list})"
