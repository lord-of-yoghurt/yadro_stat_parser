#!python2

import urllib, re, sys

serviceurl = 'http://counter.yadro.ru/values?'

if len(sys.argv) != 3 :
	print 'Error: Invalid number of arguments'
	exit()

site = sys.argv[1]
sel = int(sys.argv[2]) - 1

if sel < 1 or sel > 10 : 
	print 'Error: Invalid int argument (must be 1-11 inclusive)'
	exit()

url = serviceurl + urllib.urlencode({'site' : site})

print 'Retrieving', url

data = [site, ]

try :
	data += re.findall('^LI.* ([0-9]+)', urllib.urlopen(url).read(), re.MULTILINE)
	print data[sel]
except :
	print 'Error! Can\'t retrieve this.'