from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class ForecastForm(FlaskForm):
    city = StringField('city')
    date = DateField('date', format='%d-%m-%y', validators=[DataRequired()])
    temperature = StringField('temperature')
