from app import creat_app, db
from app.models import PhotoGroup, Photo, ImgTag
from app.admin.views import PhotoGroupView, PhotoView, ImgTagView
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView


app = creat_app()

admin = Admin(app, 'Mr.Bean', template_mode='bootstrap3')

admin.add_view(PhotoGroupView(db.session, name='摄影集'))
admin.add_view(PhotoView(db.session, name='相片展'))
admin.add_view(ImgTagView(db.session, name='相片标签'))


manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()