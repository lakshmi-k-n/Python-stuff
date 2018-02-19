import requests
import json

def ip():
	response = requests.get("http://httpbin.org/get")
	j=json.loads(response.text)
	print j[""u'origin'""]

ip()
	
