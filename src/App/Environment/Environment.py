
from App.Environment.Simulation import *

class Environment:
    def __init__(self, properties):
        self.properties = properties

    def create_simulation(self, name):
        return Simulation(name)

    def get_properties(self):
        print(self.properties)