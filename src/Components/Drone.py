import numpy as np
import os
import pygame

class Drone:
    def __init__(self, position, velocity, id, file_path="drone0.png"):
        self.position = position
        self.velocity = velocity
        self.id = id
        self.width = 60
        self.height = 60
        self.depth = 60
        self.is_collidable = True
        self.file_path = file_path
        self.texture = pygame.transform.scale(pygame.image.load(os.path.join(os.pardir, "assets", self.file_path)), (self.width, self.depth))
        self.mask = pygame.mask.from_surface(self.texture)

    def on_update(self, step):
        self.position += np.array([0, 1, 0]) * self.velocity
        print("Drone {0} at position: {1}, {2}, {3}".format(self.id, self.position[0], self.position[1], self.position[2]))

    def on_display(self, surface):
        surface.blit(self.texture, (self.position[0]-self.width/2, self.position[1] - self.depth/2, self.width, self.depth))

    def on_collision(self, step):
        print("AŁA")

    def get_collider(self):
        return (self.position[0]-self.width/2, self.position[1] - self.depth/2, self.width, self.depth)