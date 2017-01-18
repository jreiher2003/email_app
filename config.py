import os 

class BaseConfig(object):
    DEBUG = False 
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_BINDS = {'linkedin': os.environ["LINKEDIN_DATABASE_URL"],
                        'myspace': os.environ["MYSPACE_DATABASE_URL"]}

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MAIL_SERVER = os.environ["MAIL_SERVER"]
    MAIL_USERNAME = os.environ["MAIL_USERNAME"]
    MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
    MAIL_DEFAULT_SENDER = '"Cloud Storage" <asciichan.tripplannr.com@gmail.com>'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    UPLOADED_PHOTOS_DEST = "/vagrant/app/static/img"

class ProductionConfig(BaseConfig):
    DEBUG = False
    UPLOADED_PHOTOS_DEST = "/var/www/email_app/email_app/app/static/img"
    MAIL_SERVER = os.environ["MAIL_SERVER"]
    MAIL_DEFAULT_SENDER = '"Cloud Storage" <email@asciichan-tripplannr.com>'