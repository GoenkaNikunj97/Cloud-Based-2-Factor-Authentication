import requests
import json
import config

def registerUser(userData):
    registrationUrl = config.readConfig('AwsServiceUrl', 'aws.registration')

    print(json.dumps(userData))
    response = requests.post(registrationUrl, body = json.dumps(userData))

    print(response.content)

    if (response.status_code == 200):
        return True
    else:
        return False