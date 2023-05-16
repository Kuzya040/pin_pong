from pygame import *
from random import randint
clock = time.Clock()
image1 = image.load('pngwing.com (2).png')
image2 = image.load('pngwing.com (4).png')
image3 = image.load('platform.png')
win = display.set_mode((750,500))
bk = transform.scale(image2,(750,500))
display.set_caption("pin pong") #?   название программы
font.init()
text = font.SysFont('Arial',36)
speed = randint(1,5)
game = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x, player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(player_image,(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < 750 - 80:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x >0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < 750 - 80:
            self.rect.y += self.speed
platform_left = Player(image3,1,300,120,220,5)
platform_rigth = Player(image3,650,300,120,220,5)
while not game:
    for i in event.get():
        if i.type == QUIT:
            game = True
    win.blit(bk,(0,0))
    platform_left.update_right()
    platform_rigth.update_left()
    platform_left.reset()
    platform_rigth.reset()
    display.update()
    time.delay(20)
