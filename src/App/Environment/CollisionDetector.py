# think how to handle that

import pygame 

class Collider():
    def __init__(self, rect, id):
        self.rect = rect
        self.id = id

class CollisionDetector():
    def __init__(self):
        self.colliders = []
        self.detections = []

    def detect(self):
        self.detections.clear()
        for first in self.colliders:
            for second in self.colliders:
                if first is not second:
                    if self.collide(first.rect, second.rect):
                        self.detections.append((first, second))
                        print("Object: {0} id collided with object: {1} id".format(first.id, second.id))

    def collide(self, rect1, rect2):
        if rect2[0] + rect2[2] > rect1[0] and rect2[0] < rect1[0] + rect1[2]:
            if rect2[1] + rect2[3] > rect1[1] and  rect2[1] < rect1[1] + rect1[3]:
                return True

        return False

    def shutdown(self):
        self.colliders.clear()
        self.detections.clear()

    def draw_boxes(self, surface):
        for c in self.colliders:
            pygame.draw.rect(surface, (255, 0, 0), c.rect, 2)

    def get_from_layers(self, layers):
        self.colliders.clear()
        for l in layers:
            for c in l.components:
                if c.is_collidable:
                    collider = Collider(c.get_collider(), c.id)
                    self.colliders.append(collider)