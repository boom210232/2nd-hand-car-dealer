from models.item_detail import ItemDetail
from sqlalchemy.orm.session import Session


class ItemDetailDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_items(self):
        return self.__session.query(ItemDetail).all()

    def get_item_by_items_id(self, items_id):
        return self.__session.query(ItemDetail).filter_by(items_id=items_id).first()

    def get_item_by_item_name(self, item_name):
        return self.__session.query(ItemDetail).filter_by(item_name=item_name).first()

    def get_items_by_material(self, material):
        return self.__session.query(ItemDetail).filter_by(material=material).all()

    def get_items_by_label(self, label):
        return self.__session.query(ItemDetail).filter_by(label=label).all()

    def add_item(self, item: ItemDetail):
        self.__session.add(item)
        self.__session.commit()
        print("Market added successfully.")

    def delete_item_by_id(self, items_id: int):
        item = self.__session.query(ItemDetail).filter_by(items_id=items_id).first()
        self.__session.delete(item)
        self.__session.commit()
        print("Market deleted successfully.")
