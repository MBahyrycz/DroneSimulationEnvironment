from Layers.Layer import *

from Components.Weather import *

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
        

class Scenario:
    def __init__(self, name):
        self.name = name

    def execute(self, step, layers):

        for l in layers:
            if l.type == Type.WEATHER and step == 7:
                l.components[0].conditions = Conditions.RAINY
