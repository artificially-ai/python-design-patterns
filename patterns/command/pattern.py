from patterns.command.action import Action


class Command:

    def __init__(self, action: Action):
        self.action = action

    def execute(self) -> None:
        pass
