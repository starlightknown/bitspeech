from flask.cli import AppGroup

cli_app_group = AppGroup("cli")

from bitspeech.cli import commands
