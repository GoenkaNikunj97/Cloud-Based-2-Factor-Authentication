import wget
import os
from os import path

SAVED_USERNAME = "admin"
SAVED_PASSWORD = "admin"

def getSeedData():
    if(path.exists("C:\\loanApplication\\seed.txt")):
        temp = open("C:\\loanApplication\\seed.txt", "r")
        return temp
    return False

def isUserValid(userId, password):
    seed = getSeedData();

    if(seed):
        print("Local Seed Found");
        #print(seed.read())
        # Check if User and password is Correct
        if (userId == SAVED_USERNAME and password == SAVED_PASSWORD):
            return True
        else:
            return False
    else:
        print("Seed Not Found - Checking UserID")
        # Check if UserId is there in DB
        if(userId == SAVED_USERNAME):
            print("UserID found Getting Seed")
            url = "https://www.python.org/static/img/python-logo@2x.png"

            is_accessible = os.access("C:\\loanApplication", os.F_OK)  # Check if you have access, this should be a path
            if is_accessible == False:  # If you don't, create the path
                os.makedirs("C:\\loanApplication")
            os.chdir("C:\\loanApplication")  # Check now if the path exist

            wget.download(url, 'C:\\loanApplication\\seed.png')

            return True
