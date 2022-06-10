from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)





with app.app_context():
    print('-'*20 + 'Initializing' + '-' * 20 )
    import app_module
    from auth import auth_required
    from hooks import setup
    setup()






@app.route('/')
def hello_world():

    return 'home'


@app.route('/test')
@auth_required
def test(current_user):
    # setup()

    return current_user.id





"""


# python3 -m venv venv 
# . venv/bin/activate 
 
https://www.the-analytics.club/python-shell-commands 
https://geekflare.com/securing-flask-api-with-jwt/
https://medium.com/analytics-vidhya/server-validation-in-flask-api-with-json-schema-963aa05e305f
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application

https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
"""
