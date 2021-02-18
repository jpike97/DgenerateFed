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


def getNews(symbol):
    print("getting news")
    news_array = []
    api_key = "594ed19f25ef4721bc7cf77cbf0aadc6"
    try:
        response = requests.get("https://newsapi.org/v2/everything?q=" +
                                symbol + "&apiKey=" + api_key)
        print (response)
                    
    except:
        return ["no news...", "google.com"]
    json_news_data = response.json()
    print (json_news_data)
    for x in json_news_data['articles']:
        news_array.append([x['title'], x['url']])
        print(x['title'])
    return news_array
    print("got news I guess")


password = config.password
username = config.username
client = pymongo.MongoClient("mongodb://" + username + ":" + password + "@cluster0-shard-00-00.7s8dh.mongodb.net:27017,cluster0-shard-00-01.7s8dh.mongodb.net:27017,cluster0-shard-00-02.7s8dh.mongodb.net:27017/dGenerate?ssl=true&replicaSet=atlas-wjz2hv-shard-0&authSource=admin&retryWrites=true&w=majority")

names = client.list_database_names()
db = client.dGenerate
now = datetime.now()

assetsToGetNewsFor = db.bizWordsCards.find({"numMentions": {"$gt": 10}}).sort("numMentions", pymongo.DESCENDING).limit(12)



for x in assetsToGetNewsFor:
    top_headlines = getNews(x['ticker'])
    db.news.insert_one({"id": x['ticker'], "ticker": x['ticker'], "currentPrice": 0, "news": top_headlines, "dateTimeStamp": datetime.now()})
    