import base64

from utils import get_application_token

from search import SearchAPI

# CLASS TwitterClient
# acts as the highest level interface for interacting with the Twitter API
#
# __init__ (consumer_key, consumer_secret)
#
# consumer_key : stores consumer_key
# consumer_secret : stores consumer_secrets
# basic_token : stores base64 encoded concatenation of consumer key and secret according to Twitter API specs
# bearer_token : stores Application-only authentication token
# search : instance of class SearchAPI
class TwitterClient(object):

    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.basic_token = base64.urlsafe_b64encode("%s:%s" % (consumer_key, consumer_secret))
        self.bearer_token = get_application_token(self.basic_token)
        self.search = SearchAPI(self.bearer_token)
