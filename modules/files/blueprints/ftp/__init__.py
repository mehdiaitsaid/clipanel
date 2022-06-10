
from .models import db



def setup():
    db.create_all()