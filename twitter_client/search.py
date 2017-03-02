from utils import api_call
import json

# CLASS SearchAPI
# acts as the interface for interacting with the Twitter API's `/search` endpoints
#
# __init__ (token, auth_type = 'Bearer')
# auth_type : helps seperate user token from application token
#
# main_route : stores parent endpoint belonging to a certain type (eg. search)
# auth_type : helps seperate user token from application token
# token : stores the oauth token to be used for making API requests
class SearchAPI(object):

    def __init__(self, token, auth_type = 'Bearer'):
        self.main_route = 'search'
        self.auth_type = auth_type
        self.token = token

    def tweets_by_hashtag(self, hashtag = '#custserv', retweet_threshold = 0, count = 100):
        endpoint = self.main_route + '/tweets.json'
        # hit the API
        response = api_call('GET', endpoint, url_params = {'q': hashtag, 'count': count}, auth_type = self.auth_type, token = self.token)
        # extract tweets list
        response = response['statuses']
        # filter tweets based on whether the `retweet_count` is greater than the `retweet_threshold`
        filtered_response = [tweet for tweet in response if tweet['retweet_count'] > retweet_threshold]
        # convert to json and return
        return json.dumps(filtered_response)
