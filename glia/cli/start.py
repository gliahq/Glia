import argparse

from glia import app
from glia.cli import CommandFactory


class StartCommand(CommandFactory):
    def __init__(self, parser, *args, **kwargs):
        self.parser = parser.add_parser(*args, **kwargs)
        self.parser.set_defaults(action=self.run)

        # Set Logging Levels
        self.choices = [
            'spam', 'debug', 'verbose', 'info', 'notice', 'warning',
            'success', 'error', 'critical'
        ]
        self.parser.add_argument(
            '--log',
            choices=self.choices,
            type=str.lower,
            help="amount of info to log"
        )

    def run(self, *sys_args, **kwargs):
        passed_args = {
            'log_level': None
        }
        if sys_args[0].log:
            passed_args['log_level'] = sys_args[0].log

        app.start(**passed_args)
