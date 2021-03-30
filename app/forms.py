from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import DateField, EmailField
from wtforms.validators import DataRequired, Email, email_validator


class ForecastForm(FlaskForm):
    city = StringField('city')
    date = DateField('date', format='%d-%m-%y', validators=[DataRequired()])
    temperature = StringField('temperature')


class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])


class CreateUserForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
