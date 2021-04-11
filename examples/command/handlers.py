from patterns.command.callback.handler import Callback

from pathlib import Path


class AsyncCallbackHandler(Callback):

    def on_error(self, message):
        file_name = Path(__file__).parent / 'tests/error.txt'
        with(open(file_name, 'w')) as f:
            f.write(message)

    def on_success(self, message):
        file_name = Path(__file__).parent / 'tests/success.txt'
        with(open(file_name, 'w')) as f:
            f.write(message)
