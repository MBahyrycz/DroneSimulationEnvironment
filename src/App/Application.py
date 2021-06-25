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
from App.GUI.add_drone import *
from App.GUI.add_station import *


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.environment = Environment({'name': 'Skulim environment'})
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.step_time = 1/10
        self.station_props = []
        self.num_station = 3 #self.ui.number_of_stations.value()
        self.dronelib = DroneLib()
        self.objectmanager = ObjectManager()
        self.drone_layer = Layer(Type.DRONE, [])
        self.station_layer = Layer(Type.STATION, [])
        self.map_layer = Layer(Type.MAP, [])
        self.weather_layer = Layer(Type.WEATHER, [])

        self.ui.play.clicked.connect(self.on_run_button_clicked)
        self.ui.add_drone.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_drone_widget))
        self.ui.add_station.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_station_widget))
        self.ui.add_weather.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_weather_widget))
        self.ui.add_map.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.add_map_widget))
        self.ui.edit_scenario.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.edit_scenario_widget))

        self.ui.cancel.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.cancel_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.go_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.go_back_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.go_back_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.go_back_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))

        self.ui.add.clicked.connect(self.create_drone)
        self.ui.add_station_2.clicked.connect(self.create_station)

        self.run()

    def run(self):
        self.window.show()

        sys.exit(self.app.exec_())

    def calculate(self):     
        self.simulation = self.environment.create_simulation('symulacja') 
        map_props = {'width' : 1000, 'height' : 1000, 'name' : "Libertów", 'file_path': "terrain.png"}

        map = Map(map_props, 4)
        self.map_layer = Layer(Type.MAP, [map])

        weather = Weather(Conditions.SUNNY, 1)
        self.weather_layer = Layer(Type.WEATHER, [weather])

        self.weather_scenario = Scenario("Rain")

        self.simulation.add_layer(self.map_layer)
        self.simulation.add_layer(self.drone_layer)
        self.simulation.add_layer(self.weather_layer)
        self.simulation.add_scenario(self.weather_scenario)

    def reset_simulation(self, station_pos):
        self.simulation = self.environment.create_simulation('symulacja')
        print(self.num_station)
        print(self.station_props)
        for i in range(0, self.num_station):
            station = DockingStation(np.array([station_pos[i][0], station_pos[i][1], 10]),
                                     self.station_props[i], i+2)
            self.station_layer.add_component(station)
        map_props = {'width' : 1000, 'height' : 1000, 'name' : "Libertów", 'file_path': "terrain.png"}

        map = Map(map_props, 4)
        self.map_layer = Layer(Type.MAP, [map])

        weather = Weather(Conditions.SUNNY, 1)
        
        self.weather_layer = Layer(Type.WEATHER, [weather])
        self.weather_scenario = Scenario("Rain")
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
        del self.drone_layer
        del self.station_layer
        del self.map_layer
        del self.weather_layer
        msg.exec_()

    def on_run_button_clicked(self):
        self.calculate()
        self.simulation.run(self.step_time, 10, "Rain")
        station_pos = self.environment.position_station(self.num_station)
        self.simulation.shutdown()
        self.reset_simulation(station_pos)
        self.simulation.run(self.step_time, 10, "Rain")
        self.sum_up_simulation()
        self.simulation.shutdown()

    def create_drone(self):
        x = self.ui.x_pos.value()
        y = self.ui.y_pos.value()
        z = self.ui.z_pos.value()
        #print(self.objectmanager.get_id())
        props = self.ui.drone_select_type.currentItem()
        drone = Drone(np.array([x, y, z]), self.dronelib.get_props(props.text().lower()), 0)
        self.drone_layer.add_component(drone)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.x_pos.setValue(0)
        self.ui.y_pos.setValue(0)
        self.ui.z_pos.setValue(0)

    def create_station(self):
        power = self.ui.charge_power.currentItem()
        places = self.ui.docking_places.currentItem()
        paths = ["station1.png", "station2.png"]
        props = {'width': 50, 'height': 200, 'depth': 50, 'charge_power': int(power.text()),
                 'docking_places': int(places.text()), 'file_path': paths[random.randint(0, 1)]}
        self.station_props.append(props)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        # station = DockingStation(np.array([x, y, z]), props, self.objectmanager.get_id())
        # self.station_layer.add_component(station)
        #
        # self.ui.x_pos.setValue(0)
        # self.ui.y_pos.setValue(0)
        # self.ui.z_pos.setValue(0)

    # def create_map(self):
    #     if self.ui.checkBox.isChecked():
    #         terrain = Map(1000, 1000, "Libertow")
    #         self.map_layer.add_component(terrain)
        # else:
        #     msg = QMessageBox()
        #     msg.setWindowTitle("Simulation info")
        #     msg.setText("No map chosen")
        #     msg.setIcon(QMessageBox.Information)
        #     msg.exec_()

