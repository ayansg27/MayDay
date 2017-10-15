from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import subprocess
customer_key='OBBc9El0RrFsTGAJV2g7f0czx'
customer_secret='Mep0j3NOOP9RhUdWogog5d1bdPpAe5hb8FlzHecpL1HzaXPfN8'
access_token='564713359-QDvMIwBFIeEv12GWtzwQzNp2bdyyZeUF4q100DRW'
access_secret='khGMQDGwEm9HG9aWWvEJvFpEXVFPxVtM3AOxFMcrB5nm6'

class listener(StreamListener):
    # def on_data(self, data):
    #     return(True)

    def on_status(self, status):
        print status.user.screen_name, status.text
        return

    def on_error(self, status):
        print status

def main():
    auth = OAuthHandler(customer_key, customer_secret)
    auth.set_access_token(access_token, access_secret)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["#trump"])      # use comma separated values
    


if __name__ == '__main__':
    main()

