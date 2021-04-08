from patterns.command.action import Action
from patterns.command.pattern import Command


class SwitchOnCommand(Command):

    def __init__(self, action: Action):
        self.action = action

    def execute(self):
        self.action.perform()
