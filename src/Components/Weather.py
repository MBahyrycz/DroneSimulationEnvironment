from enum import Enum

class Conditions(Enum):
    SUNNY = 1
    RAINY = 2
    CLOUDY = 3

class Weather:
    def __init__(self, conditions, id):
        self.conditions = conditions
        self.id = id
        self.is_collidable = False

    def on_update(self, step):
        print(self.conditions.name)

    def on_display(self, surface):
        pass

    def on_change(self, step, conditions):
        pass

    def set_conditions(self, conditions):
        self.conditions = conditions
