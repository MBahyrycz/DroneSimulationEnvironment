from enum import Enum
import queue

class InstructionType(Enum):
    MOVE = 1
    ACTION = 2
    WEATHER = 3

class MoveQueue:
    def __init__(self):
        self.bufor = []
        self.queue = queue.Queue(10)

    def set_instructions(self, list):
        for i in list:
            self.queue.put(i)

    def get_instruction(self, position, step):
        if not self.bufor:
            if self.queue.empty():
                self.bufor.append(MoveInstruction(position, type))
            else:
                self.bufor.append(self.queue.get())
        if self.bufor[0].ready(position, step):
            if self.queue.empty():
                self.bufor[0] = MoveInstruction(position, type)
            else:
                self.bufor[0] = self.queue.get()

        return self.bufor[0]

class MoveInstruction():
    def __init__(self, position, type):
        self.position = position
        self.type = type

    def ready(self, position, step):
        return self.position[0] == position[0] and self.position[1] == position[1] and self.position[2] == position[2]

class MoveWaitAtInstruction():
    def __init__(self, step, type):
        self.step = step
        self.type = type

    def ready(self, position, step):
        return self.step == step

class WeatherQueue:
    def __init__(self):
        self.bufor = []
        self.queue = queue.Queue(10)

    def set_instructions(self, list):
        for i in list:
            self.queue.put(i)

    def get_instruction(self, conditions, step):
        if not self.bufor:
            if self.queue.empty():
                self.bufor.append(WeatherChangeInstruction(conditions, type))
            else:
                self.bufor.append(self.queue.get())
        if self.bufor[0].ready(conditions, step):
            if self.queue.empty():
                self.bufor[0] = WeatherChangeInstruction(conditions, type)
            else:
                self.bufor[0] = self.queue.get()

        return self.bufor[0]

class WeatherChangeInstruction():
    def __init__(self, conditions, type):
        self.conditions = conditions
        self.type = type

    def ready(self, conditions, step):
        return self.conditions == conditions

class WeatherWaitAtInstruction():
    def __init__(self, step, type):
        self.step = step
        self.type = type

    def ready(self, conditions, step):
        return self.step == step

