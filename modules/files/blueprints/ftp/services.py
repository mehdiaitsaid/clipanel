from .models import File,db



def setup():
    db.create_all()