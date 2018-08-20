from app import creat_app, db
from app.models import PhotoGroup, Photo, ImgTag
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = creat_app()
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()