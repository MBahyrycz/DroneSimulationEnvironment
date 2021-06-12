import pygame
import os

class Map:
    def __init__(self, width, height, name="", file_path="terrain.png"):
        self.width = width
        self.height = height
        self.name = name
        self.file_path = file_path
        self.background = pygame.image.load(os.path.join(os.pardir, "assets", self.file_path))
        self.is_collidable = False

    def on_update(self, step):
        print("Map: {0} width: {1}, height: {2}".format(self.name, self.width, self.height))

    def on_display(self, surface):
        width, height = pygame.display.get_surface().get_size()
        self.background = pygame.transform.scale(self.background, (max(width, self.width), max(height, self.height)))
        surface.blit(self.background, (0,0))
