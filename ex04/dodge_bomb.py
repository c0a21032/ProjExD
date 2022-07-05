import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1700, 900))

    bgimg = pg.image.load("ex04/fig/pg_bg.jpg")
    bgrect = bgimg.get_rect()

    life = 900
    lifebar = pg.Surface((100, 900))
    liferect = lifebar.get_rect()
    liferect.center = 1650, 450
    rect = (0, 0, 100, life)
    pg.draw.rect(lifebar, (0, 255, 0), rect)

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
        screen.blit(lifebar, liferect)

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
            life -= 5

        if life == 0:
            return

        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        pg.display.update()

        clock = pg.time.Clock()
        if key_dic[pg.K_SPACE]: #SPACEを押すと時間が四分の一になる
            clock.tick(250)
            life -= 1  
        else:
            clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()