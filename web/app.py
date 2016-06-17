from flask import Flask
from flask import render_template
import pymongo
from bson import json_util

app = Flask(__name__)

db = pymongo.MongoClient(host='db').ergo_tweet_watcher


@app.route('/')
def index():
    tweets = latest_tweets()

    return render_template('index.html', tweets=tweets)


@app.route('/api/latest-tweets')
def latest_tweets():
    recent_tweets = db.tweets.find(
        {},
        {'text': 1, 'created_at': 1},
        limit=30
    ).sort('created_at', pymongo.DESCENDING)
    return json_util.dumps({'tweets': recent_tweets})


if __name__ == '__main__':
    app.run('0.0.0.0')
