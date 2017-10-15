# API Key: 4339258eb6b74848aabec09a921e47c0

import requests
import json

from urllib2 import Request, urlopen, URLError

url = 'https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=4339258eb6b74848aabec09a921e47c0'
# run for multiple sources

try:
    request = Request(url)
    response = urlopen(request)
    newsText = response.read()
    newsText = json.loads(newsText)
    for article in newsText["articles"]:
        if "hurricane" in article["description"].lower() or "hurricane" in article["title"].lower():
            # create hurricane event if not exists
            pass
        if "earthquake" in article["description"].lower() or "earthquake" in article["title"].lower():
            # create earthquake event if not exists
            pass
except URLError, e:
    print 'Error reading news API'
