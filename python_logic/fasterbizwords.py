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
from iexfinance.stocks import Stock


def findTickers(bodyText):
    matches = re.findall(
        r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)",
        bodyText)
    return (matches)

# TODO: use set?


whitelist = set('abcdefghijklmnopqrstuvwxyz $ABCDEFGHIJKLMNOPQRSTUVWXYZ')

newNoGoArray = []


def getPrice(ticker):
    try:
        price = Stock(ticker).get_price()
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
        json_news_data = response.json()
        print (json_news_data)
        for x in json_news_data['articles']:
            news_array.append([x['title'], x['url']])
        return news_array
    print("got news I guess")


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
    "YoY", "UK", "NY", "QoQ", "NAHB", "XI", "Im", "FUD", "USD", "TRIPLE",  "Gf", 'Am I', 'No I', 'MUCH', 'Id', 'Uh', 'NO', 'Mr', 'LSD', 'Me', 'BBC', 'V', 'X', 'AI', 'AOC', 'ST', 'YO', 'Ex', 'SiL', 'OC', 'He', 'BY', 'Y', 'THAT', 'YES', 'MORE', 'GF', 'WAIT', 'G', 'O', 'T', 'MIN', 'H', 'SJWs', 'On', 'Al', 'AR', 'YOU', 'S', 'VII', 'VIII', 'VI', 'II', 'Au', 'Ag', 'BUMP', 'Ew', 'FAST', 'XD', 'Ro', 'Em', 'N', 'ROLL', 'Eh', 'RAUL', 'Re', 'YLYL', 'AC', 'DC', 'BBQ', 'Op', 'KOd', 'Us', 'PC', 'As', 'CEO', 'SAME', 'Bc', 'By', 'TACs', 'R', 'HG', 'JFC', 'IP', 'JC', 'IT', 'ONE', 'BJ', 'CL', 'Oh I', 'HUNG', 'Bf', 'Bi', 'M', 'F', 'Z', 'K', 'CDC', 'NOT', 'Be', 'TV', 'NPD', 'CIS', 'OK', 'Bj', 'OMG', 'JJ', 'WWYD', 'STFU', 'C', 'WOO', 'LoL', 'GTA', 'E', 'RAGE', 'XSX', 'MC', 'SA', 'SON', 'An', 'Eg', 'LGBT', 'GDP', 'GW', 'Da', 'GAY', 'Dr', 'DLC', 'GE', 'MOBA', 'ToS', 'IRQ', 'Mb', 'WHFB', 'AoS', 'MOAR', 'NEED', 'GoT', 'B', 'Vp', 'AND', 'EU', 'Um', 'STOP', 'BRO', 'CDs', 'BE', 'HRT', 'HON', 'GME', 'OK I', 'OTC', 'NC', 'D', 'GOOD', 'Hi', 'BBW', 'HOT', 'AA', 'EVER', 'ARE', 'LA', 'KYS', 'IQ', 'SAT', 'GTFO', 'HEY', 'FBI', 'ACT', 'CAN', 'BMI', 'FTM', 'SHTF', 'MRE', 'PB', 'SO', 'USA', 'TABS', 'CP', 'BLM', 'EXT', 'RO', 'EDC', 'KEK', 'Ar', 'ACs', 'DVR', 'PSE', 'HA', 'BOB', 'BOY', 'Hm', 'De', 'AD', 'USSR', 'NK', 'ANY', 'OSHA', 'MSHA', 'NAZI', 'CEJL', 'TO', 'GO', 'THIS', 'AvE', 'A No', 'THEM', 'BWC', 'Hu', 'OwO', 'UDK', 'ASS', 'ASMR', 'VR', 'ERP', 'DRAT', 'JSON', 'PR', 'WSHH', 'IDK', 'BC', 'OS', 'AHH', 'Ya', 'OPs', 'St', 'A B', 'L', 'BLT', 'BLTs', 'LARP', 'EZ', 'POC', 'CNN', 'ALL', 'OR', 'W', 'WITH', 'POV', 'EP', 'Mm', 'HC', 'YT', 'FYI', 'SNL', 'SJW', 'Nu', 'RPM', 'HOA', 'VP', 'SUCK', 'Ez', 'NS', 'Rr', 'Ah I', 'IF', 'NPE', 'DNA', 'SUCH', 'Lo', 'Ey', 'Nj', 'IPCC', 'TP', 'Ku', 'NVLD', 'Q', 'TX', 'HODL', 'ETH', 'BTC'
}


class Ticker:
    def __init__(self):
        self.mentions = 0
        self.name = "o"
        self.price = 0


def updateTickerInfo(stock_ticker_to_update):
    # see if it exists in the dictionary
    if stock_ticker_to_update in stock_ticker_tracking_array:
        stock_ticker_tracking_array[stock_ticker_to_update].mentions += 1

# otherwise create
    else:
        newTicker = Ticker()
        newTicker.name = stock_ticker_to_update
        newTicker.mentions = 1
        # newTicker.price = getPrice(stock_ticker_to_update)
        stock_ticker_tracking_array[newTicker.name] = newTicker

# get ids of all threads
bizBoard = basc_py4chan.Board('biz')
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
            for stock_ticker in tickerArray:
                if len(stock_ticker) < 5:
                    if stock_ticker in nogoSet:
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
    if (stock_ticker_tracking_array[x].mentions > 5):
        top_headlines = getNews(stock_ticker_tracking_array[x].name)
        print(stock_ticker_tracking_array[x].name)
        print (top_headlines)
        db.bizWordsCards.insert_one({"id": stock_ticker_tracking_array[x].name, "ticker": stock_ticker_tracking_array[x].name, "currentPrice": stock_ticker_tracking_array[x].price, "comments": [
        ], "numMentions": stock_ticker_tracking_array[x].mentions, "dateTimeStamp": datetime.now(), "news": top_headlines})
        print('-----')
