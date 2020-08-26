from bs4 import BeautifulSoup

whitelist = set('abcdefghijklmnopqrstuvwxyz $ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def sanitize(comment_input):
	cleaned_comment = BeautifulSoup(comment_input).get_text()
	return ''.join(filter(whitelist.__contains__, cleaned_comment))
