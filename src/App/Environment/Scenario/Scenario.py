from Layers.Layer import *

from Components.Weather import *

from App.Environment.Scenario.Instructions import *

class Scenario:
    def __init__(self, name):
        self.name = name
        inst1 = MoveInstruction(InstructionType.MOVE, np.array([0,0,0]))
        inst2 = MoveInstruction(InstructionType.MOVE, np.array([500,0,0]))
        inst3 = MoveInstruction(InstructionType.WEATHER, Conditions.RAINY)
        self.tasks = {0:[inst1], 1:[inst2], 7:[inst3]}

    def execute(self, step, layers, manager):

        for t in self.tasks:
            if self.tasks[t][0].type == InstructionType.MOVE:
                manager.get_object_by_id(t).set_destination(self.tasks[t][0].execute())
            if self.tasks[t][0].type == InstructionType.WEATHER and step == 7:
                manager.get_object_by_id(t).set_conditions(self.tasks[t][0].execute())



            
