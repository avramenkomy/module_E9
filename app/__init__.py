from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sqla
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = sqla(app)
db.create_all()

from app import routes, models
