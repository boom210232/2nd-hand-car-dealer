from models.item_detail import ItemDetail
from sqlalchemy.orm.session import Session


class ItemDetailDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_market_transaction(self):
        return self.__session.query(ItemDetail).all()
