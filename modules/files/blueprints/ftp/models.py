from database import db

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.String(250), primary_key=True)
    file = db.Column(db.String(250), nullable=False)