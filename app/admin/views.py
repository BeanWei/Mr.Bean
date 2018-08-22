from flask import flash, redirect, url_for, render_template, session
from flask_admin import expose, BaseView
from flask_admin.contrib.sqla import ModelView
from app.models import PhotoGroup, Photo, ImgTag
from app.admin.forms import PhotoGroupForm, PhotoForm, ImgTagForm
from app import db
from datetime import datetime
from .github import github


class AuthView(ModelView):
    def _handle_view(self, name, **kwargs):
        if 'github_token' in session:
            me = github.get('user')
            return me
        return redirect(url_for('github.login'))


class PhotoGroupView(AuthView):
    """相册管理视图"""
    
    column_list = [
        'id',
        'name',
        'description',
        'ctime',
        'photos'
    ]
    column_searchable_list = ['name']
    column_filters = ['ctime']
    column_labels = {
        'id': '序号',
        'name': '相册',
        'description': '描述',
        'ctime': '创建时间',
        'photos': '相片'
    }
    form_excluded_columns = ['photos']

    @expose('/addalbum', methods=['GET', 'POST'])
    def addalbum(self):
        form = PhotoGroupForm()
        if form.validate_on_submit():
            album = PhotoGroup(name=form.name.data,
                               ctime=datetime.utcnow())
            db.session.add(album)
            db.session.commit()
            flash('新相册创建成功, 快去添加相片吧!')
            return redirect(url_for('addalbum'))
        albums = PhotoGroup.query.order_by(PhotoGroup.ctime.desc())
        return render_template('add_album.html', form=form,
                               albums=albums.items)

    def __init__(self, session, **kwargs):
        super().__init__(PhotoGroup, session, **kwargs)


class PhotoView(AuthView):
    """相片管理视图"""

    column_list = [
        'id',
        'link',
        'title',
        'context',
        'tags',
        'like_count',
        'ctime',
        'album',
        'is_top',
        'is_display'
    ]
    column_searchable_list = ['ctime']
    column_filters = ['ctime']
    column_labels = {
        'id': '序号',
        'link': '链接',
        'title': '标题',
        'context': '内容',
        'tags': '标签',
        'like_count': '喜欢',
        'ctime': '上传时间',
        'album': '相册',
        'is_top': '置顶',
        'is_display': '展示'
    }
    form_excluded_columns = ['like_count']

    @expose('/addphoto', methods=['GET', 'POST'])
    def addphoto(self):
        form = PhotoForm()
        form.alubm.choices = [(album, album.name)
                              for album in PhotoGroup.query.order_by('name')]
        form.tags.choices = [(tag, tag.name)
                             for tag in ImgTag.query.order_by('name')]

        if form.validate_on_submit():
            photo = Photo(album=form.alubm.data,
                          link=form.link.data,
                          title=form.title.data,
                          context=form.context.data,
                          tags=form.tags.data,
                          ctime=form.ctime.data,
                          is_top=form.istop.data,
                          is_display=form.isdisplay.data)
            db.session.add(photo)
            db.session.commit()
            flash('已成功上传相片')
            return redirect(url_for('addphoto'))
        return render_template('add_photo.html',form=form)

    def __init__(self, session, **kwargs):
        super().__init__(Photo, session, **kwargs)


class ImgTagView(AuthView):
    """相片标签管理视图"""

    column_list = ['id', 'name']
    column_labels = {'id': '序号',
                     'name': '标签',
                     'photo': '相片'}
    form_excluded_columns = ['photo']

    @expose('/addtag', methods=['GET', 'POST'])
    def addtag(self):
        form = ImgTagForm()
        if form.validate_on_submit():
            tag = ImgTag(name=form.name.data)
            db.session.add(tag)
            db.session.commit()
            flash('已成功添加标签')
            return redirect(url_for('addtag'))
        return render_template('add_tag.html', form=form)

    def __init__(self, session, **kwargs):
        super().__init__(ImgTag, session, **kwargs)


# class LogoutView(BaseView):
#     @expose('/logout')
#     def index(self):
#         return redirect(url_for('main.index'))