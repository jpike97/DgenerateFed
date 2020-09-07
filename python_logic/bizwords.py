import requests
import json
from utilities.sanitize import sanitize
from utilities.findTickers import findTickers
from utilities.getPrice import getPrice
from bs4 import BeautifulSoup

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
		self.price = 0


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
				print (stock_ticker)
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
		json_data_comments = response.json()
		for x in json_data_comments['posts']:
			try:
				# print(x['sub'])
				if '/smg/' in x['sub']:
					print("found smg")
					scrapeComments(json_data_comments)
					break
			except:
				break
for x in stock_ticker_tracking_array:
	print(stock_ticker_tracking_array[x].name)
	print(stock_ticker_tracking_array[x].mentions)
	print(stock_ticker_tracking_array[x].price)
	print('-----')
