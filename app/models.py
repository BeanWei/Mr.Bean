from app import db
from flask import current_app, url_for
from datetime import datetime, timedelta


class PhotoGroup(db.Model):
    """摄影集数据模型"""
    __tablename__ = 'photogroup'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    ctime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    photos = db.relationship('Photo', backref='theme', lazy='dynamic')

    def __repr__(self):
        return '<Photo Album {}>'.format(self.name)



photos_tags_table = db.Table(
    'photos_tags',
    db.Column('img_id', db.Integer, db.ForeignKey('photo.id')),
    db.Column('imgtag_id', db.Integer, db.ForeignKey('imgtag.id'))
)

class Photo(db.Model):
    """照片数据模型"""
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True)
    img_upload = db.Column(db.String(128))
    img_title = db.Column(db.String(128))
    img_context = db.Column(db.String(200))
    img_tags = db.relationship('ImgTag',
                                secondary=photos_tags_table, 
                                backref='photo', lazy='dynamic')
    is_top = db.Column(db.Boolean, default=False)
    like_count = db.Column(db.Integer, default=0)
    is_display = db.Column(db.Boolean, default=True)
    ctime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    theme_id = db.Column(db.Integer, db.ForeignKey('photogroup.id'))

    def __repr__(self):
        return '<Photo {}>'.format(self.img_title)


class ImgTag(db.Model):
    """照片标签数据模型"""
    __tablename__ = 'imgtag'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return '<ImgTag {}>'.format(self.tag_name)
