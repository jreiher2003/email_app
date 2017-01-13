from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, DataRequired
from wtforms.fields.html5 import EmailField

class EmailForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(message="You need to put in a username"), Email()])