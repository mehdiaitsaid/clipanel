
from blinker import Namespace



namespace = Namespace()
before_app_init = namespace.signal('before_app_init')


@before_app_init.connect
def set(app, **kwargs):
    print('---------- --------- setup-auth2222')


def setup():
    print('---------- setup')
    before_app_init.send()
