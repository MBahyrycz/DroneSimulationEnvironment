import pygame
import os

'''
properties template

props {
    'width' : width
    'height' : height
    'depth' : depth
    'charge_power' : charge_power (charging rate?)
    'docking_places' : docking_places
    'file_path': png_texture
}

'''

class DockingStation:
    def __init__(self, position, props,  id):
        self.position = position
        self.props = props
        self.id = id
        self.is_collidable = True

        self.texture = pygame.transform.scale(pygame.image.load(os.path.join(os.pardir, "assets", self.props['file_path'])), (self.props['width'], self.props['depth']))

    def on_update(self, step):
        # print("Docking station {0} at position: {1}, {2}, {3}".format(self.id, self.position[0], self.position[1], self.position[2]))
        pass

    def on_display(self, surface):
        # pygame.draw.rect(surface, (0, 0, 0), (self.position[0]-self.props['width']/2, self.position[1] - self.props['depth']/2, self.props['width'], self.props['depth']))
        surface.blit(self.texture, (self.position[0]-self.props['width']/2, self.position[1] - self.props['depth']/2, self.props['width'], self.props['depth']))


    def on_collision(self, step):
        # print("AŁA")
        pass

    def get_collider(self):
        return self.position[0]-self.props['width']/2, self.position[1] - self.props['depth']/2, self.props['width'], self.props['depth']