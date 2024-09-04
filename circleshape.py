import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.postition = pygame.Vector2(x, y)
        self.velocity = pygame.Vector3(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass
