import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://student:PqyqrY2aEC22B5SB@cluster0-ya1yr.mongodb.net/stock-prices?retryWrites=true")
db = client['<database>']
collection = db.prices

# write your queries here


