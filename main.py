import pygame as pg
from constants import *


def main():
    pg.init()
    print("Starting asteroids!")
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill("black")
        pg.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000


if __name__ == "__main__":
    main()
