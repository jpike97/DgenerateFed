import requests
import json
from utilities.sanitize import sanitize
from utilities.findTickers import findTickers
from utilities.getPrice import getPrice
from bs4 import BeautifulSoup
import config
import pymongo
import config
from datetime import datetime

password = config.password
username = config.username
client = pymongo.MongoClient("mongodb://" + username + ":" + password + "@cluster0-shard-00-00.7s8dh.mongodb.net:27017,cluster0-shard-00-01.7s8dh.mongodb.net:27017,cluster0-shard-00-02.7s8dh.mongodb.net:27017/dGenerate?ssl=true&replicaSet=atlas-wjz2hv-shard-0&authSource=admin&retryWrites=true&w=majority")

names = client.list_database_names()
db = client.dGenerate
now = datetime.now()

db.bizWordsCards.insert_one({"id": "test1", "ticker": "testTicker1", "currentPrice": 26, "comments": [], "numMentions": 47, "dateTimeStamp": datetime.now()})