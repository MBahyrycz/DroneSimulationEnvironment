from Layers.Layer import *

from Components.Weather import *
from Components.Instructions import *

class Scenario:
    def __init__(self, name):
        self.name = name
        inst1 = MoveInstruction(np.array([4,2,0]), InstructionType.MOVE)
        inst2 = MoveInstruction(np.array([500,0,0]), InstructionType.MOVE)
        inst3 = WeatherChangeInstruction(Conditions.RAINY,InstructionType.WEATHER)
        inst4 = WeatherChangeInstruction(Conditions.SUNNY,InstructionType.WEATHER)
        inst5 = WeatherWaitAtInstruction(5, InstructionType.WEATHER)
        inst6 = WeatherWaitAtInstruction(25, InstructionType.WEATHER)
        inst7 = MoveWaitAtInstruction(30, InstructionType.MOVE)
        self.tasks = {0:[inst1, inst7, inst2], 1:[inst2], 2:[inst1], 7:[inst5, inst3, inst6, inst4]}

    def execute(self, manager):
        for l in self.tasks:
            manager.get_object_by_id(l).set_instructions(self.tasks[l])
        



            
