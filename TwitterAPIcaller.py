import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
from pymongo import MongoClient
from textblob.classifiers import NaiveBayesClassifier


customer_key=''
customer_secret=''
access_token=''
access_secret=''


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
                # retweet
                username = status.user.screen_name
                status_id = status.id
                cfg = {
                    "consumer_key": customer_key,
                    "consumer_secret": customer_secret,
                    "access_token": access_token,
                    "access_token_secret": access_secret
                }
                api = get_api(cfg)
                tweet = "@%s Hello!" % (username)
                tweet += "\nWould you like to volunteer for the victims? Email me your contact information at xxx.xxx@xxx!"
                status = api.update_status(tweet, status_id)
                # add to db
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


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


# def retweet(username, status_id):
#     cfg = {
#         "consumer_key": customer_key,
#         "consumer_secret": customer_secret,
#         "access_token": access_token,
#         "access_token_secret": access_secret
#     }
#     api = get_api(cfg)
#     tweet = "@%s Hello!" % (username)
#     tweet += "Hey, would you like to volunteer for the victims? Email me at xxx.xxx@xxx!"
#     #status = api.update_status(status=tweet, status_id)
#     status = api.update_status(tweet, status_id)


def main():
    auth = OAuthHandler(customer_key, customer_secret)
    auth.set_access_token(access_token, access_secret)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["help"])
    #twitterStream.sample()


if __name__ == '__main__':
    main()
