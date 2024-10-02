import pygame as pg
import constants
import player as pl


def main():
    pg.init()
    print("Starting asteroids!")
    screen = pg.display.set_mode(
        (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0
    x = constants.SCREEN_WIDTH/2
    y = constants.SCREEN_HEIGHT/2
    player = pl.Player(x, y)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pg.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000


if __name__ == "__main__":
    main()
