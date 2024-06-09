import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_very_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:1234@localhost/trabalho_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
