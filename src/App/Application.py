import PySimpleGUI as sg
import numpy as np

from Components.Drone import *
from Components.DockingStation import *
from Components.Weather import *
from Components.Map import *

from Layers.Layer import *

from App.Environment.Environment import *
from App.Environment.Scenario import *

class Application:
    def __init__(self):
        layout = [[sg.Text("Press RUN button to run simulation")], [sg.Button("RUN")]]
        self.window = sg.Window("Drone Environment", layout, size=(800, 640))
        self.is_running = True
        self.environment=Environment({'name':'Skulim environment'})

    def create_simulation(self):
        self.step_time = 1/1

        drone1 = Drone(np.array([100,40,0]), 10, 0, file_path="drone0.png")
        drone2 = Drone(np.array([150,400,0]), 15, 1, file_path="drone1.png")
        drone3 = Drone(np.array([500,300,0]), 5, 2, file_path="drone2.png")
        drone4 = Drone(np.array([650,500,0]), 25, 3, file_path="drone0.png")
        self.drone_layer = Layer(Type.DRONE, [drone1, drone2, drone3]) 
        self.drone_layer.add_component(drone4)

        station1 = DockingStation(np.array([11, 13, 10]), 0)
        station2 = DockingStation(np.array([-7, 31, 10]), 1)
        self.station_layer = Layer(Type.STATION, [station1, station2])

        map = Map(1000, 1000, "Libertow")
        self.map_layer = Layer(Type.MAP, [map])

        weather = Weather(Conditions.SUNNY)
        self.weather_layer = Layer(Type.WEATHER, [weather])

        self.weather_scenario = Scenario("Rain")

        self.simulation = self.environment.create_simulation('symulacja')
        self.simulation.add_layer(self.map_layer)
        self.simulation.add_layer(self.drone_layer)
        self.simulation.add_layer(self.station_layer)
        self.simulation.add_layer(self.weather_layer)
        self.simulation.add_scenario(self.weather_scenario)


    def main_loop(self):
        while self.is_running:
            event, values = self.window.read()
            # end program
            if event == sg.WIN_CLOSED:
                self.is_running = False
            # run simulation
            elif event == "RUN":
                self.create_simulation()
                self.simulation.run(self.step_time, 10, "Rain")

        self.window.close()