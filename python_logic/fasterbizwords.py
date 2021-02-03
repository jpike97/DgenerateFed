from yahoo_fin import stock_info as si
import requests
import json
import config
import pymongo
from datetime import datetime
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from newsapi import NewsApiClient
import basc_py4chan


def findTickers(bodyText):
    matches = re.findall(
        r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)",
        bodyText)
    return (matches)

##TODO: use set?

whitelist = set('abcdefghijklmnopqrstuvwxyz $ABCDEFGHIJKLMNOPQRSTUVWXYZ')

newNoGoArray = []

def getPrice(ticker):
    print ("Getting price for " + ticker)
    try:
        price = si.get_live_price(ticker)
        print("ticker price complete for "  + ticker)
        return price
    except:
        return newNoGoArray.append(ticker)


def getNews(symbol):
    news_array = []
    api_key = "594ed19f25ef4721bc7cf77cbf0aadc6"
    try:
        response = requests.get("https://newsapi.org/v2/everything?q=" +
                                symbol + "&apiKey=" + api_key)
    except:
        return 0


password = config.password
username = config.username
client = pymongo.MongoClient("mongodb://" + username + ":" + password +
                             "@cluster0-shard-00-00.7s8dh.mongodb.net:27017,cluster0-shard-00-01.7s8dh.mongodb.net:27017,cluster0-shard-00-02.7s8dh.mongodb.net:27017/dGenerate?ssl=true&replicaSet=atlas-wjz2hv-shard-0&authSource=admin&retryWrites=true&w=majority")

names = client.list_database_names()
db = client.dGenerate
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

count = 0
stock_ticker_tracking_array = {}
nogoSet = { 
    "If I", "DD", "LEAPs", "ATH", "I", "Gj", "So I", "OTM", "ITM", "My", "A",
    "So", "TF", "WHY", "LOL", "No", "Leap", "Leaps", "Go", "Up", "It", "WSB",
    "WSB DD", "YOLOS", "YOLO", "FD", "If", "LMAO", "RIP", "IV", "EOW", "Or",
    "Is", "ER", "REWARDS", "Ok", "FOMO", "DOJ", "NYC", "FDs", "Of", "OTM FDs",
    "We", "Yo", "Im", "At", "Do", "Su", "My", "To", "ETF", "IPAD", "LOOK", "AT",
    "RH", "EOD", "AM", "PM", "A", "HERE", "Xi", "IN", "ASAP", "HK", "LOT",
    "ZERO", "ROPE", "Oh", "CNBC", "JR", "INSANE", "TRADE", "LAST", "P", "PTSD",
    "LEAP", "FWIW", "DR", "TED", "TL", "FOMC", "FOMO", "POTUS", "FROM", "BOYS",
    "FUCK", "YC", "BOYS", "WILL", "SEC", "TARIFF", "FROM", "BREXIT", "AIDS",
    "POTUS", "WEEKS", "AH", "IB", "UXXXXX", "Ah", "US", "FED", "GC", "U", "iN",
    "FOMC", "TINA", "TL", "DR", "TED", "OP", "QE", "LEAP", "FWIW", "TLDR",
    "DUMB", "CALL", "SPYs", "BS", "YOLOs", "In", "Jr", "STILL", "EST", "CRAZY",
    "VIX", "FAFSA", "BTFD", "EOY", "YUGE", "EDT", "CHINA", "UNK", "JAPAN",
    "YoY", "UK", "NY", "QoQ", "NAHB", "XI", "Im", "FUD", "USD", "TRIPLE",  "Gf"
}


class Ticker:
    def __init__(self):
        self.mentions = 0
        self.name = "o"
        self.price = 0


def updateTickerInfo(stock_ticker_to_update):
    # see if it exists in the dictionary
    print("check ticker for" + stock_ticker_to_update)
    if stock_ticker_to_update in stock_ticker_tracking_array.keys():
        print ("updating mentions for: " + stock_ticker_to_update)
        print ("currently has " + str(stock_ticker_tracking_array[stock_ticker_to_update].mentions))
        stock_ticker_tracking_array[stock_ticker_to_update].mentions += 1
        
# otherwise create
    else:
        print ("creating new ticker for" + stock_ticker_to_update)
        newTicker = Ticker()
        newTicker.name = stock_ticker_to_update
        newTicker.mentions = 1
        newTicker.price = getPrice(stock_ticker_to_update)
        stock_ticker_tracking_array[newTicker.name] = newTicker
        print ("finished ticker for" + stock_ticker_to_update)



# get ids of all threads

bizBoard = basc_py4chan.Board('b')
bizThreadIDs = bizBoard.get_all_thread_ids()

for threadID in bizThreadIDs:
    if bizBoard.thread_exists(threadID):
        thread = bizBoard.get_thread(threadID)
        try:
            posts = thread.all_posts
        except:
            continue
        for post in posts:
            text_comment = post.text_comment
            tickerArray = (findTickers(text_comment))
            print (tickerArray)
            for stock_ticker in tickerArray:
                print ("iterating")
                if len(stock_ticker) < 5:
                    if stock_ticker in nogoSet:
                        print(stock_ticker + " was in NOGOS!")
                        print(stock_ticker)
                        print("so we skipping")
                        continue
                    else:
                        updateTickerInfo(stock_ticker)
                    
                else:
                    continue


# news


# /v2/top-headlines


# /v2/everything

# /v2/sources


news = []

for x in stock_ticker_tracking_array:
    db.bizWordsCards.remove({"id": stock_ticker_tracking_array[x].name})

for x in stock_ticker_tracking_array:
    # get news!
    top_headlines = getNews(stock_ticker_tracking_array[x].name)
    if stock_ticker_tracking_array[x].price is not None:
        print(stock_ticker_tracking_array[x].name)
        db.bizWordsCards.insert_one({"id": stock_ticker_tracking_array[x].name, "ticker": stock_ticker_tracking_array[x].name, "currentPrice": stock_ticker_tracking_array[x].price, "comments": [
        ], "numMentions": stock_ticker_tracking_array[x].mentions, "dateTimeStamp": datetime.now(), "news": top_headlines})
        print('-----')

print (newNoGoArray)