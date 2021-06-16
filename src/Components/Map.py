import pygame
import os

'''
properties template

props {
        'width' : float
        'height' : float
        'name' : str
        'file_path': path to png
}
'''

class Map:
    def __init__(self, props, id):
        self.props = props
        self.id=id
        self.background = pygame.image.load(os.path.join(os.pardir, "assets", self.props['file_path']))
        self.is_collidable = False

    def on_update(self, step):
        print("Map: {0} width: {1}, height: {2}".format(self.props['name'], self.props['width'], self.props['height']))

    def on_display(self, surface):
        width, height = pygame.display.get_surface().get_size()
        self.background = pygame.transform.scale(self.background, (max(width, self.props['width']), max(height, self.props['height'])))
        surface.blit(self.background, (0,0))
