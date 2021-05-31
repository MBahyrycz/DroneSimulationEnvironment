from enum import Enum

class Conditions(Enum):
    SUNNY = 1
    RAINY = 2
    CLOUDY = 3


class Weather:
    def __init__(self, conditions):
        self.conditions = conditions

    def on_update(self, step):
        # if self.conditions.name == "SUNNY":
        print(self.conditions.name)