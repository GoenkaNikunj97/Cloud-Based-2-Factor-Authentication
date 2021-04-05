import wget
import os
from os import path
import requests
import json
import cryptoLogic

BASE_URL = "https://7mqeagvdnf.execute-api.us-east-1.amazonaws.com/"
HOME_PATH = os.path.expanduser('~')
SEED_LOCATION = os.path.join(HOME_PATH , "seed.enc")

def getSeedData():
    if(path.exists(SEED_LOCATION)):
        temp = open(SEED_LOCATION, "r")
        data = temp.read()
        temp.close()
        return data
    return False

def isUserValid(userId, password):
    seed = getSeedData();

    if(seed):
        print("Local Seed Found");

        decryptedSeed = cryptoLogic.decrypt(seed , password)
        decryptedSeed = hash(decryptedSeed)

        queryUrl = BASE_URL + "validate_hash?hash=" + str(decryptedSeed)
        res = requests.get(queryUrl)

        if (res.status_code == 200):
            return True
        else:
            return False
    else:
        print("Seed Not Found - Checking UserID")
        # Check if UserId is there in DB
        queryUrl = BASE_URL+"validate_user?emailId="+userId
        res = requests.get(queryUrl)
        output = res.status_code
        if(output == 200):
            print("UserID found Getting Seed")

            queryUrl = "https://g52kmvfp98.execute-api.us-east-1.amazonaws.com/download_seed"

            userData={
                'emailid':userId,
                'password':password
            }

            userData = json.dumps(userData)
            print(userData)
            requests.post(queryUrl, json=userData)
            res = requests.get(queryUrl)
            print(res.text);

            responseData = json.loads(res.text)['message']

            is_accessible = os.access(HOME_PATH, os.F_OK)  # Check if you have access, this should be a path
            if is_accessible == False:  # If you don't, create the path
                os.makedirs(HOME_PATH)
            os.chdir(HOME_PATH)  # Check now if the path exist

            #f = open(SEED_LOCATION, "w")
            #encrptedSeed = cryptoLogic.encrypt(responseData , password)
            #f.write(encrptedSeed.decode())
            #f.close()

            return True