# blackdesert-DAO

## Table description 
### Table "item detail"
- item_id is an id for item lists.
- item_name is name of the item in black desert online.
- types is a type of item (such as weapon or armor).
- label is a label of frame in item icon to show how it rare.

### Table "market"
- user_id is an id for user.
- username is a username that show in black desert online.
- buy_item to show what player buy reference to the id of the item in "item detail table"


### How to use sqlite3 ###
At first you need to install the requirement by using the command below.     
` pip install -r requirement.txt`      
Then, you need to make the database file by using this command       
`sqlite3 bdo_database.db -init bdo_db.schema`     
The sqlite will redirect to loading the resource from the schema for the first time.
Then copy by step these three line below for import .csv files to the DB.          
        
`.mode csv`     
**For import item_detail.csv to item_detail table.**      
`.import data/item_detail.csv item_detail`       
**For import market.csv to market table.**   
`.import data/market.csv market`     
**Exit the sqlite**      
`.quit` or you can use Ctrl + C for exit

In case that you want to fix after first time. Use this command to open sqlite.         
`sqlite3 bdo_database.db`     

## Documents for this repository.
TBA


