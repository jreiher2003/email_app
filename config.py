import os 

class BaseConfig(object):
    DEBUG = False 
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ['SECRET_KEY']
    MAIL_SERVER = os.environ["MAIL_SERVER"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_BINDS = {'linkedin': 'postgresql://will:finn7797@localhost/linkedin',
                        'myspace': 'postgresql://will:finn7797@localhost/myspace'}


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MAIL_USERNAME = os.environ["MAIL_USERNAME"]
    MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
    MAIL_DEFAULT_SENDER = '"Cloud Storage" <asciichan.tripplannr.com@gmail.com>'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PORT = 465

class ProductionConfig(BaseConfig):
    DEBUG = False