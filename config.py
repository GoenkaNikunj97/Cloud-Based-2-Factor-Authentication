import os
import configparser
import configProperties as c

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'SecretKey'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT=True
    DEBUG=True

def readConfig(section,key):

    #configParser = configparser.RawConfigParser()
    #configParser.read('configFile.properties')
    return c.get(key)
    #return configParser.get(section, key)

SQLALCHEMY_DATABASE_URI="DB_URL"