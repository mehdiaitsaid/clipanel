import click
from . import services, files_explorer_app





@files_explorer_app.cli.command("make-folder")
@click.argument("name")
def make_folder(name):
    services.make_folder(name)
    return 'Ok'