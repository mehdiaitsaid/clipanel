from auth import auth_required
from . import services, files_explorer_app
from flask import request, jsonify, make_response
from cerberus import Validator

from .validators import make_folder_schema


@files_explorer_app.route('/make-folder', methods=[ 'POST'])
@auth_required
def make_folder(current_user):
    data = request.get_json()
    v = Validator(make_folder_schema)

    if not v.validate(data):
        return make_response('The name of folder is required.', 401)
    services.make_folder(data['name'])
    return 'Ok'