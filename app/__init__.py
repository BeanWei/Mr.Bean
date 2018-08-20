import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from config import Config


db = SQLAlchemy()
login = LoginManager()
moment = Moment()

def creat_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)
    moment.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    #根据生产环境决定是否保存logs信息
    if not app.debug:
        logs_file_handler = RotatingFileHandler(
            os.path.join(app.config['LOG_OUTPUT_PATH'], 'app.log'),
                            maxBytes=10240, backupCount=10)
        logs_file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s'
            '[in %(pathname)s: %(lineno)s]'))
        logs_file_handler.setLevel(logging.INFO)
        app.logger.addHandler(logs_file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Mr.Bean is coming')
    
    return app


from app import models
