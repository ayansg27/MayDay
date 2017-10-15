# API Key: 4339258eb6b74848aabec09a921e47c0

import requests
import json

from urllib2 import Request, urlopen, URLError

url = 'https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=4339258eb6b74848aabec09a921e47c0'
# run for multiple sources

try:
    newsText = json.dumps('{}')
    request = Request(url)
    response = urlopen(request)
    newsText = response.read()
    newsText = json.loads(newsText)
    print newsText
    # f = open('output.txt', 'w')
    # f.write(json.dumps(newsText, indent=4, sort_keys=True))
    # f.close()
except URLError, e:
    print 'Error reading news API'
