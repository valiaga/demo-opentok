import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    # SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

from common import Credenciales, fire_Config

api_key = Credenciales().getApiKey()
api_secret = Credenciales().getApiSecret()

# Configudacion de firebase
fire_config ={
    "apiKey": fire_Config().getApiKey(),
    "authDomain": fire_Config().getAuthDomain(),
    "databaseURL": fire_Config().getDatabaseURL(),
    "storageBucket": fire_Config().getStorageBucket()
}