import config
import os
from os import path
import requests
import json
import cryptoLogic

HOME_PATH = os.path.expanduser('~')
def registerUser(userData):
    registrationUrl = config.readConfig('AwsServiceUrl', 'aws.registration')

    response = requests.post(registrationUrl, data = json.dumps(userData))

    print(json.loads(response.text)["salt"])

    if response.status_code == 200:
        store_seed(userData,json.loads(response.text)["salt"])
        return True
    else:
        return False



def store_seed(userData,response):
    is_accessible = os.access(HOME_PATH, os.F_OK)  # Check if you have access, this should be a path
    if is_accessible == False:  # If you don't, create the path
        os.makedirs(HOME_PATH)
    os.chdir(HOME_PATH)  # Check now if the path exist

    seedName = userData["emailid"] + "_seed.enc"
    SEED_LOCATION = os.path.join(HOME_PATH, seedName)

    f = open(SEED_LOCATION, "w")

    encryptedSeed = cryptoLogic.encrypt(str(response["emailid_uuid"]), str(userData["password"]))
    f.write(encryptedSeed.decode())
    f.close()