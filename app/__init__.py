from flask import Flask
from flask_sqlalchemy import SQLAlchemy as sqla
from config import Config
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object(Config)
db = sqla(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
db.create_all()

from app import routes, models
