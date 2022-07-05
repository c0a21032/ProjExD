import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))

    bg = pg.image.load("ex04/pg_bg.jpg")
    bg_rect = bg.get_rect()
    
    tori_img = pg.image.load("ex04/fig/3.png")
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900, 400

    while True:
        screen.blit(bg, bg_rect)

        key_dic = pg.key.get_pressed()
        if key_dic[pg.K_UP]:
            x, y = tori_rect.center
            y -= 1
            tori_rect.center = x, y
        if key_dic[pg.K_DOWN]:
            x, y = tori_rect.center
            y += 1
            tori_rect.center = x, y
        if key_dic[pg.K_LEFT]:
            x, y = tori_rect.center
            x -= 1
            tori_rect.center = x, y
        if key_dic[pg.K_RIGHT]:
            x, y = tori_rect.center
            x += 1
            tori_rect.center = x, y
        screen.blit(tori_img, tori_rect)

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