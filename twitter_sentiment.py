#Create an app in twitter -> apps.twitter.com
#Install pip install tweepy -> used to communicate with the twitter api
#Install pip install textblob -> used for analysis

import tweepy
from textblob import TextBlob

consumer_key = "#"
consumer_secret = "#"

access_token = "#"
access_token_secret = "#"

#created authication variable
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

#Created api variable
api = tweepy.API(auth)

#Created a variable that displays public tweets based on the people I follow on twitter
public_tweets = api.search('Zambia')

#Creaed a for loop
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
