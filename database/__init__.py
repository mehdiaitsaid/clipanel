import os
from flask_sqlalchemy import SQLAlchemy
from main import app

try:
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir , 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)
    print("Connection to the database created successfully.")
except Exception as ex:
    print("Connection could not be made due to the following error: \n", ex)


