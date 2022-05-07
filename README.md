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

### Getting started
Please install requirement package by using below command.       
` pip install -r requirement.txt` 
### How to use sqlite3 
**In the case of no .db file in your local machine only. If it have, please skip it.**       
At first you need to install the requirement by using the command below.          
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

### Try to use Swagger with FastAPI    
After install package in requirement.txt      
You can use FastAPI by using `uvicorn main:app --reload` to run the FastAPI.         
Then go to `http://127.0.0.1:8000/docs` to use API with swagger.io UI.
   

## Documents for this repository.
[Domain Model](https://github.com/boom210232/blackdesert-DAO/wiki/Domain-Model)           
[Package diagram](https://github.com/boom210232/blackdesert-DAO/wiki/Package-diagram)       
[UML diagram](https://github.com/boom210232/blackdesert-DAO/wiki/UML-diagram)          
[Web service API](https://github.com/boom210232/blackdesert-DAO/wiki/Web-Services-API)     
Package and UML diagram - Draft version.        
  

## Wiki
[Link to Wiki](https://github.com/boom210232/blackdesert-DAO/wiki)



