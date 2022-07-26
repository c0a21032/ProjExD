import pygame as pg
import sys
import random


class Paddle:
    def __init__(self, color, size):
        self.sfc = pg.Surface(size)
        self.rct = self.sfc.get_rect()
        self.rct.center = (300, 550)
        self.sfc.fill(color)
    
    def update(self, key):
        if key[pg.K_RIGHT]:
            self.rct.centerx += 2
        if key[pg.K_LEFT]:
            self.rct.centerx -= 2
        if self.rct.right > 600:
            self.rct.centerx -= 2
        if self.rct.left < 0:
            self.rct.centerx += 2


class Ball:
    def __init__(self, color, radius, velocity):
        self.sfc = pg.Surface((radius*2, radius*2))
        self.rct = self.sfc.get_rect()
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (radius, radius), radius)
        self.rct.center = (300, 400)
        self.vx, self.vy = velocity
    
    def update(self, scr, pad, bri, key):
        self.rct.move_ip(self.vx, self.vy)
        if self.rct.left < scr.left or scr.right  < self.rct.right :
            self.vx *= -1
        if self.rct.top  < scr.top  or scr.bottom < self.rct.bottom:
            self.vy *= -1
        hori, vert = check_bound(self.rct, pad)
        self.vx *= hori
        self.vy *= vert
        for i in bri:
            hori, vert = check_bound(self.rct, i.rct)
            self.vx *= hori
            self.vy *= vert
        if check_bound(self.rct, pad) != (1, 1):
            if key[pg.K_RIGHT]:
                self.vx += 1
            if key[pg.K_LEFT]:
                self.vx -= 1


class Brick:
    def __init__(self, color, size, pos):
        self.sfc = pg.Surface(size)
        self.rct = self.sfc.get_rect()
        self.rct.center = pos
        self.sfc.fill(color)


def check_bound(rct, opp):
    yoko, tate = +1, +1
    if rct.colliderect(opp):
        if(abs(rct.right - opp.left) < 2 or abs(opp.right - rct.left) < 2):
            yoko = -1
            tate = 1
        elif(rct.bottom  > opp.top or opp.bottom > rct.top):
            tate = -1
    return yoko, tate


def make_bricks(width, height, row, line):
    bricks = []
    for i in range(row):
        for j in range(line):
            bricks.append(Brick((100, (255 / line) * j, (255 / row) * i), (width, height), (100 + width*j, 60 + height*i)))
    return bricks


def main():
    pg.display.set_caption("ブロック崩しゲーム")
    screen = pg.display.set_mode((600, 600))
    screen_rect = screen.get_rect()
    bar = Paddle((255, 255, 255), (100, 10))
    sphere = Ball((255, 0, 0), 10, (random.choice([-1, 1]), -1))
    bricks = make_bricks(100, 50, 4, 5)
    clock = pg.time.Clock()
    while True:
        screen.fill((0, 0, 0))
        key = pg.key.get_pressed()
        bar.update(key)
        screen.blit(bar.sfc, bar.rct)
        sphere.update(screen_rect, bar.rct, bricks, key)
        screen.blit(sphere.sfc, sphere.rct)
        for i in bricks:
            if sphere.rct.colliderect(i.rct):
                bricks.remove(i)
            screen.blit(i.sfc, i.rct)
        pg.display.update()
        clock.tick(200)
        for event in pg.event.get():
                if event.type == pg.QUIT: return
        if len(bricks) <= 0 or sphere.rct.bottom > 600:
            return


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()