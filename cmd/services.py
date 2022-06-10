import subprocess
import os
from .models import db


def single_line_command(cmd):
    return os.system(cmd)

def args_command(cmd):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE)


