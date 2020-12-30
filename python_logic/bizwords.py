import requests
import json
from bs4 import BeautifulSoup
import config
import pymongo
from datetime import datetime
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
from webcolors import hex_to_name
from newsapi import NewsApiClient



def findTickers(bodyText):
	matches = re.findall(
	    r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)",
	    bodyText)
	return (matches)


def getNews(symbol):
	news_array = []
	api_key = "594ed19f25ef4721bc7cf77cbf0aadc6"
	try:
		response = requests.get("https://newsapi.org/v2/everything?q=" +
		                        symbol + "&apiKey=" + api_key)
	except:
		return 0

	json_news_data = response.json()
	for x in json_news_data['articles']:
		news_array.append([x['title'], x['url']])
	return news_array

newsApi = config.newsApi
whitelist = set('abcdefghijklmnopqrstuvwxyz $ABCDEFGHIJKLMNOPQRSTUVWXYZ')
newsapi = NewsApiClient(api_key=newsApi)


from yahoo_fin import stock_info as si


def getPrice(ticker):
	try:
		price = si.get_live_price(ticker)
		return price
	except:
		print('no')

def sanitize(comment_input):
	cleaned_comment = BeautifulSoup(comment_input).get_text()
	return ''.join(filter(whitelist.__contains__, cleaned_comment))



biz_threads_url = "https://a.4cdn.org/biz/threads.json"

biz_single_base_url = "https://a.4cdn.org/biz/thread/"

password = config.password
username = config.username
client = pymongo.MongoClient("mongodb://" + username + ":" + password + "@cluster0-shard-00-00.7s8dh.mongodb.net:27017,cluster0-shard-00-01.7s8dh.mongodb.net:27017,cluster0-shard-00-02.7s8dh.mongodb.net:27017/dGenerate?ssl=true&replicaSet=atlas-wjz2hv-shard-0&authSource=admin&retryWrites=true&w=majority")

names = client.list_database_names()
db = client.dGenerate
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

response = requests.get(biz_threads_url)
json_data = response.json()
count = 0
hold_id = 17020414
stock_ticker_tracking_array = {}
nogos = [
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
    "YoY", "UK", "NY", "QoQ", "NAHB", "XI", "Im", "FUD"
]


class Ticker:

	def __init__(self):
		self.mentions = 0
		self.name = "o"
		self.price = 0
		self.newsArticles = []


def updateTickerInfo(stock_ticker_to_update):
	try:
		stock_ticker_tracking_array[stock_ticker_to_update].mentions += 1
	except:
		newTicker = Ticker()
		newTicker.name = stock_ticker_to_update
		newTicker.mentions = 1
		newTicker.price = getPrice(stock_ticker_to_update)
		stock_ticker_tracking_array[newTicker.name] = newTicker


def scrapeComments(the_thread):
	count_comments = 0
	# print(the_thread)
	for x in the_thread['posts']:
		try:
			comment_with_tags = (x['com'])
			cleaned_comment = sanitize(comment_with_tags)
			count_comments += 1
			# print(count_comments)
			tickerArray = (findTickers(cleaned_comment))
			for stock_ticker in tickerArray:
				if len(stock_ticker) < 5 and stock_ticker not in nogos:
					updateTickerInfo(stock_ticker)

				# try:
				# 	print(stock_ticker)
				# 	print(getPrice(stock_ticker))
				# except:
				# 	'not a valid ticker lol'
			# print('------')
		except:
			print('no com')


#get ids of all threads
for x in json_data:
	for y in x['threads']:
		thread_id = y['no']
		response = requests.get(biz_single_base_url + str(thread_id) + '.json')
		try:
			json_data_comments = response.json()
		except:
			print("no")
		for x in json_data_comments['posts']:
			try:
				print(x['sub'])
				if 'smg' in x['sub']:
					scrapeComments(json_data_comments)
					break
			except:
				break



###news


# /v2/top-headlines


# /v2/everything

# /v2/sources


news = []

for x in stock_ticker_tracking_array:
	db.bizWordsCards.remove( { "id" : stock_ticker_tracking_array[x].name})

for x in stock_ticker_tracking_array:
	##get news!
	top_headlines = getNews(stock_ticker_tracking_array[x].name)
	if stock_ticker_tracking_array[x].price is not None:
			db.bizWordsCards.insert_one({"id": stock_ticker_tracking_array[x].name, "ticker": stock_ticker_tracking_array[x].name, "currentPrice": stock_ticker_tracking_array[x].price, "comments": [], "numMentions": stock_ticker_tracking_array[x].mentions, "dateTimeStamp": datetime.now(), "news": top_headlines})
			print('-----')