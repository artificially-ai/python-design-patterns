import sys

from datetime import datetime

from patterns.singleton.pattern import SingletonType


class Logger(metaclass=SingletonType):

    def __init__(self):
        self.console = sys.stdout
        self.error = sys.stderr

    def info(self, message):
        time = datetime.now()
        self.console.writelines([f'[INFO] - {time} - Console ID {id(self.console)} - Logger ID {id(self)} - '
                                f'Message: {message}\n'])

    def warn(self, message):
        time = datetime.now()
        self.console.writelines([f'[WARN] - {time} - Console ID {id(self.console)} - Logger ID {id(self)} - '
                                f'Message: {message}\n'])

    def error(self, message):
        time = datetime.now()
        self.error.writelines([f'[ERROR] - {time} - Console ID {id(self.console)} - Logger ID {id(self)} -'
                                f'Message: {message}\n'])
