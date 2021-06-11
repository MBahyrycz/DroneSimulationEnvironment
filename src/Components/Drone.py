import numpy as np

class Drone:
    def __init__(self, position, velocity, id):
        self.position = position
        self.velocity = velocity
        self.id = id
        self.width = 40
        self.height = 40
        self.depth = 40
        self.collidable = True

    def on_update(self, step):
        self.position += np.array([1, 1, 0]) * self.velocity
        print("Drone {0} at position: {1}, {2}, {3}".format(self.id, self.position[0], self.position[1], self.position[2]))

    def on_display(self, screen):
        pass

    def on_collide(self, step):
        pass