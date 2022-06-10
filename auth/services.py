from flask import request, jsonify, make_response

from datetime import datetime
from datetime import timedelta
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import os

from .models import User,db


def add_user(first_name, last_name,password,email):
    hashed_password = generate_password_hash(password)
    new_user = User(id=str(uuid.uuid4()),
                           first_name=first_name,
                           last_name=last_name,
                           email=email,
                           created_at=datetime.now(),
                           updated_at=datetime.now(),
                           password=hashed_password)

    db.session.add(new_user)
    db.session.commit()
    return new_user

def login(email,password):
    user = User.query.filter_by(email=email).first()
    if check_password_hash(user.password, password):
        token = jwt.encode({'id': user.id, 'exp' : datetime.utcnow() + timedelta(minutes=1000)}, os.getenv("SECRET_JWT_KEY"), algorithm="HS256")
        return jsonify({'token' : token})
    return make_response('The email address or password is incorrect.',  401, {'WWW.Authentication': 'Basic realm: "login required"'})

def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        bearer = request.headers.get('Authorization')    # Bearer YourTokenHere
        if not bearer:
            return jsonify({'message': 'Authentication required. Sign in to your account.'})
        token = bearer.split()[1]
        if not token:
            return jsonify({'message': 'Authentication required. Sign in to your account.'})
        try:
            data = jwt.decode(token, os.getenv("SECRET_JWT_KEY"),  algorithms=['HS256'])
            current_user = User.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'Authentication required. Sign in to your account.'})
        return f(current_user, *args, **kwargs)
    return decorator

