from pygame import *
from random import *

okno = display.set_mode((1200,600))
class gameobj(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
class tank(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.napr = 'vverh'
    def ris(self):
        
        self.image1 = transform.scale(self.image,(30,30))
        self.image2 = transform.rotate(self.image, 180)
        self.image3 = transform.rotate(self.image, 90)
        self.image4 = transform.rotate(self.image, -90)
        if self.napr == 'vverh': 
            okno.blit(self.image1, (self.rect.x, self.rect.y))       
        elif self.napr == 'vniz':
            okno.blit(self.image2, (self.rect.x, self.rect.y))
        elif self.napr == 'vprav':
            okno.blit(self.image4, (self.rect.x, self.rect.y))
        elif self.napr == 'vlev':
            okno.blit(self.image3, (self.rect.x, self.rect.y))
    def move(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_UP]:
            self.napr = 'vverh'
            self.rect.y -= 5
            self.lasty = self.rect.y
        elif kn[K_DOWN]:
            self.napr = 'vniz'
            self.rect.y += 5
            self.lasty = self.rect.y
        elif kn[K_RIGHT]:
            self.napr = 'vprav'
            self.rect.x += 5
            self.lastx = self.rect.x
        elif kn[K_LEFT]:
            self.napr = 'vlev'
            self.rect.x -= 5
            self.lastx = self.rect.x
am1 = image.load('background.png')
am1 = transform.scale(am1, (600,600))
tankp = tank('rt.png',0,0, 30,30) 
fps = time.Clock() #контроль fps
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
