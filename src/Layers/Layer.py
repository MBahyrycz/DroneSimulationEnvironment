import numpy as np
import matplotlib.pyplot as plt

from enum import Enum

class Type(Enum):
    DRONE = 1
    STATION = 2
    MAP = 3
    WEATHER = 4

class Layer:
    def __init__(self, type, components, width=50, height=50, depth=50): # 
        self.type = type
        self.width = width
        self.height = height
        self.depth = depth
        self.components = components
        self.is_visible = True
        self.is_computed = True

    def on_update(self, step):
        if self.is_computed:
            for c in self.components:
                c.on_update(step)

    def on_display(self, surface):
        if self.is_visible:
            for c in self.components:
                c.on_display(surface)

    def add_component(self, component):
        self.components.append(component)
    