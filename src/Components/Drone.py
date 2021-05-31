import numpy as np

class Drone:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def on_update(self):
        self.position += np.array([1, 1, 0]) * self.velocity
        print(self.position)