import  get_secrets # User defined class for getting keys and tokens
import re
import tweepy
from tweepy import OAuthHandler
consumer_key=get_secrets.get_secrets.get_consumer_key()
consumer_secret = get_secrets.get_secrets.get_consumer_secret()
access_token = get_secrets.get_secrets.get_access_token()
access_token_secret =get_secrets.get_secrets.get_access_token_secret()
try:
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
except Exception as e:
    print(ex)

