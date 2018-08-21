from app import db
from flask import current_app, url_for
from datetime import datetime, timedelta


class PhotoGroup(db.Model):
    """摄影集数据模型"""
    __tablename__ = 'photogroup'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.String(300))
    ctime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    photos = db.relationship('Photo', backref='theme')

    def __repr__(self):
        return self.name



photos_tags_table = db.Table(
    'photos_tags',
    db.Column('img_id', db.Integer, db.ForeignKey('photo.id')),
    db.Column('imgtag_id', db.Integer, db.ForeignKey('imgtag.id'))
)

class Photo(db.Model):
    """照片数据模型"""
    __tablename__ = 'photo'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(128))
    title = db.Column(db.String(128))
    context = db.Column(db.String(200))
    tags = db.relationship('ImgTag',
                            secondary=photos_tags_table,
                            backref=db.backref('photo', lazy='dynamic'))
    is_top = db.Column(db.Boolean, default=False)
    like_count = db.Column(db.Integer, default=0)
    is_display = db.Column(db.Boolean, default=True)
    ctime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    album = db.Column(db.Integer, db.ForeignKey('photogroup.id'))

    def __repr__(self):
        return self.title


class ImgTag(db.Model):
    """照片标签数据模型"""
    __tablename__ = 'imgtag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return self.name
