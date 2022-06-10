import subprocess
import os
import uuid
from datetime import datetime

from .models import db, Cmd


def single_line_command(cmd):
    return os.system(cmd)


def args_command(cmd):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE)


def add_command(key, cmd, args, distribution):
    new_cmd = Cmd(id=str(uuid.uuid4()),
                   key=key,
                   cmd=cmd,
                   args=args,
                   distribution=distribution,
                   created_at=datetime.now(),
                   updated_at=datetime.now())

    db.session.add(new_cmd)
    db.session.commit()
    return new_cmd

def get_command_by_key(key):
    return Cmd.query.filter_by(key=key).first()

def get_command_by_id(id):
    return Cmd.query.filter_by(id=id).first()

def delete_command_by_key(key):
    Cmd.query.filter_by(key=key).delete()
    db.session.commit()

def delete_command_by_id(id):
    Cmd.query.filter_by(id=id).delete()
    db.session.commit()
