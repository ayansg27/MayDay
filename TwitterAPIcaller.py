from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
from pymongo import MongoClient
from textblob.classifiers import NaiveBayesClassifier

customer_key='OBBc9El0RrFsTGAJV2g7f0czx'
customer_secret='Mep0j3NOOP9RhUdWogog5d1bdPpAe5hb8FlzHecpL1HzaXPfN8'
access_token='564713359-QDvMIwBFIeEv12GWtzwQzNp2bdyyZeUF4q100DRW'
access_secret='khGMQDGwEm9HG9aWWvEJvFpEXVFPxVtM3AOxFMcrB5nm6'


class listener(StreamListener):

    def on_status(self, status):
        #print status.user.screen_name, status.text
        # # loading classifier

        with open('TweetClassifierMapping.json', 'r') as f:
        #f = open("TweetClassifierMapping.json", 'r')
            cl=NaiveBayesClassifier(f,format="json")
        # connect to db
        client = MongoClient('localhost', 27017)
        db = client.mayday
        cursor = db.keywords.find()
        keywords = []
        for doc in cursor:
            keywords.append(doc["keyword"])
        # use cl to check
        wiki=TextBlob(status.text)
        for word in wiki.words:
            if word in keywords and cl.classify(status.text)=='pos':
                event=""
                if "hurricane" in keywords:
                    event="hurricane"
                else:
                    event="earthquake"
                result = db.events.update_one(
                    {"name": event},
                    {"$push": {"volunteers": {"username": status.user.screen_name}}}
                )

    def on_error(self, status):
        print status



def main():
    auth = OAuthHandler(customer_key, customer_secret)
    auth.set_access_token(access_token, access_secret)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["help"])
    #twitterStream.sample()


if __name__ == '__main__':
    main()