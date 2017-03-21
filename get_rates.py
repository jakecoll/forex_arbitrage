import urllib2
import json
import pprint
import requests

# http://fixer.io/
class GetRates:

	def __init__(self):
		self.url = "http://api.fixer.io/latest"

	def get_forex_rates(self):
		response = urllib2.Request(self.url)
		opener = urllib2.build_opener()
		f = opener.open(response)
		data = json.loads(f.read())

		### get currencies
		currencies = data['rates'].keys()
		currencies.append('EUR')
		
		by_country = self.get_forex_for_each_country(currencies)

		return by_country

	def get_forex_for_each_country(self, denom_codes):

		graph = {}

		for country in denom_codes:
			req = urllib2.Request(self.url + "?base=" + country)
			opener = urllib2.build_opener()
			f = opener.open(req)
			data = json.loads(f.read())
			graph[country] = data['rates']
		
		return graph



if __name__ == "__main__":

	rates = GetRates()
	print rates.get_forex_rates()