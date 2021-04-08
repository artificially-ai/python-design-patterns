from patterns.command.action import Action

from absl import logging


class SwitchOnAction(Action):

    def perform(self):
        logging.info('Switching on the machine.')
