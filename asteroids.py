import circleshape
import pygame as pg
import constants


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super(). __init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
