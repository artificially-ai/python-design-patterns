from patterns.command.callback.handler import Callback


class AsyncCallbackHandler(Callback):

    def on_error(self, message):
        with(open('tests/error.txt', 'w')) as f:
            f.write(message)

    def on_success(self, message):
        with(open('tests/success.txt', 'w')) as f:
            f.write(message)
