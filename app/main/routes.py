from flask import render_template, url_for, redirect, request
from app.models import PhotoGroup, Photo, ImgTag
from app.main import bp
from app import db
from collections import defaultdict


@bp.route('/', methods=['GET'])
@bp.route('/index', methods=['GET'])
def index():
    photo_albums = PhotoGroup.query.all()
    photo_data = defaultdict(list)
    for photo_album in photo_albums:
        photo_list = Photo.query.filter(theme_id=photo_album.id, display=True)
        photo_data[photo_album] = photo_list
    return render_template('photo_list.html', title='摄影集', photo_data=photo_data)


