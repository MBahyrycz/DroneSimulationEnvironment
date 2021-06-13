import pygame

'''
properties template

props {
    'width' : width
    'height' : height
    'depth' : depth
    'charge power' : charge_power (charging rate?)
    'docking places' : docking_places
}

'''

class DockingStation:
    def __init__(self, position, props,  id):
        self.position = position
        self.props = props
        self.id = id
        self.is_collidable = True

    def on_update(self, step):
        print("Docking station {0} at position: {1}, {2}, {3}".format(self.id, self.position[0], self.position[1], self.position[2]))

    def on_display(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.position[0]-self.props['width']/2, self.position[1] - self.props['depth']/2, self.props['width'], self.props['depth']))

    def on_collision(self, step):
        print("AŁA")

    def get_collider(self):
        return self.position[0]-self.props['width']/2, self.position[1] - self.props['depth']/2, self.props['width'], self.props['depth']