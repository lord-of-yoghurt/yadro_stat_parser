import urllib, re, sys

serviceurl = 'http://counter.yadro.ru/values?'

site = sys.argv[1]
url = serviceurl + urllib.urlencode({'site' : site})

print 'Retrieving', url

data = [site, ]

try :
	data += re.findall('[0-9]+', urllib.urlopen(url).read(), re.MULTILINE)
	print data[int(sys.argv[2]) - 1]
except :
	print 'Error! Can\'t retrieve this.'