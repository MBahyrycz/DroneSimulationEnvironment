import copy

# from Components.Drone import *

'''
properties template

props {
        'name' {
                'velocity' : float
                'width' : float
                'height' : float
                'depth' : float
                'carriage' : float
                'camera': bool
                'battery': float
                'dis_rate': discharge rate -> float
                'file_path': path to png}
}
'''


class DroneLib:
    org_props = {"default": {'velocity': 10, 'width': 60, 'height': 60, 'depth': 60, 'carriage': 5, 'camera': 0,
                             'battery': 100, 'dis_rate': 5, 'file_path': "drone0.png"},
                 "scout1": {'velocity': 15, 'width': 30, 'height': 30, 'depth': 20, 'carriage': 1, 'camera': 1,
                            'battery': 120, 'dis_rate': 3, 'file_path': "drone4.png"},
                 "scout2": {'velocity': 16, 'width': 30, 'height': 30, 'depth': 30, 'carriage': 1, 'camera': 1,
                            'battery': 110, 'dis_rate': 3, 'file_path': "drone5.png"},
                 "scout3": {'velocity': 12, 'width': 40, 'height': 40, 'depth': 40, 'carriage': 3, 'camera': 1,
                            'battery': 150, 'dis_rate': 3, 'file_path': "drone6.png"},
                 "carrier1": {'velocity': 10, 'width': 60, 'height': 60, 'depth': 60, 'carriage': 7, 'camera': 0,
                              'battery': 100, 'dis_rate': 5, 'file_path': "drone7.png"},
                 "carrier2": {'velocity': 8, 'width': 60, 'height': 60, 'depth': 60, 'carriage': 5, 'camera': 0,
                              'battery': 110, 'dis_rate': 5, 'file_path': "drone8.png"},
                 "carrier3": {'velocity': 12, 'width': 60, 'height': 60, 'depth': 60, 'carriage': 9, 'camera': 0,
                              'battery': 100, 'dis_rate': 5, 'file_path': "drone9.png"},
                 "mixed1": {'velocity': 10, 'width': 40, 'height': 40, 'depth': 40, 'carriage': 6, 'camera': 1,
                            'battery': 100, 'dis_rate': 4, 'file_path': "drone10.png"},
                 "mixed2": {'velocity': 9, 'width': 40, 'height': 40, 'depth': 40, 'carriage': 5, 'camera': 1,
                            'battery': 120, 'dis_rate': 4, 'file_path': "drone11.png"},
                 "mixed3": {'velocity': 11, 'width': 40, 'height': 40, 'depth': 40, 'carriage': 4, 'camera': 1,
                            'battery': 100, 'dis_rate': 4, 'file_path': "drone12.png"}}

    def __init__(self, props=copy.deepcopy(org_props)):
        self.props = props

    def add_drone(self, name: str, props: dict) -> None:
        self.props[name] = props

    def remove_drone(self, name: str) -> None:
        self.props.pop(name, None)

    def get_props(self, name) -> dict:
        return self.props[name]


'''
    def get_drone(self, name):
        return Drone(self.store[name])
'''
