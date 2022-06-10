
from flask import current_app as app

from cmd import services, cmd_app


@cmd_app.route('/test')
def test():
    # setup()
    services.args_command(['mkdir', 'cmd_dire'])
    return 'Done'