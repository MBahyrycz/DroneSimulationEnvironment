from Layers.Layer import *

from Components.Weather import *

class Scenario:
    def __init__(self, name):
        self.name = name

    def execute(self, step, layers):

        for l in layers:
            if l.type == Type.WEATHER and step == 7:
                l.components[0].conditions = Conditions.RAINY
            if l.type == Type.DRONE and step == 3:
                for c in l.components:
                    c.set_destination(np.array([500, 500, 0]))


            
