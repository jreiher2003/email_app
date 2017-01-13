import os 

class BaseConfig(object):
    DEBUG = False 
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ['SECRET_KEY']
    MAIL_SERVER = os.environ["MAIL_SERVER"]
    DATABASE_URL = os.environ["DATABASE_URL"]

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False