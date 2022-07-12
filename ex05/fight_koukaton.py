import pygame as pg
import sys
import random


class Screen:
    def __init__(self, title, size, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size)   #Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image, scale, position):
        self.sfc = pg.image.load(image) #Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, scale) #Surface
        self.rct = self.sfc.get_rect()  #Rect
        self.rct.center = position
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]    == True:
            self.rct.centery -= 8
        if key_states[pg.K_DOWN]  == True:
            self.rct.centery += 8
        if key_states[pg.K_LEFT]  == True:
            self.rct.centerx -= 8
        if key_states[pg.K_RIGHT] == True:
            self.rct.centerx += 8
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    == True:
                self.rct.centery += 8
            if key_states[pg.K_DOWN]  == True:
                self.rct.centery -= 8
            if key_states[pg.K_LEFT]  == True:
                self.rct.centerx += 8
            if key_states[pg.K_RIGHT] == True:
                self.rct.centerx -= 8
        self.blit(scr)


class Bomb:
    def __init__(self, color, radius, velocity, scr: Screen):
        self.sfc = pg.Surface((2*radius, 2*radius)) #Surface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (radius, radius), radius)
        self.rct = self.sfc.get_rect() #Rect
        self.rct.centerx = random.randint(radius, scr.rct.width-radius)
        self.rct.centery = random.randint(radius, scr.rct.height-radius)
        self.vx, self.vy = velocity
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Enemy:
    def __init__(self, image, scale, position):
        self.sfc = pg.image.load(image) #Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, scale) #Surface
        self.rct = self.sfc.get_rect()  #Rect
        self.rct.center = position
        self.life = 100
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, player: Bird, scr: Screen):
        if self.rct.centerx - player.rct.centerx < 0:
            self.rct.centerx += 2
        if self.rct.centerx - player.rct.centerx > 0:
            self.rct.centerx -= 2
        if self.rct.centery - player.rct.centery > 0:
            self.rct.centery -= 2
        if self.rct.centery - player.rct.centery < 0:
            self.rct.centery += 2
        self.blit(scr)


def main():
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1600, 900), "ex05/fig/pg_bg.jpg")
    kkt = Bird("ex05/fig/6.png", 2.0, (random.randint(100, 700), random.randint(100, 800)))
    teki = Enemy("ex05/fig/6.png", 4.0, (random.randint(900, 1500), random.randint(100, 800)))
    bkd1 = Bomb((255, 0, 0), 10, (random.choice([-4, 4]), random.choice([-4, 4])), scr)
    bkd2 = Bomb((255, 0, 0), 10, (random.choice([-4, 4]), random.choice([-4, 4])), scr)
    bkd3 = Bomb((255, 0, 0), 10, (random.choice([-4, 4]), random.choice([-4, 4])), scr)
    while True:
        scr.blit()
        key_state = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        kkt.update(scr)
        teki.update(kkt, scr)
        bkd1.update(scr)
        bkd1.blit(scr)
        bkd2.update(scr)
        bkd2.blit(scr)
        bkd3.update(scr)
        bkd3.blit(scr)
        if bkd1.rct.colliderect(teki.rct):
            print(teki.life)
            teki.life -= 1
        if kkt.rct.colliderect(bkd1.rct):
            return
        if kkt.rct.colliderect(bkd2.rct):
            return
        if kkt.rct.colliderect(bkd3.rct):
            return
        if kkt.rct.colliderect(teki.rct):
            return
        if teki.life == 0:
            return
        pg.display.update()
        clock.tick(100)


def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right :
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()