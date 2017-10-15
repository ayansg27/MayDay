# API Key: 4339258eb6b74848aabec09a921e47c0

#import requests
from datetime import datetime, timedelta
from pymongo import MongoClient
import json

from urllib2 import Request, urlopen, URLError

url = 'https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=4339258eb6b74848aabec09a921e47c0'
# run for multiple sources

#connect to db
client=MongoClient('localhost',27017)
db=client.mayday
#insert keywords
result=db.keywords.insert([
    {
        "keyword":"earthquake"
    },
    {
        "keyword":"hurricane"
    },
    {
        "keyword":"checkNeil"
    },
    {
        "keyword":"checkAyan"
    }
])


try:
    request = Request(url)
    response = urlopen(request)
    newsText = response.read()
    newsText = json.loads(newsText)
    print newsText
    for article in newsText["articles"]:
        if "hurricane" in article["description"].lower() or "hurricane" in article["title"].lower():
            # create hurricane event if not exists
            hrdt = datetime.now() - timedelta(hours=72)
            if db.events.find_one({"is_valid": "True", "timestamp": {"$gt": hrdt}}):
                pass
            else:
                result=db.events.insert_one(
                    {
                        "title":"hurricane",
                        "timestamp":datetime.now(),
                        "source":"news",
                        "volunteers":[],
                        "victims":[],
                        "volunteercount":0,
                        "victimcount":0
                    }
                )
                db.event_ids.insert_one(
                    {
                        "id":result.inserted_id,
                        "category":"hurricane"
                    }
                )

        if "earthquake" in article["description"].lower() or "earthquake" in article["title"].lower():
            # create earthquake event if not exists
            eqdt = datetime.now() - timedelta(hours=24)
            if db.events.find_one({"is_valid": "True", "timestamp": {"$gt": eqdt}}):
                pass
            else:
                result = db.events.insert_one(
                    {
                        "title": "earthquake",
                        "timestamp": datetime.now(),
                        "source": "news",
                        "volunteers": [],
                        "victims": [],
                        "volunteercount": 0,
                        "victimcount": 0
                    }
                )
                db.event_ids.insert_one(
                    {
                        "id": result.inserted_id,
                        "category": "hurricane"
                    }
                )

except URLError:
    print ('Error reading news API')