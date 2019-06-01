import  get_secrets # Contains user defined class retrieving getting keys and tokens
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

def get_tweets(query,count):
    tweets=[]
    fetched_data = api.search(q=query,count=count)
    for tweet in fetched_data:
        print(tweet) #live fetch of tweeter

consumer_key=get_secrets.get_secrets.get_consumer_key()
consumer_secret = get_secrets.get_secrets.get_consumer_secret()
access_token = get_secrets.get_secrets.get_access_token()
access_token_secret =get_secrets.get_secrets.get_access_token_secret()
try:
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    get_tweets("#HindiLanguage",1)
except Exception as e:
    print(ex)

