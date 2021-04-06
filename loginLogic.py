import os
from os import path
import requests
import json
import cryptoLogic
import config

BASE_URL = config.readConfig('AwsServiceUrl', 'baseURL')

VALIDATE_USER_URL = config.readConfig('AwsServiceUrl', 'validateUser')
VALIDATE_OTP_URL = config.readConfig('AwsServiceUrl', 'validateOtp')

SEND_OTP_URL = config.readConfig('AwsServiceUrl', 'sendOtp')

HOME_PATH = os.path.expanduser('~')

def getLocalSeed(userId):
    seedName = userId + "_seed.txt"
    SEED_LOCATION = os.path.join(HOME_PATH, seedName)
    print(SEED_LOCATION)
    if(path.exists(SEED_LOCATION)):
        temp = open(SEED_LOCATION, "r")
        data = temp.read()
        temp.close()
        return data
    return False

def isUserValid(userId, password, otp=""):
    userData = json.dumps({
        "emailid": userId,
        "password": password
    })
    url = BASE_URL + VALIDATE_USER_URL
    res = requests.post(url, data=userData)

    resData = json.loads(res.text)["response"]
    print(resData)
    if (res.status_code == 200):
        isSeedPresent = getLocalSeed(userId)
        if(isSeedPresent):
            print("Local Seed Found")
            try:
                decryptedSeed = cryptoLogic.decrypt(isSeedPresent, password)
            except:
                responseToReturn = {
                    "isCorrect": False,
                    "message": "Password Wrong"
                }
                return responseToReturn
            print(decryptedSeed)
            responseToReturn = {
                "isCorrect": True,
                "message": ""
            }
            return responseToReturn
        else:
            print("Seed Not Found")
            if(otp):
                print("Inside OTP:"+ str(otp))
                url = BASE_URL + VALIDATE_OTP_URL
                userData = json.dumps({
                    "emailid": userId,
                    "user_otp": otp
                })
                res = requests.post(url, data=userData)
                print(json.loads(res.text))
                if(res.status_code == 200):
                    is_accessible = os.access(HOME_PATH, os.F_OK)  # Check if you have access, this should be a path
                    if is_accessible == False:  # If you don't, create the path
                        os.makedirs(HOME_PATH)
                    os.chdir(HOME_PATH)  # Check now if the path exist

                    seedName = userId + "_seed.txt"
                    SEED_LOCATION = os.path.join(HOME_PATH, seedName)

                    f = open(SEED_LOCATION, "w")

                    if(password == str(resData["password"])):
                        encrptedSeed = cryptoLogic.encrypt(str(resData["emailid_uuid"]) , str(resData["password"]))
                        f.write(encrptedSeed.decode())
                        f.close()
                        responseToReturn = {
                            "isCorrect": True,
                            "message": ""
                        }
                        return responseToReturn
                else:
                    responseToReturn = {
                        "isCorrect": False,
                        "message": "OTP is Wrong"
                    }
                    return responseToReturn
            else:
                url = BASE_URL + SEND_OTP_URL
                requests.post(url, data=userData)
                responseToReturn = {
                    "isCorrect" : False,
                    "message" : "OTP"
                }
                return responseToReturn

    responseToReturn = {
        "isCorrect": False,
        "message": "invalid User"
    }
    return responseToReturn