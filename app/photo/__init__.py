from flask import Blueprint

bp = Blueprint('photo', __name__)

from app.photo import routes