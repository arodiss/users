from sqlalchemy import Column, Integer, String
from database import Base
from flask_login import UserMixin


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(31), unique=True)
    password = Column(String(31), unique=False)

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)