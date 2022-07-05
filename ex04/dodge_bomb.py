import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    bg = pg.image.load("ex04/pg_bg.jpg")
    bg_rect = bg.get_rect()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()