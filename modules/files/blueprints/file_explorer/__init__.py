from flask import Blueprint

files_explorer_app = Blueprint('files-explore', __name__)


from .services import *
from .controller import *
from .cli import *
from hooks import app_init

from .models import db


def setup():
    db.create_all()