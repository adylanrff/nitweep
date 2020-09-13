import os
import tweepy

class TwitterClient():
    def __init__(self,
                 consumer_key=os.environ['TWITTER_API_KEY'],
                 consumer_secret=os.environ['TWITTER_API_SECRET_KEY'],
                 access_token=os.environ['TWITTER_ACCESS_TOKEN'],
                 access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
                ):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)