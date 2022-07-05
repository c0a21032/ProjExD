import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))

    bgimg = pg.image.load("ex04/fig/pg_bg.jpg")
    bgrect = bgimg.get_rect()

    tori_img = pg.image.load("ex04/fig/3.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400

    bombimg = pg.Surface((20, 20))
    bombimg.set_colorkey((0, 0, 0))
    pg.draw.circle(bombimg, (255, 0, 0), (10, 10), 10)
    bombrect = bombimg.get_rect()
    bombrect.center = random.randint(10, 1590), random.randint(10, 890)
    vx = 1; vy = 1

    while True:
        screen.blit(bgimg, bgrect)

        key_dic = pg.key.get_pressed()
        if key_dic[pg.K_UP]:
            x, y = tori_rect.center
            if 48 < y:
                y -= 1
            tori_rect.center = x, y
        if key_dic[pg.K_DOWN]:
            x, y = tori_rect.center
            if y < 852:
                y += 1
            tori_rect.center = x, y
        if key_dic[pg.K_LEFT]:
            x, y = tori_rect.center
            if 48 < x:
                x -= 1
            tori_rect.center = x, y
        if key_dic[pg.K_RIGHT]:
            x, y = tori_rect.center
            if x < 1552:
                x += 1
            tori_rect.center = x, y
        screen.blit(tori_img, tori_rect)

        x, y = bombrect.center
        if x < 10 or 1590 < x:
            vx *= -1
        elif y < 10 or 890 < y:
            vy *= -1
        x += vx; y += vy
        bombrect.center = x, y
        screen.blit(bombimg, bombrect)

        if tori_rect.colliderect(bombrect):
            return

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