# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_drone.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_new_drone(object):
    def setupUi(self, new_drone):
        new_drone.setObjectName("new_drone")
        new_drone.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(new_drone)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 330, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.add_drone = QtWidgets.QPushButton(self.centralwidget)
        self.add_drone.setGeometry(QtCore.QRect(190, 330, 75, 23))
        self.add_drone.setObjectName("add_drone")
        self.delete_drone = QtWidgets.QPushButton(self.centralwidget)
        self.delete_drone.setGeometry(QtCore.QRect(280, 330, 75, 23))
        self.delete_drone.setObjectName("delete_drone")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 40, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 130, 47, 13))
        self.label_4.setObjectName("label_4")
        self.x_pos = QtWidgets.QSlider(self.centralwidget)
        self.x_pos.setGeometry(QtCore.QRect(210, 70, 160, 22))
        self.x_pos.setMaximum(1000)
        self.x_pos.setOrientation(QtCore.Qt.Horizontal)
        self.x_pos.setObjectName("x_pos")
        self.y_pos = QtWidgets.QSlider(self.centralwidget)
        self.y_pos.setGeometry(QtCore.QRect(210, 100, 160, 22))
        self.y_pos.setMaximum(1000)
        self.y_pos.setOrientation(QtCore.Qt.Horizontal)
        self.y_pos.setObjectName("y_pos")
        self.z_pos = QtWidgets.QSlider(self.centralwidget)
        self.z_pos.setGeometry(QtCore.QRect(210, 130, 160, 22))
        self.z_pos.setMaximum(1000)
        self.z_pos.setOrientation(QtCore.Qt.Horizontal)
        self.z_pos.setObjectName("z_pos")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 160, 101, 16))
        self.label_5.setObjectName("label_5")
        self.drone_select_type = QtWidgets.QListWidget(self.centralwidget)
        self.drone_select_type.setGeometry(QtCore.QRect(190, 180, 256, 71))
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
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 270, 47, 13))
        self.label_6.setObjectName("label_6")
        self.drone_id = QtWidgets.QLCDNumber(self.centralwidget)
        self.drone_id.setGeometry(QtCore.QRect(190, 290, 64, 23))
        self.drone_id.setObjectName("drone_id")
        new_drone.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(new_drone)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        new_drone.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(new_drone)
        self.statusbar.setObjectName("statusbar")
        new_drone.setStatusBar(self.statusbar)

        self.retranslateUi(new_drone)
        QtCore.QMetaObject.connectSlotsByName(new_drone)

    def retranslateUi(self, new_drone):
        _translate = QtCore.QCoreApplication.translate
        new_drone.setWindowTitle(_translate("new_drone", "MainWindow"))
        self.pushButton.setText(_translate("new_drone", "Cancel"))
        self.add_drone.setText(_translate("new_drone", "Add"))
        self.delete_drone.setText(_translate("new_drone", "Delete"))
        self.label.setText(_translate("new_drone", "Insert start position:"))
        self.label_2.setText(_translate("new_drone", "X:"))
        self.label_3.setText(_translate("new_drone", "Y:"))
        self.label_4.setText(_translate("new_drone", "Z:"))
        self.label_5.setText(_translate("new_drone", "Select drone type:"))
        __sortingEnabled = self.drone_select_type.isSortingEnabled()
        self.drone_select_type.setSortingEnabled(False)
        item = self.drone_select_type.item(0)
        item.setText(_translate("new_drone", "Default"))
        item = self.drone_select_type.item(1)
        item.setText(_translate("new_drone", "Scout1"))
        item = self.drone_select_type.item(2)
        item.setText(_translate("new_drone", "Scout2"))
        item = self.drone_select_type.item(3)
        item.setText(_translate("new_drone", "Scout3"))
        item = self.drone_select_type.item(4)
        item.setText(_translate("new_drone", "Carrier1"))
        item = self.drone_select_type.item(5)
        item.setText(_translate("new_drone", "Carrier2"))
        item = self.drone_select_type.item(6)
        item.setText(_translate("new_drone", "Carrier3"))
        item = self.drone_select_type.item(7)
        item.setText(_translate("new_drone", "Mixed1"))
        item = self.drone_select_type.item(8)
        item.setText(_translate("new_drone", "Mixed2"))
        item = self.drone_select_type.item(9)
        item.setText(_translate("new_drone", "Mixed3"))
        self.drone_select_type.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("new_drone", "Drone ID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_drone = QtWidgets.QMainWindow()
    ui = Ui_new_drone()
    ui.setupUi(new_drone)
    new_drone.show()
    sys.exit(app.exec_())
