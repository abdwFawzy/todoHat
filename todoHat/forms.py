from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo

class registerform(FlaskForm):
    username = StringField('username',
                            validators=[DataRequired(), Length(min=2,max=20)])
    password = PasswordField('password',
                            validators=[DataRequired(),Length(min=8)])
    confirm =  PasswordField('confirmation',
                            validators=[DataRequired(),Length(min=8), EqualTo('password')])
    submit = SubmitField('sign Up')

class loginform(FlaskForm):
    username = StringField('username',
                            validators=[DataRequired(), Length(min=2,max=20)])
    password = PasswordField('password',
                            validators=[DataRequired(),Length(min=8)])
    submit = SubmitField('log in')