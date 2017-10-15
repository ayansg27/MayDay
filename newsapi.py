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
    f = open('output.txt', 'w')
    for article in newsText["articles"]:
        print article["description"]
        print article["title"]
        f.write(json.dumps(article["description"], article["title"]))
        print "\n\n\n"
        #f.write(json.dumps(article))
    #f.write(json.dumps(newsText["articles"], indent=4, sort_keys=True))
    f.close()
except URLError, e:
    print 'Error reading news API'
