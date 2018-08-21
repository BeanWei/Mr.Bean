from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateTimeField, \
    SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError
from app.models import PhotoGroup, ImgTag



class PhotoGroupForm(FlaskForm):
    name = StringField('相册名称', validators=[DataRequired()])
    ctime = DateTimeField('创建时间')

    def validate_name(self, name):
        name = PhotoGroup.query.filter_by(name=name.data).first()
        if name is not None:
            raise ValidationError('此相册已存在，无需新建')


class PhotoForm(FlaskForm):
    alubm = SelectField('相册', validators=[DataRequired()])
    link = StringField('相片地址', validators=[DataRequired()])
    title = StringField('标题', validators=[DataRequired()])
    context = StringField('内容', validators=[DataRequired()])
    tags = SelectMultipleField('标签', validators=[DataRequired()])
    ctime = DateTimeField('创建时间')
    istop = BooleanField('置顶', validators=[DataRequired()])
    isdisplay = BooleanField('展示', validators=[DataRequired()])
    submit = SubmitField('确认')


class ImgTagForm(FlaskForm):
    name = StringField('标签', validators=[DataRequired()])

    def validate_name(self, name):
        name = ImgTag.query.filter_by(name=name.data).first()
        if name is not None:
            raise ValidationError('此标签已存在，无需添加')