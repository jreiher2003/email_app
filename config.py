import os 

class BaseConfig(object):
    DEBUG = False 
    SECRET_KEY = os.environ['SECRET_KEY']
    MAIL_SERVER = os.environ["MAIL_SERVER"]

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False