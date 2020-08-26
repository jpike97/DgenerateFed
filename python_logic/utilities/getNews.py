import json
import requests


def getNews(symbol):
	news_array = []
	api_key = "594ed19f25ef4721bc7cf77cbf0aadc6"
	try:
		response = requests.get("https://newsapi.org/v2/everything?q=" +
		                        symbol + "&apiKey=" + api_key)
	except:
		return 0

	json_news_data = response.json()
	print(json_news_data['articles'])
	for x in json_news_data['articles']:
		news_array.append([x['title'], x['url']])
	return news_array
