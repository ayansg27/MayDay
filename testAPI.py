import twitter

api=twitter.Api(
    consumer_key='OBBc9El0RrFsTGAJV2g7f0czx',
    consumer_secret='Mep0j3NOOP9RhUdWogog5d1bdPpAe5hb8FlzHecpL1HzaXPfN8',
    access_token_key='564713359-QDvMIwBFIeEv12GWtzwQzNp2bdyyZeUF4q100DRW',
    access_token_secret='khGMQDGwEm9HG9aWWvEJvFpEXVFPxVtM3AOxFMcrB5nm6')

hashtags_to_track = [
    "#instagood",
]
stream = api.GetStreamSample()
stream = api.GetStreamFilter(track=hashtags_to_track)
for line in stream:
    if 'in_reply_to_status_id' in line:
        tweet=twitter.Status.NewFromJsonDict(line)
        print("User: {user}, Tweet: '{tweet}'".format(user=tweet.user.screen_name,tweet=tweet.text))
