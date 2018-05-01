import requests
import sys
import webbrowser
import bs4

print('searching...') 

req = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
req.raise_for_status()

soup = bs4.BeautifulSoup(req.text)
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
webbrowser.open('htpp://google.com' + linkElems[i].get('href'))
