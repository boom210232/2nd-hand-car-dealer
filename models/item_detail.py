from sqlalchemy import Integer, Column, Text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class ItemDetail(Base):
    __tablename__ = "item_detail"
    item_id = Column(Integer, primary_key=True)
    item_name = Column(Text)
    types = Column(Text)
    label = Column(Text)

    market = relationship("Market", back_populates="market")

    def __repr__(self):
        return f"ItemsDetail(item_id={self.item_id}, item_name={self.item_name}, types={self.types}, label={self.label})"
