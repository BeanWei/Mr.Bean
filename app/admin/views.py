from flask_admin import  BaseView
from app.models import PhotoGroup, Photo, ImgTag


class PhotoGroupView(BaseView):
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
    
    def __init__(self, session, **kwargs):
        super().__init__(PhotoGroup, session, **kwargs)


class PhotoView(BaseView):
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


class ImgTagView(BaseView):
    """相片标签管理视图"""

    coloumn_list = ['id', 'name']
    coloumn_lables = {'id': '序号', 'name': '标签'}

    def __init__(self, session, **kwargs):
        super().__init__(ImgTag, session, **kwargs)
