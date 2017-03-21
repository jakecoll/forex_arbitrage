import urllib2
import json

path = ['SGD', 'HKD', 'SGD']
#[u'ZAR', u'USD', u'AUD', u'NZD', u'BRL', u'PLN', u'ZAR']

money = 100

for i in range(len(path)-1):

	response = urllib2.Request("http://api.fixer.io/latest?base=" + path[i] + "&symbols=" + path[i+1])
	opener = urllib2.build_opener()
	f = opener.open(response)
	data = json.loads(f.read())

	money = money * data['rates'][path[i+1]]

print money


# path on 3-19 made .00287 cents
# the alogrithm missed collecting the negative cycle because USD did not have a parent