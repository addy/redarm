import requests
import json

API_URL = 'http://catfacts-api.appspot.com/api/facts?'

def getCatFacts(num):
    param = {'number' : num}
    res = requests.get(API_URL, params=param)
    res = res.json()
    if res['success'] == "true":
        return res['facts']
    else:
        return False
