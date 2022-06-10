
from flask import Blueprint
from flask.cli import AppGroup


from modules.files.blueprints.file_explorer import files_explorer_app

files_app = Blueprint('files', __name__)




files_app.register_blueprint(files_explorer_app, url_prefix='/files-explore',cli_group='files')
