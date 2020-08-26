import praw
import numpy
import re
from psaw import PushshiftAPI
import sys
import pandas as pd
import datetime as dt
from datetime import datetime, timedelta
from collections import Counter
import csv
import praw
import numpy
import pyodbc
import re
import sys
import yahoo_finance
from yahoo_finance import Share
from collections import Counter
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib import style
from utilities.findTickers import findTickers
from utilities.getPrice import getPrice
from utilities.getNews import getNews
import config
import requests
import json
from utilities.sanitize import sanitize
from utilities.findTickers import findTickers
from utilities.getPrice import getPrice
from bs4 import BeautifulSoup

total_count = 0
biz_threads_url = "https://a.4cdn.org/biz/threads.json"
biz_single_base_url = "https://a.4cdn.org/biz/thread/"

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
    "YoY", "UK", "NY", "QoQ", "NAHB", "XI", "Im"
]


class Ticker:

	def __init__(self):
		self.mentions = 0
		self.name = "o"
		self.time = 0
		self.comments = []
		self.news = []


def updateTickerInfo(stock_ticker_to_update, comment_text):
	try:
		stock_ticker_tracking_array1[stock_ticker_to_update].mentions += 1
		stock_ticker_tracking_array1[stock_ticker_to_update].comments.append(
		    comment_text)
	except:
		newTicker = Ticker()
		newTicker.name = stock_ticker_to_update
		newTicker.mentions = 1
		newTicker.time = track_time_combined
		##news limits at 250 requests lol
		# try:
		# 	some_news = (getNews(stock_ticker_to_update))
		# 	print("news worked")
		# 	newTicker.news.append(some_news)

		# except:
		# 	print("couldn't find any news")
		stock_ticker_tracking_array1[newTicker.name] = newTicker


##################bizwords code TODO: seperate into function
def scrapeComments(the_thread):
	count_comments = 0
	# print(the_thread)
	for x in the_thread['posts']:
		try:
			comment_with_tags = (x['com'])
			cleaned_comment = sanitize(comment_with_tags)
			# print(cleaned_comment)
			count_comments += 1
			# print(count_comments)
			tickerArray = (findTickers(cleaned_comment))
			for stock_ticker in tickerArray:
				if len(stock_ticker) < 5 and stock_ticker not in nogos:
					updateTickerInfo(stock_ticker, cleaned_comment)

				# try:
				# 	print(stock_ticker)
				# 	print(getPrice(stock_ticker))
				# except:
				# 	'not a valid ticker lol'
			# print('------')
		except:
			print('no com')

redditPassword = config.settings['redditPassword']
redditClientSecret = config.settings['redditClientSecret']

reddit = praw.Reddit(
    client_id='GCjpdb-78ljIQg',
    client_secret=redditClientSecret,
    password=redditPassword,
    user_agent='testguyman',
    username='opsanun')
api = PushshiftAPI(reddit)

time_start = dt.datetime(2020, 2, 21)
track_time_minutes = dt.datetime.now().time()
track_time_combined = datetime.combine(time_start, track_time_minutes)
print(track_time_combined)
time_end = time_start + timedelta(days=1)
stock_ticker_tracking_array1 = {}
start_epoch = time_start

end_epoch = time_end

List1 = list(
    api.search_submissions(
        q='Daily Discussion Thread',
        after=start_epoch,
        before=end_epoch,
        subreddit='wallstreetbets',
        limit=10))
callarray = List1
print('looking for submissions')
for submission in List1:
	print(submission.title)
	for j in callarray:
		j.comments.replace_more(limit=0)
		matches = findTickers(j.selftext)
		for x in matches:
			a = Ticker()
			if len(x) < 5 and x not in nogos:
				updateTickerInfo(x, j.selftext)
		for comment in j.comments:
			matches = findTickers(comment.body)
			for x in matches:
				a = Ticker()
				if len(x) < 5 and x not in nogos:
					updateTickerInfo(x, comment.body)

##################bizwords code TODO: seperate into function

# for x in json_data:
# 	for y in x['threads']:
# 		thread_id = y['no']
# 		print(thread_id)
# 		try:
# 			response = requests.get(biz_single_base_url + str(thread_id) +
# 			                        '.json')
# 		except:
# 			print("didn't work")
# 		json_data_comments = response.json()
# 		for x in json_data_comments['posts']:
# 			try:
# 				# print(x['sub'])
# 				if '/smg/' in x['sub']:
# 					scrapeComments(json_data_comments)
# 					break
# 			except:
# 				break

##SQL STUFF
#commenting out for now , might use firebase
# server = 'localhost'
# database = 'stock_proj'
# username = config.settings['username']
# password = config.settings['password']
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
#                       server + ';DATABASE=' + database + ';UID=' + username +
#                       ';PWD=' + password)
# cursor = cnxn.cursor()
# sql = "INSERT INTO dbo.stocks (symbol, price, time_checked, num_mentions, source) VALUES (?, ?, ?, ?, ?)"

# with open('output1.txt', 'a') as the_file:
# 	for x in stock_ticker_tracking_array1:
# 		if x not in nogos:
# 			try:
# 				val = (stock_ticker_tracking_array1[x].name,
# 				       stock_ticker_tracking_array1[x].price,
# 				       stock_ticker_tracking_array1[x].time,
# 				       stock_ticker_tracking_array1[x].mentions, 'reddit')
# 				cursor.execute(sql, val)
# 				cnxn.commit()
# 			except:
# 				print(x)
# 				print("that broke it lol")
# 			the_file.write(stock_ticker_tracking_array1[x].name)
# 			the_file.write('\n')
# 			the_file.write(str(stock_ticker_tracking_array1[x].mentions))
# 			the_file.write('\n')
# 			the_file.write(str(stock_ticker_tracking_array1[x].price))
# 			the_file.write('\n')
# 			the_file.write(str(stock_ticker_tracking_array1[x].time))
# 			for words in stock_ticker_tracking_array1[x].comments:
# 				the_file.write('between words')
# 				the_file.write('\n')
# 				try:
# 					the_file.write(words)
# 				except:
# 					print("words that broke")
# 					print(words)
# 				the_file.write('\n')
# 			the_file.write('-----')
# 			the_file.write('\n')
# 			total_count = total_count + stock_ticker_tracking_array1[x].mentions
for x in stock_ticker_tracking_array1:
	#todo add firebase stuff
	print (x)


