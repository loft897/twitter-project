import tweepy
import csv

consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret'
access_token = 'your-access-token'
access_token_secret = 'your-access-token-secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        with open('tweets.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([status.created_at, status.user.screen_name, status.text])

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['keyword']) # replace 'keyword' with the keyword you want to track
 
