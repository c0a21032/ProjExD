import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    bg = pg.image.load("ex04/pg_bg.jpg")
    bg_rect = bg.get_rect()
    while True:
        screen.blit(bg, bg_rect)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        pg.display.update()
        clock = pg.time.Clock()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()