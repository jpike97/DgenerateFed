from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from datetime import timedelta
import json
import pymongo
import config

password = config.password
username = config.username
client = pymongo.MongoClient("mongodb://" + username + ":" + password + "@cluster0-shard-00-00.7s8dh.mongodb.net:27017,cluster0-shard-00-01.7s8dh.mongodb.net:27017,cluster0-shard-00-02.7s8dh.mongodb.net:27017/dGenerate?ssl=true&replicaSet=atlas-wjz2hv-shard-0&authSource=admin&retryWrites=true&w=majority")

names = client.list_database_names()
db = client.dGenerate
now = datetime.now() - timedelta(days=1)
now = datetime(*now.timetuple()[:3])
print(now)
db.bizWordsCards.remove( { "dateTimeStamp" : {"$lt" : now } })
db.bizPicSnaps.remove( { "dateTimeStamp" : {"$lt" : now } })
