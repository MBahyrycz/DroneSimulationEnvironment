from enum import Enum

class InstructionType(Enum):
    MOVE = 1
    ACTION = 2

class Instruction:
    def __init__(self, type):
        self.started = False
        self.in_progress = self.started and not self.ended
        self.ended = False

        self.type = type