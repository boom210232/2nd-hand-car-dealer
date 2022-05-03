from models.market import Market
from sqlalchemy.orm.session import Session


class MarketDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_market_transaction(self):
        return self.__session.query(Market).all()


