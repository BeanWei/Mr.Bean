from flask import flash, redirect, url_for, render_template
from flask_admin import expose
from flask_admin.contrib.sqla import ModelView
from app.models import PhotoGroup, Photo, ImgTag
from app.admin.forms import PhotoGroupForm, PhotoForm
from app import db
from datetime import datetime


class PhotoGroupView(ModelView):
    """相册管理视图"""
    
    coloumn_list = [
        'id',
        'name',
        'ctime',
        'photos'
    ]
    column_searchable_list = ['name']
    coloumn_filters = ['ctime']
    column_lables = {
        'id': '序号',
        'name': '相册', 
        'ctime': '创建时间',
        'photos': '相片'
    }

    @expose('/albums', methods=['GET', 'POST'])
    def albums(self):
        form = PhotoGroupForm()

        if form.validate_on_submit():
            album = PhotoGroup(name=form.name.data,
                               ctime=datetime.utcnow())
            db.session.add(album)
            db.session.commit()
            flash('新相册创建成功, 快去添加相片吧!')
            return redirect(url_for('photos'))
        albums = PhotoGroup.query.order_by(PhotoGroup.ctime.desc())
        return render_template('album_list.html', form=form,
                               albums=albums.items)

    def __init__(self, session, **kwargs):
        super().__init__(PhotoGroup, session, **kwargs)


class PhotoView(ModelView):
    """相片管理视图"""

    coloumn_list = [
        'id',
        'link',
        'title',
        'context',
        'tags',
        'like',
        'ctime',
        'album',
        'istop',
        'isdisplay'
    ]
    column_searchable_list = ['ctime']
    coloumn_filters = ['ctime']
    coloumn_lables = {
        'id': '序号',
        'link': '链接',
        'title': '标题',
        'context': '内容',
        'tags': '标签',
        'like': '喜欢',
        'ctime': '上传时间',
        'album': '相册',
        'istop': '置顶',
        'isdisplay': '展示'
    }

    def __init__(self, session, **kwargs):
        super().__init__(Photo, session, **kwargs)


class ImgTagView(ModelView):
    """相片标签管理视图"""

    coloumn_list = ['id', 'name']
    coloumn_lables = {'id': '序号', 'name': '标签'}

    def __init__(self, session, **kwargs):
        super().__init__(ImgTag, session, **kwargs)
