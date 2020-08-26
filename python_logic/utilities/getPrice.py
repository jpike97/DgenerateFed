from yahoo_fin import stock_info as si


def getPrice(ticker):
	try:
		price = si.get_live_price(ticker)
		return price
	except:
		print('no')
