import FundamentalAnalysis
import lxml
from lxml import html
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def getYahooTrending():
	page = requests.get('https://finance.yahoo.com/trending-tickers')
	tree = html.fromstring(page.content)
	table = tree.xpath('//table')
	symbol = pd.read_html(lxml.etree.tostring(
	    table[0], method='html'))[0]['Symbol'].to_list()
	print(symbol)
