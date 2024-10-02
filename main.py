import pygame as pg
import constants
import player as pl
import asteroids as ast
import asteroidFiled as af


def main():
    pg.init()
    print("Starting asteroids!")
    screen = pg.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0
    x = constants.SCREEN_WIDTH/2
    y = constants.SCREEN_HEIGHT/2
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    pl.Player.containers = (updatable, drawable)
    ast.Asteroid.containers = (updatable, drawable)
    af.AsteroidField.containers = (updatable)
    player = pl.Player(x, y)
    asf = af.AsteroidField()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill("black")
        for object in updatable:
            object.update(dt)
        for object in drawable:
            object.draw(screen)
        pg.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000


if __name__ == "__main__":
    main()
