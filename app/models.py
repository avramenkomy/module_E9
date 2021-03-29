from app import db


class Forecast(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    temperature = db.Column(db.String(10), unique=False, nullable=False)
