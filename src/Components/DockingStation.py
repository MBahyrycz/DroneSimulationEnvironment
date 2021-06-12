import pygame

class DockingStation:
    def __init__(self, position, id):
        self.position = position
        self.id = id
        self.width = 50
        self.height = 200
        self.depth = 50
        self.collidable = True

    def on_update(self, step):
        print("Docking station {0} at position: {1}, {2}, {3}".format(self.id, self.position[0], self.position[1], self.position[2]))

    def on_display(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.position[0]-self.width, self.position[1] - self.depth, self.width, self.depth))

    def on_collide(self, step):
        pass