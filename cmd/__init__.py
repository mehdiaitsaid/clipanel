
from flask import Blueprint

cmd_app = Blueprint('cmd', __name__)


from .services import *
from .controller import *
from hooks import app_init


@app_init.connect
def setup(app, **kwargs):
    db.create_all()
