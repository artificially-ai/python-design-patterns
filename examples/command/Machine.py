from examples.command.actions import SwitchOnAction
from examples.command.commands import SwitchOnCommand
from patterns.command.pattern import Command

from absl import app


class Machine:

    def __init__(self):
        self.switch_on: Command = SwitchOnCommand(SwitchOnAction())

    def on(self):
        self.switch_on.execute()


def main(argv):
    machine = Machine()
    machine.on()


if __name__ == '__main__':
    app.run(main)
