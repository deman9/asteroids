import pygame
from modules import circleshape
from modules import constants


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        radius = constants.PLAYER_RADIUS
        super().__init__(x, y, radius)
        self.rotation = 0
        self.cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        position = self.triangle()
        pygame.draw.polygon(screen, 'white', position, width=2)

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(0-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(0-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.cooldown -= dt

    def shoot(self):
        if self.cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(
            self.rotation) * constants.PLAYER_SHOT_SPEED
        self.cooldown = constants.PLAYER_SHOOT_COOLDOWN


class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super(). __init__(x, y, constants.SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
