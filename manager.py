from app import creat_app, db
from app.models import PhotoGroup, Photo, ImgTag

app = creat_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'PhotoGroup': PhotoGroup, 'Photo': Photo, 'ImgTag': ImgTag}

if __name__ == '__main__':
    app.run(debug=True)