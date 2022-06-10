
from blinker import Namespace



namespace = Namespace()
app_init = namespace.signal('app_init')



def setup():
    app_init.send()
