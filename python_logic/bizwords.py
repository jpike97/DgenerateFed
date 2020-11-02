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


def findTickers(bodyText):
	matches = re.findall(
	    r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)",
	    bodyText)
	return (matches)

whitelist = set('abcdefghijklmnopqrstuvwxyz $ABCDEFGHIJKLMNOPQRSTUVWXYZ')

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
		print(thread_id)
		response = requests.get(biz_single_base_url + str(thread_id) + '.json')
		json_data_comments = response.json()
		for x in json_data_comments['posts']:
			try:
				print(x['sub'])
				if 'smg' in x['sub']:
					print("found smg")
					scrapeComments(json_data_comments)
					break
			except:
				break
for x in stock_ticker_tracking_array:
	print(stock_ticker_tracking_array[x].name)
	print(stock_ticker_tracking_array[x].mentions)
	print(stock_ticker_tracking_array[x].price)
	db.bizWordsCards.remove( { "id" : stock_ticker_tracking_array[x].name})
	if stock_ticker_tracking_array[x].price is not None:
			db.bizWordsCards.insert_one({"id": stock_ticker_tracking_array[x].name, "ticker": stock_ticker_tracking_array[x].name, "currentPrice": stock_ticker_tracking_array[x].price, "comments": [], "numMentions": stock_ticker_tracking_array[x].mentions, "dateTimeStamp": datetime.now()})
			print('-----')


colorlist = []
a = 1


def imagecalc():
	NUM_CLUSTERS = 5
	im = Image.open('img/image.jpg')
	im = im.resize((150, 150))  # optional, to reduce time
	ar = np.asarray(im)
	shape = ar.shape
	ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

	codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

	vecs, dist = scipy.cluster.vq.vq(ar, codes)  # assign codes
	counts, bins = scipy.histogram(vecs, len(codes))  # count occurrences

	index_max = scipy.argmax(counts)  # find most frequent
	peak = codes[index_max]
	colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
	colourHSV = convertToHSV(colour)
	colorlist.append(colourHSV)

def convertToHSV(rgbColor):
		h = rgbColor
		rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
		r = rgb[0]
		g = rgb[1]
		b = rgb[2]

		r, g, b = r / 255.0, g / 255.0, b / 255.0
  
	# h, s, v = hue, saturation, value 
		cmax = max(r, g, b)    # maximum of r, g, b 
		cmin = min(r, g, b)    # minimum of r, g, b 
		diff = cmax-cmin       # diff of cmax and cmin. 
  
	# if cmax and cmax are equal then h = 0 
		if cmax == cmin:  
			h = 0
	  
	# if cmax equal r then compute h 
		elif cmax == r:  
			h = (60 * ((g - b) / diff) + 360) % 360
  
	# if cmax equal g then compute h 
		elif cmax == g: 
			h = (60 * ((b - r) / diff) + 120) % 360
  
	# if cmax equal b then compute h 
		elif cmax == b: 
			h = (60 * ((r - g) / diff) + 240) % 360
  
		# if cmax equal zero 
		if cmax == 0: 
			s = 0
		else: 
			s = (diff / cmax) * 100
  
	# compute v 
		v = cmax * 100
		
		hsvTuple = (h,s,v)
		return hsvTuple



count = 0
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://4chan.org/biz/catalog")
images = driver.find_elements_by_tag_name('img')

for image in images:
	urllib.request.urlretrieve(image.get_attribute('src'), 'img/image.jpg')
	try:
		imagecalc()
	except:
		print("oof")
	count += 1

driver.close()

redTotal = 0
greenTotal = 0
imageTotal = 0
hueTotal = 0
satTotal = 0
vTotal = 0

for rgbValue in colorlist:
	hue = rgbValue[0]
	sat = rgbValue[1]
	v = rgbValue[2]

	##grey / blackness check
	if sat and v > 30:
		##check for red / green
		if hue > 0 and hue < 60:
			redTotal += 1
			
		elif hue > 100 and hue < 180:
			greenTotal += 1

	hueTotal += hue
	satTotal += sat
	vTotal += v
	imageTotal += 1
	
hueAvg = hueTotal / imageTotal
satAvg = satTotal / imageTotal
vAvg = vTotal / imageTotal
HSVAvg = (hueAvg, satAvg, vAvg)
##TODO: show reddest & greenest image lol?


db.bizPicSnaps.insert_one({"greentotal": greenTotal, "redTotal": redTotal, "imageTotal": imageTotal, "HSVavg": HSVAvg, "dateTimeStamp": now})

#results = '{"greenTotal": greenTotal,"redTotal": redTotal,
 #   "imageTotal": imageTotal,
  #  "hueAvg": hueAvg,
   # "satAvg": satAvg,
	#"vAvg": vAvg,
	#"dateTime": now,
	#"HSVAvg": 
#}'