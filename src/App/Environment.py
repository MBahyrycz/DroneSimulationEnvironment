
from App.Simulation import *

class Environment:
    def __init__(self, properties):
        self.properties = properties
        pass

    def create_simulation(self, name):
        return Simulation(name)

    def get_properties(self):
        print(self.properties)