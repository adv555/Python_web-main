import pathlib
from dotenv import dotenv_values

config = dotenv_values(".env")

BASE_DIR = pathlib.Path(__file__).parent.parent


class Config:
    SECRET_KEY = config['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'contact.sql')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
