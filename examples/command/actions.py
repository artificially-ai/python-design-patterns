from multiprocessing import Pool
from random import randrange

from absl import logging

from patterns.command.action import Action
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
            logging.info('The message will be sent in a different process.')

            # Silly way to simulate an issue before the call is dispatched to the callback.
            random_failure = randrange(0, 5)
            logging.info(f'Random failure state: {random_failure}')
            if random_failure:
                logging.info('Random failure has been triggered.')
                raise SystemError(f'Random failure has been triggered. Failure: {random_failure}')

            # Do something asynchronously.
            self.pool.apply(self.callback.on_success, [f'The message was sent successfully. '
                                                       f'Success code: {random_failure}'])

        except SystemError as e:
            # If something doesn't go okay, report an error.
            self.pool.apply(self.callback.on_error, [f'SystemError: {e}'])
