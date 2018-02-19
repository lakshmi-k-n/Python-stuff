import urllib
import sys
import re
def antihtml(url=sys.argv[1]):
	urllib.urlretrieve(sys.argv[1],'web')
	x=re.findall(r'>[^<]+<',open('web').read())
	for n in x:
		print n[1:-1]
antihtml() 
