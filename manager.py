from app import creat_app, db
from app.models import PhotoGroup, Photo, ImgTag
from app.admin.views import PhotoGroupView, PhotoView, ImgTagView
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin, AdminIndexView


app = creat_app()

admin = Admin(app, 'Mr.Bean', template_mode='bootstrap3', base_template='access_control.html',
              index_view=AdminIndexView(
                  name='导航栏',
                  url='/admin'
              ))

admin.add_view(PhotoGroupView(db.session, name='摄影集'))
admin.add_view(PhotoView(db.session, name='相片展'))
admin.add_view(ImgTagView(db.session, name='相片标签'))

from app.admin.github import github
app.add_template_global(github, 'github')


manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()