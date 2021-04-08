import config
import os
from os import path
import requests
import json
import cryptoLogic

LOAN_URL = config.readConfig('AwsServiceUrl', 'applyLoan')

def appLoan(userData):
    response = requests.post(registrationUrl, data=json.dumps(userData))

    print(json.loads(response.text))

def trackLoan(emailid):
    userData = json.loads( json.dumps({
        "emailid" : emailid,
        "send_mail": "false",
        "update_user_loan" : "false",
    }))

    print(LOAN_URL)
    print(userData)
    response = requests.post(LOAN_URL, data=json.dumps(userData))
    if (response.status_code == 200):
        response = json.loads(response.text)
        print( response )

        application_data = response["loan_status"]
        return application_data["application_status"]
    else:
        return False

'''
/email, mail
'''