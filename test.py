from flask import Blueprint
from test2 import app_test2

app_test = Blueprint('test', __name__,
                        template_folder='templates')
app_test.register_blueprint(app_test2, url_prefix='/test2')

@app_test.route("/tt")
def test():
    return "<p>Hello, test!aaaaagggqqw</p>"

