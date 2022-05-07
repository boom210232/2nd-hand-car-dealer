from models.item_detail import ItemDetail
from models.market import Market
# from matplotlib.pyplot import title
from blackdesert.blackdesert_online import BdoStarter
from fastapi import FastAPI

bdo_starter = BdoStarter()

print(bdo_starter.market_list().get_all_market_transaction())
print(bdo_starter.item_list().get_items_by_label("orange"))
trash_item = ItemDetail(items_id=500, item_name="Unknown", material="weapon", label="white")
# print(bdo_starter.item_list().add_item(trash_item))
print(bdo_starter.item_list().get_item_by_items_id(500))

print(bdo_starter.market_list().get_market_by_username("livernoob"))
print(bdo_starter.market_list().get_market_by_username_id(2))

print("-------------------------------------------------------------")
new_arrival=Market(username_id=51,username="JebBush",items_id=11)
# print(bdo_starter.market_list().add_market(new_arrival))
print(bdo_starter.market_list().get_market_by_username("JebBush"))

app = FastAPI()


# @app.get("/item-list/{id}")
# async def root(id):
#     return {"info": bdo_starter.market_list().get_market_by_username_id(id)}
