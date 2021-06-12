import sys
import numpy as np

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox

from Components.Drone import *
from Components.DockingStation import *
from Components.Weather import *
from Components.Map import *

from Layers.Layer import *

from App.GUI.MainWindow import MainWindow
from App.Environment.Environment import *
from App.Environment.Scenario import *

class Application:
    def __init__(self):
        self.app = app = QApplication(sys.argv)
        self.environment=Environment({'name':'Skulim environment'})
        self.window = QWidget()
        self.window.setWindowTitle('Drone simulation envinronment')
        self.window.setGeometry(100, 100, 800, 640)
        self.window.move(60, 15)
        
        self.label = QLabel(parent=self.window)
        self.label.setText('<h1>Press RUN to run simulation</h1>')
        self.label.move(60, 15)

        self.run_button = QPushButton(parent=self.window)
        self.run_button.setText("RUN")
        self.run_button.move(100, 100)
        self.run_button.clicked.connect(self.on_run_button_clicked)

        self.run()

    def run(self):
        self.window.show()

        sys.exit(self.app.exec_())


    def reset_simulation(self):
        self.step_time = 1/1

        drone1 = Drone(np.array([130,60,0]), 10, 0, file_path="drone0.png")
        drone2 = Drone(np.array([150,400,0]), 15, 1, file_path="drone1.png")
        drone3 = Drone(np.array([500,300,0]), 5, 2, file_path="drone2.png")
        drone4 = Drone(np.array([650,500,0]), 25, 3, file_path="drone0.png")
        self.drone_layer = Layer(Type.DRONE, [drone1, drone2, drone3]) 
        self.drone_layer.add_component(drone4)

        station1 = DockingStation(np.array([240, 60, 10]), 4)
        station2 = DockingStation(np.array([130, 200, 10]), 5)
        self.station_layer = Layer(Type.STATION, [station1, station2])

        map = Map(1000, 1000, "Libertow")
        self.map_layer = Layer(Type.MAP, [map])

        weather = Weather(Conditions.SUNNY)
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
        self.reset_simulation()
        self.simulation.run(self.step_time, 10)
        self.sum_up_simulation()
        self.simulation.shutdown()