from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from blackdesert.DAO.item_detail_dao import ItemDetailDao
from blackdesert.DAO.market_dao import MarketDao


class BdoStarter:
    def __init__(self, connection_url="sqlite:///bdo_database.db"):
        engine = create_engine(connection_url)
        session = sessionmaker(bind=engine)
        self.__db_session = session()

    def market_list(self):
        return MarketDao(self.__db_session)

    def item_list(self):
        return ItemDetailDao(self.__db_session)
