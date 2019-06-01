"""
Author : Ruchitesh Malukani
Objective of application : Determine whether a piece of writing is positive, negative or neutral.
"""

# imports
import  get_secrets # Contains user defined class retrieving getting keys and tokens
import re
import tweepy
from tweepy import OAuthHandler
import pprint
from textblob import TextBlob #NLP


def Cleaner(tweetbody):
    print("__"*50+"Original"+"__"*50)
    print(tweetbody)
    print("__" * 50 + "Cleaned" + "__" * 50)
    regex = r"(@\w+)" # Find user tags(for example @user)
    tweetbody=''.join(re.sub(regex,"",tweetbody)) # Remove matched pattern
    regex = r"(\w+:\/\/\S+)" #find links
    tweetbody=''.join(re.sub(regex,"",tweetbody))#remove links
    regex = r"(#\w+)"  # Find hash tags(for example #NZvSL)
    tweetbody = re.sub(regex, "", tweetbody)  # Replace matched pattern with space
    regex = r"[^0-9A-z \t]" # Find special characters
    tweetbody=''.join(re.sub(regex,"",tweetbody)) # remove special characters
    regex = r"(\s)"
    tweetbody = ''.join(re.sub(regex," ", tweetbody))
    tweetbody=" ".join(tweetbody.split()) # Multiple space characters with single space character
    print(tweetbody)
    print("__"*100)

# query : search query
# count : number of tweets to be fetched
def get_tweets(query,count):
    tweets=[]
    fetched_data = api.search(q=query,count=count)
    for tweet in fetched_data:
        # print(tweet.text) #fetched tweet
        tweets.append(tweet.text)
    return tweets

consumer_key=get_secrets.get_secrets.get_consumer_key()
consumer_secret = get_secrets.get_secrets.get_consumer_secret()
access_token = get_secrets.get_secrets.get_access_token()
access_token_secret =get_secrets.get_secrets.get_access_token_secret()
try:
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)
    query=input("Search Query : ")
    tweets = get_tweets(query,10)
    for tweetbody in tweets:
        Cleaner(tweetbody)
except Exception as e:
    print(e)

