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


# clone repo and delete venv folder 
# python -m venv venv 
# . venv/bin/activate 
# pip install -r requirements.txt
 

"""
