import os
import tweepy

from key import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# API 클라이언트를 생성한다.
api = tweepy.API(auth)

# 사용자 타임라인을 추출한다.
public_tweets = api.home_timeline()

for status in public_tweets:
    print("@" + status.user.screen_name, status.text)
