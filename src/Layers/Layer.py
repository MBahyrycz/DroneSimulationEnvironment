import numpy as np
import matplotlib.pyplot as plt

class Layer:
    def __init__(self, components, width=50, height=50, depth=50): # 
        self.width = width
        self.height = height
        self.depth = depth
        self.components = components

    def on_update(self, delta_time):
        for c in self.components:
            c.on_update()

    def show(self, delta_time):
        # fig = plt.figure()
        # ax = fig.add_subplot(projection='3d')
        x = []
        y = []
        z = []
        for c in self.components:
            x.append(c.position[0])
            y.append(c.position[1])
            z.append(c.position[2])

        # ax.scatter(x, y, z, marker='o')
        # plt.show()

    def add_component(self, component):
        self.components.append(component)
    