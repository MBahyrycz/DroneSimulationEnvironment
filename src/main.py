import numpy as np

from Components.Drone import *
from Components.DockingStation import *
from Components.Weather import *
from Components.Map import *

from Layers.Layer import *

from App.Environment import *
from App.Scenario import *

if __name__ == "__main__":

    step = 1/1

    properties = {'name':'Skulim environment'} 
    env=Environment(properties)

    drone1 = Drone(np.array([1,0,0]), 1, 0)
    drone2 = Drone(np.array([0,0,0]), 1, 1)
    drone3 = Drone(np.array([-1,0,0]), 1, 2)
    drone4 = Drone(np.array([-2,0,0]), 1, 3)
    drone_layer = Layer(Type.DRONE, [drone1, drone2, drone3]) 
    drone_layer.add_component(drone4)

    station1 = DockingStation(np.array([11, 13, 10]), 0)
    station2 = DockingStation(np.array([-7, 31, 10]), 1)
    station_layer = Layer(Type.STATION, [station1, station2])

    map = Map(100, 100, "Libertow")
    map_layer = Layer(Type.MAP, [map])

    weather = Weather(Conditions.SUNNY)
    weather_layer = Layer(Type.WEATHER, [weather])

    weather_scenario = Scenario("Rain")

    simulation = env.create_simulation('symulacja')
    simulation.add_layer(drone_layer)
    simulation.add_layer(station_layer)
    simulation.add_layer(weather_layer)
    simulation.add_layer(map_layer)
    simulation.add_scenario(weather_scenario)
    simulation.run(step, 10, "Rain")
