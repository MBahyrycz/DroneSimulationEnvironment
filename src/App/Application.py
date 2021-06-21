from os import environ
import sys
import numpy as np

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox

from Components.Drone import *
from App.Environment.DroneLib import *
from Components.DockingStation import *
from Components.Weather import *
from Components.Map import *

from Layers.Layer import *


from App.Environment.Environment import *
from App.Environment.Scenario.Scenario import *

from App.GUI.main_window import *


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.environment = Environment({'name': 'Skulim environment'})
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.play.clicked.connect(self.on_run_button_clicked)
        self.dronelib = DroneLib()

        self.run()

    def run(self):
        self.window.show()

        sys.exit(self.app.exec_())

    def calculate(self):
        self.step_time = 1 / 10

        drone1 = Drone(np.array([130, 60, 0]), self.dronelib.get_props('default'), 0)
        drone2 = Drone(np.array([150, 400, 0]), self.dronelib.get_props('scout1'), 1)
        drone3 = Drone(np.array([500, 300, 0]), self.dronelib.get_props('carrier2'), 2)
        drone4 = Drone(np.array([650, 500, 0]), self.dronelib.get_props('mixed3'), 3)

        self.drone_layer = Layer(Type.DRONE, [drone1, drone2, drone3])
        self.drone_layer.add_component(drone4)

        map_props = {'width' : 1000, 'height' : 1000, 'name' : "Libertów", 'file_path': "terrain.png"}

        map = Map(map_props, 6)
        self.map_layer = Layer(Type.MAP, [map])

        weather = Weather(Conditions.SUNNY, 7)
        self.weather_layer = Layer(Type.WEATHER, [weather])

        self.weather_scenario = Scenario("Rain")

        self.simulation = self.environment.create_simulation('symulacja')
        self.simulation.add_layer(self.map_layer)
        self.simulation.add_layer(self.drone_layer)
        self.simulation.add_layer(self.weather_layer)
        self.simulation.add_scenario(self.weather_scenario)

    def reset_simulation(self, station_pos):
        self.step_time = 1 / 10

        drone1 = Drone(np.array([130, 60, 0]), self.dronelib.get_props('default'), 0)
        drone2 = Drone(np.array([150, 400, 0]), self.dronelib.get_props('scout1'), 1)
        drone3 = Drone(np.array([500, 300, 0]), self.dronelib.get_props('carrier2'), 2)
        drone4 = Drone(np.array([650, 500, 0]), self.dronelib.get_props('mixed3'), 3)

        self.drone_layer = Layer(Type.DRONE, [drone1, drone2, drone3])
        self.drone_layer.add_component(drone4)

        station_props = {'width': 50, 'height': 200, 'depth': 50, 'charge_power': 1, 'docking_places': 2}

        station1 = DockingStation(np.array([station_pos[0][0], station_pos[0][1], 10]), station_props, 4)
        station2 = DockingStation(np.array([station_pos[1][0], station_pos[1][1], 10]), station_props, 5)
        self.station_layer = Layer(Type.STATION, [station1, station2])

        map_props = {'width' : 1000, 'height' : 1000, 'name' : "Libertów", 'file_path': "terrain.png"}

        map = Map(map_props, 6)
        self.map_layer = Layer(Type.MAP, [map])

        weather = Weather(Conditions.SUNNY, 7)
        self.weather_layer = Layer(Type.WEATHER, [weather])

        self.weather_scenario = Scenario("Rain")

        self.simulation = self.environment.create_simulation('symulacja')
        self.simulation.add_layer(self.map_layer)
        self.simulation.add_layer(self.station_layer)
        self.simulation.add_layer(self.drone_layer)
        self.simulation.add_layer(self.weather_layer)
        self.simulation.add_scenario(self.weather_scenario)

    def sum_up_simulation(self):
        msg = QMessageBox()
        msg.setWindowTitle("Simulation info")
        msg.setText(self.simulation.sum_up())
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def on_run_button_clicked(self):
        self.calculate()
        self.simulation.run(self.step_time, 7, "Rain")
        station_pos = self.environment.position_station(2)
        self.simulation.shutdown()
        self.reset_simulation(station_pos)
        self.simulation.run(self.step_time, 10, "Rain")
        self.sum_up_simulation()
        self.simulation.shutdown()

