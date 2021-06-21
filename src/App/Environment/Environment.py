
from enum import unique
from numpy.core.fromnumeric import trace
from App.Environment.Simulation import *
from App.Environment.ObjectManager import *
from App.Environment.GeneticAlgorythm.GeneticAlgorythm import *

class Environment:
    def __init__(self, properties):
        self.properties = properties

    def create_simulation(self, name):
        return Simulation(name)

    def position_station(self, station_count):
        print("CALCULATING... \n Do nothin for a while!")
        trace = []
        unique_trace = []
        for t in ObjectManager.get_object_traces().items():
            trace += t[1]

        GeneticAlgorythm.init(station_count, trace)
        result = GeneticAlgorythm.solve()

        print(result.chromosome)
        return result.chromosome

    def get_properties(self):
        print(self.properties)