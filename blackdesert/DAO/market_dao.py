from models.market import Market
from sqlalchemy.orm.session import Session


class MarketDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_market_transaction(self):
        return self.__session.query(Market).all()

    def get_market_by_username_id(self, username_id: int):
        return self.__session.query(Market).filter_by(username_id=username_id).first()

    def get_market_by_username(self, username: str):
        return self.__session.query(Market).filter_by(username=username).first()

    def add_market(self, market: Market):
        self.__session.add(market)
        self.__session.commit()
        print("Market added successfully.")

    def delete_market_by_id(self, username_id: int):
        market = self.__session.query(Market).filter_by(username_id=username_id).first()
        self.__session.delete(market)
        self.__session.commit()
        print("Market deleted successfully.")

    def update_username_by_username_id(self, username_id, new_username: str):
        market = self.__session.query(Market).filter_by(username_id=username_id).first()
        market.username = new_username
        self.__session.commit()
        print("Market username is updated successfully.")

    def update_items_id_by_username_id(self, username_id, new_items_id: str):
        market = self.__session.query(Market).filter_by(username_id=username_id).first()
        market.items_id = new_items_id
        self.__session.commit()
        print("Market items_id is updated successfully.")


