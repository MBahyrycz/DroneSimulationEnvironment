from time import strptime
import numpy as np
import os
import pygame

from Components.Instructions import *
from App.Environment.ObjectManager import *

'''
properties template

props {
        'velocity' : float
        'width' : float
        'height' : float
        'depth' : float
        'carriage' : float
        'camera': bool
        'battery': float
        'dis_rate': discharge rate -> float
        'file_path': path to png
}
'''


class Drone:
    def __init__(self, position, props, id):
        self.position = position
        self.props = props
        self.id = id
        self.is_collidable = True
        self.move_queue = MoveQueue()
        self.current_battery = self.props['battery']
        self.range = (self.current_battery / 1) * self.props['velocity']

        self.trace = []

        # temp
        self.total_energy_cost = 0
        
        self.destination = np.array([500, 500, 0])
        self.texture = pygame.transform.scale(pygame.image.load(os.path.join(os.pardir, "assets", self.props['file_path'])), (self.props['width'], self.props['depth']))
        self.mask = pygame.mask.from_surface(self.texture)

    def go_to(self):
        x_vec = self.destination[0] - self.position[0]
        y_vec = self.destination[1] - self.position[1]
        z_vec = self.destination[2] - self.position[2]

        route_len = np.sqrt(x_vec ** 2 + y_vec ** 2 + z_vec ** 2)
        if route_len == 0:
            # print("Drone id: {0}, vec:".format(self.id), x_vec, y_vec, z_vec)
            return np.array([0, 0, 0])

        elif route_len < self.props['velocity']:
            # print("Drone id: {0}, vec:".format(self.id), x_vec, y_vec, z_vec)
            return np.array([x_vec, y_vec, z_vec])

        else:
            step = np.array([round((self.props['velocity'] * x_vec)/route_len),
                             round((self.props['velocity'] * y_vec)/route_len),
                             round((self.props['velocity'] * z_vec)/route_len)])
            return step

    def set_instructions(self, list):
        move_list = []
        for i in list:
            if i.type == InstructionType.MOVE:
                move_list.append(i)
        self.move_queue.set_instructions(move_list)

    def on_update(self, step):
        if hasattr(self.move_queue.get_instruction(self.position, step), "position"):
            self.destination = self.move_queue.get_instruction(self.position, step).position

        if self.on_discharge():
            move = self.go_to()
            self.position += move
        # print("Drone {0} at position: {1}, {2}, {3} going to destination {4}, {5}, {6} - remaining range {7}".format(
        #     self.id, self.position[0], self.position[1], self.position[2], self.destination[0], self.destination[1], self.destination[2],
        #     self.range
        #     ))

        self.trace.append((self.position[0], self.position[1]))
        ObjectManager.track(self)
        

    def on_display(self, surface):
        surface.blit(self.texture, (self.position[0]-self.props['width']/2, self.position[1] - self.props['depth']/2, self.props['width'], self.props['depth']))

    def on_collision(self, step):
        # print("AŁA")
        pass

    def on_discharge(self):
        if self.current_battery > 0:
            self.current_battery -= 1
            self.total_energy_cost += 1
        self.range = (self.current_battery / 1) * self.props['velocity']
        # print("Current battery: {0}".format(self.current_battery))
        return self.current_battery > 0

    def get_collider(self):
        return self.position[0]-self.props['width']/2, self.position[1] - self.props['depth']/2, self.props['width'], self.props['depth']