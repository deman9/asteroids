import random
from modules import circleshape
import pygame as pg
from modules import constants


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super(). __init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        n_velocity1 = self.velocity.rotate(angle)
        n_velocity2 = self.velocity.rotate(-angle)
        new_asteroid1 = Asteroid(
            self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity = n_velocity1 * 1.2
        new_asteroid2 = Asteroid(
            self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
        new_asteroid2.velocity = n_velocity2 * 1.2
