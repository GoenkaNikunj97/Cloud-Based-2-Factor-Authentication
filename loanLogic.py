import config
import os
from os import path
import requests
import json
from werkzeug.utils import secure_filename
import base64

LOAN_URL = config.readConfig('AwsServiceUrl', 'applyLoan')

def appLoan(userData):
    uploadURL = config.readConfig('AwsServiceUrl', 'uploadFile')
    dataToSend = json.loads(json.dumps({
        "emailid": userData["emailid"],
        "send_mail": "true",
        "update_user_loan": "true",
        "username": userData["name"],
        "application_status": "submitted",
        "loan_amount": userData["amount"],
        "loan_tenure_in_days":userData["time"],
        "dob": userData["dob"],
        "annual_income": userData["income"]
    }))

    file = userData["loanFile"]
    #file = secure_filename(file.filename)
    sample_string = file.read()
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    #sample_string_bytes = sample_string.encode(file.read())
    #file = userData["emailid"].filename
    file_response = requests.post(uploadURL, base64_bytes ,headers={ "Content-Type":"application/pdf","emailid" : userData["emailid"]})
    #response = requests.post(LOAN_URL, data=json.dumps(dataToSend))
    print(file_response.text)
    '''
    if (response.status_code == 200):
        return True
    else:
        return False
        '''


def trackLoan(emailid):
    userData = json.loads( json.dumps({
        "emailid" : emailid,
        "send_mail": "false",
        "update_user_loan" : "false",
    }))

    response = requests.post(LOAN_URL, data=json.dumps(userData))
    if (response.status_code == 200):
        response = json.loads(response.text)
        print( response )

        application_data = response["loan_status"]
        return application_data["application_status"]
    else:
        return False