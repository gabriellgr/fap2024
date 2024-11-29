import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite://clinica.db'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = os.uramdon(24)

    