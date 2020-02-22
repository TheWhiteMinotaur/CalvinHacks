from entity import Entity
from math import sqrt

class Enemy(Entity):
    def __init__(self, health, sX, sY, vision, sprites):
        self.health = health
        self.x = sX
        self.y = sY
        self.vision = vision
        self.sprites = []

    def is_point_visible(self, point):
        return sqrt((self.x - point[0])**2 + (self.y - point[1])**2) - 50 < 0

        # pygame.draw.circle(0,self.color, {self.x, self.y}, size)
