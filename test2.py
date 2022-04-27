from flask import Blueprint

app_test2 = Blueprint('test2', __name__,
                        template_folder='templates')

@app_test2.route("/tt2")
def test2():
    return "<p>Hello, test222!</p>"

