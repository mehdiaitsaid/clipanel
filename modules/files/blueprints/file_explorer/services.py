
from cmd import services as cmd

def make_folder(name):
    # setup()
    cmd.args_command(['mkdir', name])
    return 'Ok'