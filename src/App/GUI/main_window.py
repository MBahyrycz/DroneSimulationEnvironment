# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 625)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sep_col = QtWidgets.QFrame(self.centralwidget)
        self.sep_col.setGeometry(QtCore.QRect(490, 10, 20, 551))
        self.sep_col.setFrameShape(QtWidgets.QFrame.VLine)
        self.sep_col.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sep_col.setObjectName("sep_col")
        self.layer_manager = QtWidgets.QLabel(self.centralwidget)
        self.layer_manager.setGeometry(QtCore.QRect(530, 410, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.layer_manager.setFont(font)
        self.layer_manager.setObjectName("layer_manager")
        self.drone_visible = QtWidgets.QCheckBox(self.centralwidget)
        self.drone_visible.setGeometry(QtCore.QRect(620, 470, 70, 17))
        self.drone_visible.setObjectName("drone_visible")
        self.station_visible = QtWidgets.QCheckBox(self.centralwidget)
        self.station_visible.setGeometry(QtCore.QRect(620, 490, 70, 17))
        self.station_visible.setObjectName("station_visible")
        self.map_visible = QtWidgets.QCheckBox(self.centralwidget)
        self.map_visible.setGeometry(QtCore.QRect(620, 510, 70, 17))
        self.map_visible.setObjectName("map_visible")
        self.weather_visible = QtWidgets.QCheckBox(self.centralwidget)
        self.weather_visible.setGeometry(QtCore.QRect(620, 530, 70, 17))
        self.weather_visible.setObjectName("weather_visible")
        self.drone_computable = QtWidgets.QCheckBox(self.centralwidget)
        self.drone_computable.setGeometry(QtCore.QRect(690, 470, 91, 17))
        self.drone_computable.setObjectName("drone_computable")
        self.weather_computable = QtWidgets.QCheckBox(self.centralwidget)
        self.weather_computable.setGeometry(QtCore.QRect(690, 530, 81, 17))
        self.weather_computable.setObjectName("weather_computable")
        self.map_computable = QtWidgets.QCheckBox(self.centralwidget)
        self.map_computable.setGeometry(QtCore.QRect(690, 510, 81, 17))
        self.map_computable.setObjectName("map_computable")
        self.station_computable = QtWidgets.QCheckBox(self.centralwidget)
        self.station_computable.setGeometry(QtCore.QRect(690, 490, 81, 17))
        self.station_computable.setObjectName("station_computable")
        self.label_drone = QtWidgets.QLabel(self.centralwidget)
        self.label_drone.setGeometry(QtCore.QRect(530, 470, 81, 20))
        self.label_drone.setObjectName("label_drone")
        self.label_station = QtWidgets.QLabel(self.centralwidget)
        self.label_station.setGeometry(QtCore.QRect(530, 490, 71, 16))
        self.label_station.setObjectName("label_station")
        self.label_map = QtWidgets.QLabel(self.centralwidget)
        self.label_map.setGeometry(QtCore.QRect(530, 510, 61, 16))
        self.label_map.setObjectName("label_map")
        self.label_weather = QtWidgets.QLabel(self.centralwidget)
        self.label_weather.setGeometry(QtCore.QRect(530, 530, 81, 16))
        self.label_weather.setObjectName("label_weather")
        self.sep_row = QtWidgets.QFrame(self.centralwidget)
        self.sep_row.setGeometry(QtCore.QRect(530, 400, 241, 16))
        self.sep_row.setFrameShape(QtWidgets.QFrame.HLine)
        self.sep_row.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sep_row.setObjectName("sep_row")
        self.scenario_manager = QtWidgets.QLabel(self.centralwidget)
        self.scenario_manager.setGeometry(QtCore.QRect(530, 280, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.scenario_manager.setFont(font)
        self.scenario_manager.setObjectName("scenario_manager")
        self.sep_row_2 = QtWidgets.QFrame(self.centralwidget)
        self.sep_row_2.setGeometry(QtCore.QRect(530, 270, 241, 16))
        self.sep_row_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.sep_row_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sep_row_2.setObjectName("sep_row_2")
        self.edit_scenario = QtWidgets.QPushButton(self.centralwidget)
        self.edit_scenario.setGeometry(QtCore.QRect(590, 340, 101, 51))
        self.edit_scenario.setObjectName("edit_scenario")
        self.prepare_simulation = QtWidgets.QLabel(self.centralwidget)
        self.prepare_simulation.setGeometry(QtCore.QRect(530, 20, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prepare_simulation.setFont(font)
        self.prepare_simulation.setObjectName("prepare_simulation")
        self.simulation_window = QtWidgets.QLabel(self.centralwidget)
        self.simulation_window.setGeometry(QtCore.QRect(120, 20, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.simulation_window.setFont(font)
        self.simulation_window.setObjectName("simulation_window")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(110, 470, 75, 23))
        self.play.setObjectName("play")
        self.pause = QtWidgets.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(190, 470, 75, 23))
        self.pause.setObjectName("pause")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(270, 470, 75, 23))
        self.stop.setObjectName("stop")
        self.add_drone = QtWidgets.QPushButton(self.centralwidget)
        self.add_drone.setGeometry(QtCore.QRect(580, 70, 131, 41))
        self.add_drone.setObjectName("add_drone")
        self.add_station = QtWidgets.QPushButton(self.centralwidget)
        self.add_station.setGeometry(QtCore.QRect(580, 120, 131, 41))
        self.add_station.setObjectName("add_station")
        self.add_map = QtWidgets.QPushButton(self.centralwidget)
        self.add_map.setGeometry(QtCore.QRect(580, 170, 131, 41))
        self.add_map.setObjectName("add_map")
        self.add_weather = QtWidgets.QPushButton(self.centralwidget)
        self.add_weather.setGeometry(QtCore.QRect(580, 220, 131, 41))
        self.add_weather.setObjectName("add_weather")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(50, 100, 381, 341))
        self.stackedWidget.setObjectName("stackedWidget")
        self.add_drone_widget = QtWidgets.QWidget()
        self.add_drone_widget.setObjectName("add_drone_widget")
        self.label = QtWidgets.QLabel(self.add_drone_widget)
        self.label.setGeometry(QtCore.QRect(120, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.delete_2 = QtWidgets.QPushButton(self.add_drone_widget)
        self.delete_2.setGeometry(QtCore.QRect(150, 310, 75, 23))
        self.delete_2.setObjectName("delete_2")
        self.add = QtWidgets.QPushButton(self.add_drone_widget)
        self.add.setGeometry(QtCore.QRect(70, 310, 75, 23))
        self.add.setObjectName("add")
        self.z_pos = QtWidgets.QSlider(self.add_drone_widget)
        self.z_pos.setGeometry(QtCore.QRect(100, 170, 160, 22))
        self.z_pos.setMaximum(1000)
        self.z_pos.setOrientation(QtCore.Qt.Horizontal)
        self.z_pos.setObjectName("z_pos")
        self.label_5 = QtWidgets.QLabel(self.add_drone_widget)
        self.label_5.setGeometry(QtCore.QRect(60, 200, 101, 16))
        self.label_5.setObjectName("label_5")
        self.drone_select_type = QtWidgets.QListWidget(self.add_drone_widget)
        self.drone_select_type.setGeometry(QtCore.QRect(60, 220, 256, 71))
        self.drone_select_type.setObjectName("drone_select_type")
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.drone_select_type.addItem(item)
        self.label_3 = QtWidgets.QLabel(self.add_drone_widget)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 47, 13))
        self.label_3.setObjectName("label_3")
        self.x_pos = QtWidgets.QSlider(self.add_drone_widget)
        self.x_pos.setGeometry(QtCore.QRect(100, 110, 160, 22))
        self.x_pos.setMaximum(1000)
        self.x_pos.setOrientation(QtCore.Qt.Horizontal)
        self.x_pos.setObjectName("x_pos")
        self.y_pos = QtWidgets.QSlider(self.add_drone_widget)
        self.y_pos.setGeometry(QtCore.QRect(100, 140, 160, 22))
        self.y_pos.setMaximum(1000)
        self.y_pos.setOrientation(QtCore.Qt.Horizontal)
        self.y_pos.setObjectName("y_pos")
        self.label_2 = QtWidgets.QLabel(self.add_drone_widget)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.add_drone_widget)
        self.label_4.setGeometry(QtCore.QRect(80, 170, 47, 13))
        self.label_4.setObjectName("label_4")
        self.cancel = QtWidgets.QPushButton(self.add_drone_widget)
        self.cancel.setGeometry(QtCore.QRect(230, 310, 75, 23))
        self.cancel.setObjectName("cancel")
        self.label_7 = QtWidgets.QLabel(self.add_drone_widget)
        self.label_7.setGeometry(QtCore.QRect(80, 90, 141, 16))
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.add_drone_widget)
        self.add_station_widget = QtWidgets.QWidget()
        self.add_station_widget.setObjectName("add_station_widget")
        self.y_pos_st = QtWidgets.QSlider(self.add_station_widget)
        self.y_pos_st.setGeometry(QtCore.QRect(120, 110, 160, 22))
        self.y_pos_st.setMaximum(1000)
        self.y_pos_st.setOrientation(QtCore.Qt.Horizontal)
        self.y_pos_st.setObjectName("y_pos_st")
        self.delete_station = QtWidgets.QPushButton(self.add_station_widget)
        self.delete_station.setGeometry(QtCore.QRect(150, 300, 75, 23))
        self.delete_station.setObjectName("delete_station")
        self.charge_power = QtWidgets.QListWidget(self.add_station_widget)
        self.charge_power.setGeometry(QtCore.QRect(230, 200, 41, 71))
        self.charge_power.setObjectName("charge_power")
        item = QtWidgets.QListWidgetItem()
        self.charge_power.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.charge_power.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.charge_power.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.charge_power.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.charge_power.addItem(item)
        self.label_6 = QtWidgets.QLabel(self.add_station_widget)
        self.label_6.setGeometry(QtCore.QRect(70, 170, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.add_station_widget)
        self.label_12.setGeometry(QtCore.QRect(80, 80, 47, 13))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.add_station_widget)
        self.label_13.setGeometry(QtCore.QRect(80, 140, 47, 13))
        self.label_13.setObjectName("label_13")
        self.add_station_2 = QtWidgets.QPushButton(self.add_station_widget)
        self.add_station_2.setGeometry(QtCore.QRect(70, 300, 75, 23))
        self.add_station_2.setObjectName("add_station_2")
        self.z_pos_st = QtWidgets.QSlider(self.add_station_widget)
        self.z_pos_st.setGeometry(QtCore.QRect(120, 140, 160, 22))
        self.z_pos_st.setMaximum(1000)
        self.z_pos_st.setOrientation(QtCore.Qt.Horizontal)
        self.z_pos_st.setObjectName("z_pos_st")
        self.label_9 = QtWidgets.QLabel(self.add_station_widget)
        self.label_9.setGeometry(QtCore.QRect(200, 170, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.add_station_widget)
        self.label_10.setGeometry(QtCore.QRect(80, 110, 47, 13))
        self.label_10.setObjectName("label_10")
        self.cancel_2 = QtWidgets.QPushButton(self.add_station_widget)
        self.cancel_2.setGeometry(QtCore.QRect(230, 300, 75, 23))
        self.cancel_2.setObjectName("cancel_2")
        self.docking_places = QtWidgets.QListWidget(self.add_station_widget)
        self.docking_places.setGeometry(QtCore.QRect(100, 200, 41, 71))
        self.docking_places.setObjectName("docking_places")
        item = QtWidgets.QListWidgetItem()
        self.docking_places.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.docking_places.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.docking_places.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.docking_places.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.docking_places.addItem(item)
        self.label_11 = QtWidgets.QLabel(self.add_station_widget)
        self.label_11.setGeometry(QtCore.QRect(80, 60, 141, 16))
        self.label_11.setObjectName("label_11")
        self.x_pos_st = QtWidgets.QSlider(self.add_station_widget)
        self.x_pos_st.setGeometry(QtCore.QRect(120, 80, 160, 22))
        self.x_pos_st.setMaximum(1000)
        self.x_pos_st.setOrientation(QtCore.Qt.Horizontal)
        self.x_pos_st.setObjectName("x_pos_st")
        self.label_8 = QtWidgets.QLabel(self.add_station_widget)
        self.label_8.setGeometry(QtCore.QRect(130, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.add_station_widget)
        self.add_map_widget = QtWidgets.QWidget()
        self.add_map_widget.setObjectName("add_map_widget")
        self.label_15 = QtWidgets.QLabel(self.add_map_widget)
        self.label_15.setGeometry(QtCore.QRect(120, 30, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.checkBox = QtWidgets.QCheckBox(self.add_map_widget)
        self.checkBox.setGeometry(QtCore.QRect(130, 90, 91, 17))
        self.checkBox.setObjectName("checkBox")
        self.go_back = QtWidgets.QPushButton(self.add_map_widget)
        self.go_back.setGeometry(QtCore.QRect(130, 170, 75, 23))
        self.go_back.setObjectName("go_back")
        self.stackedWidget.addWidget(self.add_map_widget)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.edit_scenario_widget = QtWidgets.QWidget()
        self.edit_scenario_widget.setObjectName("edit_scenario_widget")
        self.go_back_3 = QtWidgets.QPushButton(self.edit_scenario_widget)
        self.go_back_3.setGeometry(QtCore.QRect(140, 170, 75, 23))
        self.go_back_3.setObjectName("go_back_3")
        self.label_16 = QtWidgets.QLabel(self.edit_scenario_widget)
        self.label_16.setGeometry(QtCore.QRect(140, 130, 101, 20))
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.edit_scenario_widget)
        self.add_weather_widget = QtWidgets.QWidget()
        self.add_weather_widget.setObjectName("add_weather_widget")
        self.go_back_2 = QtWidgets.QPushButton(self.add_weather_widget)
        self.go_back_2.setGeometry(QtCore.QRect(140, 130, 75, 23))
        self.go_back_2.setObjectName("go_back_2")
        self.label_14 = QtWidgets.QLabel(self.add_weather_widget)
        self.label_14.setGeometry(QtCore.QRect(140, 90, 101, 20))
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.add_weather_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSimulation = QtWidgets.QAction(MainWindow)
        self.actionSimulation.setObjectName("actionSimulation")
        self.menuNew.addAction(self.actionSimulation)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.layer_manager.setText(_translate("MainWindow", "Layer Manager"))
        self.drone_visible.setText(_translate("MainWindow", "Visible"))
        self.station_visible.setText(_translate("MainWindow", "Visible"))
        self.map_visible.setText(_translate("MainWindow", "Visible"))
        self.weather_visible.setText(_translate("MainWindow", "Visible"))
        self.drone_computable.setText(_translate("MainWindow", "Computable"))
        self.weather_computable.setText(_translate("MainWindow", "Computable"))
        self.map_computable.setText(_translate("MainWindow", "Computable"))
        self.station_computable.setText(_translate("MainWindow", "Computable"))
        self.label_drone.setText(_translate("MainWindow", "Drone Layer"))
        self.label_station.setText(_translate("MainWindow", "Station Layer"))
        self.label_map.setText(_translate("MainWindow", "Map Layer"))
        self.label_weather.setText(_translate("MainWindow", "Weather Layer"))
        self.scenario_manager.setText(_translate("MainWindow", "Scenario Manager"))
        self.edit_scenario.setText(_translate("MainWindow", "EDIT"))
        self.prepare_simulation.setText(_translate("MainWindow", "Prepare Simulation"))
        self.simulation_window.setText(_translate("MainWindow", "Simulation Window"))
        self.play.setText(_translate("MainWindow", "PLAY"))
        self.pause.setText(_translate("MainWindow", "PAUSE"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.add_drone.setText(_translate("MainWindow", "ADD DRONE"))
        self.add_station.setText(_translate("MainWindow", "ADD STATION"))
        self.add_map.setText(_translate("MainWindow", "ADD MAP"))
        self.add_weather.setText(_translate("MainWindow", "ADD WEATHER"))
        self.label.setText(_translate("MainWindow", "Adding drone"))
        self.delete_2.setText(_translate("MainWindow", "Delete"))
        self.add.setText(_translate("MainWindow", "Add"))
        self.label_5.setText(_translate("MainWindow", "Select drone type:"))
        __sortingEnabled = self.drone_select_type.isSortingEnabled()
        self.drone_select_type.setSortingEnabled(False)
        item = self.drone_select_type.item(0)
        item.setText(_translate("MainWindow", "Default"))
        item = self.drone_select_type.item(1)
        item.setText(_translate("MainWindow", "Scout1"))
        item = self.drone_select_type.item(2)
        item.setText(_translate("MainWindow", "Scout2"))
        item = self.drone_select_type.item(3)
        item.setText(_translate("MainWindow", "Scout3"))
        item = self.drone_select_type.item(4)
        item.setText(_translate("MainWindow", "Carrier1"))
        item = self.drone_select_type.item(5)
        item.setText(_translate("MainWindow", "Carrier2"))
        item = self.drone_select_type.item(6)
        item.setText(_translate("MainWindow", "Carrier3"))
        item = self.drone_select_type.item(7)
        item.setText(_translate("MainWindow", "Mixed1"))
        item = self.drone_select_type.item(8)
        item.setText(_translate("MainWindow", "Mixed2"))
        item = self.drone_select_type.item(9)
        item.setText(_translate("MainWindow", "Mixed3"))
        self.drone_select_type.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "Y:"))
        self.label_2.setText(_translate("MainWindow", "X:"))
        self.label_4.setText(_translate("MainWindow", "Z:"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.label_7.setText(_translate("MainWindow", "Insert start position:"))
        self.delete_station.setText(_translate("MainWindow", "Delete"))
        __sortingEnabled = self.charge_power.isSortingEnabled()
        self.charge_power.setSortingEnabled(False)
        item = self.charge_power.item(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.charge_power.item(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.charge_power.item(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.charge_power.item(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.charge_power.item(4)
        item.setText(_translate("MainWindow", "5"))
        self.charge_power.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "Select docking places:"))
        self.label_12.setText(_translate("MainWindow", "X:"))
        self.label_13.setText(_translate("MainWindow", "Z:"))
        self.add_station_2.setText(_translate("MainWindow", "Add"))
        self.label_9.setText(_translate("MainWindow", "Select power of charge:"))
        self.label_10.setText(_translate("MainWindow", "Y:"))
        self.cancel_2.setText(_translate("MainWindow", "Cancel"))
        __sortingEnabled = self.docking_places.isSortingEnabled()
        self.docking_places.setSortingEnabled(False)
        item = self.docking_places.item(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.docking_places.item(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.docking_places.item(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.docking_places.item(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.docking_places.item(4)
        item.setText(_translate("MainWindow", "5"))
        self.docking_places.setSortingEnabled(__sortingEnabled)
        self.label_11.setText(_translate("MainWindow", "Insert start position:"))
        self.label_8.setText(_translate("MainWindow", "Adding station"))
        self.label_15.setText(_translate("MainWindow", "Adding map"))
        self.checkBox.setText(_translate("MainWindow", "default map"))
        self.go_back.setText(_translate("MainWindow", "BACK"))
        self.go_back_3.setText(_translate("MainWindow", "BACK"))
        self.label_16.setText(_translate("MainWindow", "Work in progress"))
        self.go_back_2.setText(_translate("MainWindow", "BACK"))
        self.label_14.setText(_translate("MainWindow", "Work in progress"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSimulation.setText(_translate("MainWindow", "Simulation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
