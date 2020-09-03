import os
import tweepy

from key import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print("@" + status.author.screen_name, status.text)

stream = tweepy.Stream(auth, MyStreamListener())

stream.sample(languages=['ko'])