from flask import current_app as app
from flask import request, jsonify, make_response
from cerberus import Validator
from auth import services, auth_app
from auth.validators import login_schema


@auth_app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    v = Validator(login_schema)
    if not v.validate(auth):
        return make_response('The email address or password is incorrect.', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
    return services.login(auth['email'],auth['password'])