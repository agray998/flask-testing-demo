from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Add(FlaskForm):
    add = StringField("Add Item:")
    submit = SubmitField("Submit!")