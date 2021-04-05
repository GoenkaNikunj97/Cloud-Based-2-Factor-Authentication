import wget
import os
from os import path
import requests

import cryptoLogic

BASE_URL = "https://7mqeagvdnf.execute-api.us-east-1.amazonaws.com/"
success = "Success"
SAVED_USERNAME = "admin"
SAVED_PASSWORD = "admin"

def getSeedData():
    if(path.exists("C:\\loanApplication\\seed.txt")):
        temp = open("C:\\loanApplication\\seed.txt", "r")
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

            queryUrl = "https://g52kmvfp98.execute-api.us-east-1.amazonaws.com/download_seed?emailId"+userId
            res = requests.get(queryUrl)
            seed = res.text

            is_accessible = os.access("C:\\loanApplication", os.F_OK)  # Check if you have access, this should be a path
            if is_accessible == False:  # If you don't, create the path
                os.makedirs("C:\\loanApplication")
            os.chdir("C:\\loanApplication")  # Check now if the path exist

            f = open("C:\\loanApplication\\seed.txt", "w")
            encrptedSeed = cryptoLogic.encrypt(seed , password)
            f.write(encrptedSeed.decode())
            f.close()
            return True
