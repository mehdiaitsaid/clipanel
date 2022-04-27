from database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(250), primary_key=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250),  nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime,  nullable=False)
    updated_at = db.Column(db.DateTime,  nullable=False)
    deleted_at = db.Column(db.DateTime)