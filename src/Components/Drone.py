import numpy as np
import os
import pygame

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
        self.texture = pygame.transform.scale(pygame.image.load(os.path.join(os.pardir, "assets", self.props['file_path'])), (self.props['width'], self.props['depth']))
        self.mask = pygame.mask.from_surface(self.texture)

    def go_to(self, destination):
        x_vec = destination[0] - self.position[0]
        y_vec = destination[1] - self.position[1]
        z_vec = destination[2] - self.position[2]

        route_len = np.sqrt(x_vec**2 + y_vec**2 + z_vec**2)
        step = np.array([(self.props['velocity'] * x_vec)/route_len,
                         (self.props['velocity'] * y_vec)/route_len,
                         (self.props['velocity'] * z_vec)/route_len])
        return step


    def on_update(self, step):
        destination = np.array([500, 500, 0])
        move = self.go_to(destination)
        #self.position += np.array([0, 1, 0]) * self.props['velocity']
        self.position += move
        print("Drone {0} at position: {1}, {2}, {3}".format(self.id, self.position[0], self.position[1], self.position[2]))

    def on_display(self, surface):
        surface.blit(self.texture, (self.position[0]-self.props['width']/2, self.position[1] - self.props['depth']/2, self.props['width'], self.props['depth']))

    def on_collision(self, step):
        print("AŁA")

    def get_collider(self):
        return self.position[0]-self.props['width']/2, self.position[1] - self.props['depth']/2, self.props['width'], self.props['depth']