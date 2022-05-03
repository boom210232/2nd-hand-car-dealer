from models.item_detail import ItemDetail
from models.market import Market
from matplotlib.pyplot import title
from blackdesert.blackdesert_online import BdoStarter

bdo_starter = BdoStarter()

print(bdo_starter.market_list().get_all_market_transaction())
