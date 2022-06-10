
from flask import Blueprint

from modules.files.blueprints.file_explorer import files_explorer_app

files_app = Blueprint('files', __name__)



files_app.register_blueprint(files_explorer_app, url_prefix='/files-explore')
