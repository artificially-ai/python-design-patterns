from examples.command.actions import SwitchOnAction, SendMessageAction, SwitchOffAction
from examples.command.commands import SwitchOnCommand, SendMessageCommand, SwitchOffCommand
from examples.command.handlers import AsyncCallbackHandler
from patterns.command.pattern import Command

from absl import app


class Machine:

    def __init__(self):
        self.switch_on: Command = SwitchOnCommand(SwitchOnAction())
        self.switch_off: Command = SwitchOffCommand(SwitchOffAction())
        self.send_message: Command = SendMessageCommand(SendMessageAction(AsyncCallbackHandler()))

    def on(self):
        self.switch_on.execute()

    def off(self):
        self.switch_off.execute()

    def send(self):
        self.send_message.execute()


def main(arguments):
    machine = Machine()
    machine.on()
    machine.send()
    machine.off()


if __name__ == '__main__':
    app.run(main)
