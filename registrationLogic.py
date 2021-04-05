import requests
import json


def registerUser(UserData):
    queryUrl = "https://g52kmvfp98.execute-api.us-east-1.amazonaws.com/download_seed"
    res = requests.post(queryUrl, data = UserData)
    responseData = json.loads(res.text)['message']
    if (res.status_code == 200):
        return True
    else:
        return False