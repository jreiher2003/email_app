import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail 

app = Flask(__name__) 
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
mail = Mail(app)

from app import views