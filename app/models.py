from app import db
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()
metadata = Base.metadata


class Forecast(Base):
    __tablename__ = 'forecast'
    _id = Column(Integer, primary_key=True)
    date = Column(Date, unique=False, nullable=False)
    city = Column(String(80), unique=False, nullable=False)
    temperature = Column(String(10), unique=False, nullable=False)


class User(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated
