from enum import Enum

from Components.Instructions import *

class Conditions(Enum):
    SUNNY = 1
    RAINY = 2
    CLOUDY = 3

class Weather:
    def __init__(self, conditions, id):
        self.conditions = conditions
        self.id = id
        self.is_collidable = False
        self.weather_queue = WeatherQueue()

    def set_instructions(self, list):
        weather_list = []
        for i in list:
            if i.type == InstructionType.WEATHER:
                weather_list.append(i)
        self.weather_queue.set_instructions(weather_list)

    def on_update(self, step):
        if hasattr(self.weather_queue.get_instruction(self.conditions, step), "conditions"):
            self.conditions = self.weather_queue.get_instruction(self.conditions, step).conditions
        print(self.conditions.name)

    def on_display(self, surface):
        pass

    def on_change(self, step, conditions):
        pass

    def set_conditions(self, conditions):
        self.conditions = conditions
