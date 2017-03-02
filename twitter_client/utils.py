# utility functions for Twitter API wrapper

import requests
import json

BASE_URL = 'https://api.twitter.com/'
VERSION = '1.1/'

# FUNCTION api_call(method, endpoint, url_params, auth_type, token, headers, data)
# builds the Twitter API call and executes it
#
# method : request method
# endpoint : API endpoint
# url_params : url parameters
# auth_type : authorization type (application or user)
# token : oauth token
# headers : custom headers
# data : form data
def api_call(method, endpoint, url_params = {}, auth_type = None, token = None, headers = {}, data = {}):

    headers.update({'Authorization': auth_type + ' ' + token})
    url = BASE_URL + VERSION + endpoint

    if method == 'GET':
        r = requests.get(url, params = url_params, headers = headers)
        return json.loads(r.text)
    if method == 'POST':
        r = requests.get(url, data = data, headers = headers)
        print json.loads(r.text)

# FUNCTION get_application_token(basic_token)
# retrieves application-only oauth token
#
# basic_token : base64 encoded consumer key and secret according to Twitter API specs
def get_application_token(basic_token):

    url = BASE_URL + 'oauth2/token'
    headers = {'Authorization': 'Basic ' + basic_token, 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
    data = {'grant_type': 'client_credentials'}

    response = requests.post(url, headers = headers, data  = data)
    return json.loads(response.text)['access_token']
