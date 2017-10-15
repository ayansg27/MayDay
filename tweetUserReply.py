import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
from pymongo import MongoClient
from textblob.classifiers import NaiveBayesClassifier

customer_key='uLL3io5y9UjBC0oS40jaxkGHY'
customer_secret='NYYxcXaOhLFX13FuuUVMUgUxUmSierjfbSAogDmG1iSAiqL6oV'
access_token='176101290-hlpATxSsfEl9VneX343HaRbdQYPdxk5KtpL6DVph'
access_secret='c3EoeSMbryCBp5lxAXq32W3VyeqehjlOfrg1eSaatFDtd'


class listener(StreamListener):

    def on_status(self, status):
        print status.text, status.user.id
        username = status.user.screen_name
        status_id = status.id
        retweet(username, status_id)

        pass


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def retweet(username, status_id):
    cfg = {
        "consumer_key": customer_key,
        "consumer_secret": customer_secret,
        "access_token": access_token,
        "access_token_secret": access_secret
    }
    api = get_api(cfg)
    tweet = "@%s Hello!" % (username)
    tweet += "Hey, would you like to volunteer for the victims? Email me at xxx.xxx@xxx!"
    #status = api.update_status(status=tweet, status_id)
    status = api.update_status(tweet, status_id)
    pass

def main():
  # cfg = {
  #   "consumer_key"        : customer_key,
  #   "consumer_secret"     : customer_secret,
  #   "access_token"        : access_token,
  #   "access_token_secret" : access_secret
  #   }

  auth = OAuthHandler(customer_key, customer_secret)
  auth.set_access_token(access_token, access_secret)

  twitterStream = Stream(auth, listener())
  twitterStream.filter(track=["#maydaycheck"])


  # api = get_api(cfg)
  # tweet = "Hey, would you like to volunteer for the victims? Email me at xxx.xxx@xxx!"
  # status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

