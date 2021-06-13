import pygame

'''
properties template

props {
    'width' : width
    'height' : height
    'depth' : depth
    'charge power' : charge_power
    'docking places' : docking_places
}

'''

class DockingStation:
    def __init__(self, position, id):
        self.position = position
        # self.properties = properties
        self.id = id
        self.width = 50
        self.height = 200
        self.depth = 50
        self.is_collidable = True

    def on_update(self, step):
        print("Docking station {0} at position: {1}, {2}, {3}".format(self.id, self.position[0], self.position[1], self.position[2]))

    def on_display(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.position[0]-self.width/2, self.position[1] - self.depth/2, self.width, self.depth))

    def on_collision(self, step):
        print("AŁA")

    def get_collider(self):
        return (self.position[0]-self.width/2, self.position[1] - self.depth/2, self.width, self.depth)