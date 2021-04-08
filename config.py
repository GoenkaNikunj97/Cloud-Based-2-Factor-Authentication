import os
import configProperties as c

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'SecretKey'

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT=True
    DEBUG=True

def readConfig(section,key):

    return c.get(section, key)

SQLALCHEMY_DATABASE_URI="DB_URL"