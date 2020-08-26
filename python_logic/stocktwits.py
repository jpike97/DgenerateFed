import json
import requests
from utilities.getNews import getNews

response = requests.get(
    "https://api.stocktwits.com/api/2/trending/symbols.json")

json_data = response.json()

for x in json_data['symbols']:
	print(x)
	print('-------------------')
	print(getNews(x['symbol']))
