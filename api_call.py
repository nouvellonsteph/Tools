
url = 'https://www.justalittlebyte.ovh'

import urllib2

#opener = urllib2.build_opener()
#opener.addheaders = [('host', 'www.justalittlebyte.ovh')]
#opener.open(url)

req = urllib2.Request(url, '',)
req.add_header = ('User-agent', 'Mozilla/5.0'), ('host', 'www.justalittlebyte.ovh') , ('X-CF-Trace', '1')
resp = urllib2.urlopen(req)
