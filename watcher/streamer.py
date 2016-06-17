import json
import tweepy
import config
from pymongo import MongoClient

config.TW_CONSUMER_KEY
auth = tweepy.OAuthHandler(config.TW_CONSUMER_KEY, config.TW_CONSUMER_SECRET)
auth.set_access_token(config.TW_ACCESS_TOKEN, config.TW_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


class ErgoStreamListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.db = MongoClient(host='db').ergo_tweet_watcher

    def on_timeout(self):
        return True

    def on_error(self, status_code):
        return True

    def on_data(self, status):
        self.db.tweets.insert(json.loads(status))

ergo_stream = tweepy.Stream(api.auth, ErgoStreamListener(api))
ergo_stream.filter(track=config.TW_STREAM_TERMS)
