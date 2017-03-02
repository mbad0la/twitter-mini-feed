from flask import Flask, redirect

from twitter_client import TwitterClient
from credentials import CONSUMER_KEY, CONSUMER_SECRET

# initialise twitter api wrapper
twitter = TwitterClient(CONSUMER_KEY, CONSUMER_SECRET)

app = Flask(__name__)

# respond '/' request with index.html
@app.route('/')
def send_index():
    return app.send_static_file('index.html')

# respond '/resources/<path:path>' request with
# static file at `path` inside `static` folder
@app.route('/resources/<path:path>')
def send_resources(path):
    return app.send_static_file(path)

# respond '/api/custserv' request with tweets with hashtag `#custserv`
# and `retweet_count` greater than 0
@app.route('/api/<hashtag>')
def custserv_responses(hashtag):
    return twitter.search.tweets_by_hashtag(hashtag = hashtag)

if __name__ == "__main__":
    app.run()
