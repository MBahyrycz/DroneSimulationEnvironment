import unittest

# import selected elements, ex.:
from src.App.Environment.DroneLib import *


class DroneLibCreationTest(unittest.TestCase):
    def test_library_creation(self):
        dronelib = DroneLib()
        self.assertIsInstance(dronelib, DroneLib)

    def test_get_props(self):
        dronelib = DroneLib()
        props = {'velocity': 10, 'width': 60, 'height': 60, 'depth': 60, 'carriage': 5, 'camera': 0,
                 'battery': 100, 'dis_rate': 5, 'file_path': "drone0.png"}
        self.assertEqual(dronelib.get_props("default"), props)

    def test_add_drone(self):
        dronelib = DroneLib()
        name = "test"
        props = {'velocity': 10, 'width': 60, 'height': 60, 'depth': 60, 'carriage': 5, 'camera': 0,
                 'battery': 100, 'dis_rate': 5, 'file_path': "drone0.png"}
        dronelib.add_drone(name, props)
        self.assertEqual(dronelib.get_props("test"), props)

    def test_remove_drone(self):
        dronelib = DroneLib()
        dronelib.remove_drone("default")
        with self.assertRaises(KeyError):
             dronelib.get_props("default")


if __name__ == '__main__':
    unittest.main()
