import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail 
from flask_uploads import UploadSet, configure_uploads, IMAGES, UploadNotAllowed

app = Flask(__name__) 
app.config.from_object(os.environ['APP_SETTINGS'])

uploaded_photos = UploadSet('photos', IMAGES)
configure_uploads(app, uploaded_photos)

db = SQLAlchemy(app)
mail = Mail(app)

from app import views