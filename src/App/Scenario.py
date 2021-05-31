from Layers.Layer import *

from Components.Weather import *

class Scenario:
    def __init__(self, name):
        self.name = name

    def execute(self, step, layers):

        for l in layers:
            if l.type == Type.WEATHER and step == 7:
                l.components[0].conditions = Conditions.RAINY
