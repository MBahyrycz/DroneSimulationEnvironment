from enum import Enum

class InstructionType(Enum):
    MOVE = 1
    ACTION = 2
    WEATHER = 3

class Instruction:
    def __init__(self):
        self.started = False
        self.in_progress = self.started and not self.ended
        self.ended = False

class MoveInstruction(Instruction):
    def __init__(self, type, position):
        super().__init__()
        self.position = position
        self.type = type

    def execute(self):
        self.started = True
        self.in_progress = self.started and not self.ended
        self.ended = False
        return self.position

class ChangeWeatherInstruction(Instruction):
    def __init__(self, type, conditions):
        super().__init__()
        self.conditions = conditions
        self.type = type

    def execute(self):
        self.started = True
        self.in_progress = self.started and not self.ended
        self.ended = False
        return self.conditions

