from datetime import datetime
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
from .models import User,db
from hooks import before_app_init

@before_app_init.connect
def setup(app, **kwargs):
    print('---------- ---------------------------- setup-auth')
    db.create_all()

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

