from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Market(Base):
    __tablename__ = "market"
    user_id = Column(Integer, primary_key=True)
    username = Column(Text)
    buy_item = Column(Integer)

    market = relationship("ItemDetail", back_populates="item_detail")

    def __repr__(self):
        return f"ItemsDetail(user_id={self.user_id}, username={self.username}, buy_id={self.buy_item})"
