import urllib
import sys
def wget(url=sys.argv[1]):
	url1=url.split('/')
	name=url1[-1]
	if name=='':
		name="index.html"
	urllib.urlretrieve(url,name)
	
wget()
