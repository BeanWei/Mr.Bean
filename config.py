import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL') or \
        'mysql:///' + os.path.join(basedir, 'app.sql')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_OUTPUT_PATH = os.environ.get('LOG_OUTPUT_PATH') or \
        os.path.join(basedir, './logs')
