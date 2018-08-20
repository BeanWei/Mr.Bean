from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, ValidationError
from app.models import PhotoGroup



class PhotoGroupForm(FlaskForm):
    name = StringField('相册名称', validators=[DataRequired()])
    ctime = DateTimeField('创建时间')

    def validate_name(self, name):
        name = PhotoGroup.query.filter_by(name=name.data).first()
        if name is not None:
            raise ValidationError('此相册已存在')


class PhotoForm(FlaskForm):
    Alubm = StringField('相册', validators=[DataRequired()])
    link = StringField('相片地址', validators=[DataRequired()])
    title = StringField('标题', validators=[DataRequired()])
    context = StringField('内容', validators=[DataRequired()])
    tags = StringField('标签', validators=[DataRequired()])
    ctime = DateTimeField('创建时间')
    istop = BooleanField('置顶', validators=[DataRequired()])
    isdisplay = BooleanField('展示', validators=[DataRequired()])
    submit = SubmitField('确认')
