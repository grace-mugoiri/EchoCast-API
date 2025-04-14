import os

class Config:
    SQLAlCHEMY_DATABASE_URI = 'sqlite:///echocasts.db'
    SQLACHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    