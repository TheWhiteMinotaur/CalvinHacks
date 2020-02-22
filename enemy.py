from entity import Entity
from math import sqrt

class Enemy(Entity):
    def __init__(self, health, sX, sY, sprites):
        self.health = health
        self.x = sX
        self.y = sY
        self.sprites = []

    def is_point_visible(self, point):
        return sqrt((self.x - point[0])**2 + (self.y - point[1])**2) - 50 < 0

        # pygame.draw.circle(0,self.color, {self.x, self.y}, size)
