from database import db

class Cmd(db.Model):
    __tablename__ = 'cmds'
    id = db.Column(db.String(250), primary_key=True)
    key = db.Column(db.String(250), unique=True)  #module name + unique key ex : FTP_ADD_USER
    cmd = db.Column(db.String(300), nullable=False)
    args = db.Column(db.String(300), nullable=False)
    distribution = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime,  nullable=False)
    updated_at = db.Column(db.DateTime,  nullable=False)
    deleted_at = db.Column(db.DateTime)