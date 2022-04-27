from flask import Flask, jsonify
import uuid
app = Flask(__name__)
import auth.services as auth


auth.setup()


@app.route("/")
def hello_world():
    auth.add_user('test','ait','root','roo@email.com')
    # admin = User(username='admin', email='admin@example.com')
    # guest = User(username='guest', email='guest@example.com')
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()
    return str(uuid.uuid4())




"""
 . venv/bin/activate 
https://geekflare.com/securing-flask-api-with-jwt/
https://medium.com/analytics-vidhya/server-validation-in-flask-api-with-json-schema-963aa05e305f
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application


"""
