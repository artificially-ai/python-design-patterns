from patterns.command.action import Action

from multiprocessing import Pool

from absl import logging

from patterns.command.callback.handler import Callback


class SwitchOnAction(Action):

    def perform(self):
        logging.info('Switching on the machine.')


class SwitchOffAction(Action):

    def perform(self):
        logging.info('Switching off the machine.')


class SendMessageAction(Action):

    def __init__(self, callback: Callback):
        self.callback = callback
        self.pool: Pool = Pool(1)

    def perform(self):
        try:
            logging.info('Will send the message in a different process.')
            # Do something asynchronously.
            self.pool.apply(self.callback.on_success, ['Message sent successfully.'])

        except:
            # If something doesn't go okay, report an error.
            self.pool.apply(self.callback.on_error, ['Error occurred when sending the message.'])
