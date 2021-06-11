import pygame
import os

class Map:
    def __init__(self, width, height, name="", file_name="terrain.png"):
        self.width = width
        self.height = height
        self.name = name
        self.file_name = file_name
        self.background = pygame.image.load(os.path.join(os.pardir, "assets", self.file_name))

    def on_update(self, step):
        print("Map: {0} width: {1}, height: {2}".format(self.name, self.width, self.height))

    def on_display(self, screen):
        screen.blit(self.background, (0,0))
