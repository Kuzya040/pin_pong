from pygame import *
from random import randint
clock = time.Clock()
image1 = image.load('pngwing.com (2).png')
image2 = image.load('pngwing.com (4).png')
image3 = image.load('platform.png')
image4 = image.load('platform.png')
image4 = transform.rotate(image4,180)
win = display.set_mode((950,650))
bk = transform.scale(image2,(950,650))
display.set_caption("pin pong") #?   название программы
font.init()
text = font.SysFont('Arial',36)
speed_x = 12
speed_y = 12
heart_l = 3
heart_r = 3
text  = font.SysFont('arial',40)
loser = text.render('игрок 1 проиграл',1,(255,255,255))
loser1 = text.render('игрок 2 проиграл',1,(255,255,255))
game = False
finish = False
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
        if keys[K_DOWN] and self.rect.x < 950 - 80:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x >0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < 950 - 80:
            self.rect.y += self.speed
platform_left = Player(image3,1,300,70,220,11)
platform_rigth = Player(image4,850,300,70,220,11)
ball = GameSprite(image1,400,250,100,100,0)
while not game:
    heart1 = text.render('жизней'+' '+str(heart_l),1,(255,255,255))
    heart2 = text.render('жизней'+' '+str(heart_r),1,(255,255,255))
    for i in event.get():
        if i.type == QUIT:
            game = True
    if not finish:
        win.blit(bk,(0,0))
        win.blit(heart1,(0,0))
        win.blit(heart2,(700,0))
        platform_left.update_right()
        platform_rigth.update_left()
        platform_left.reset()
        platform_rigth.reset()
        ball.reset()
        if finish != 1:
            ball.rect.x +=speed_x
            ball.rect.y +=speed_y     
        if ball.rect.y <0 or ball.rect.y == 550:
            speed_y *= -1
        if sprite.collide_rect(platform_left,ball) or sprite.collide_rect(platform_rigth,ball):
            speed_x *= -1
        if ball.rect.x <0:
            heart_l -=1
            ball = GameSprite(image1,400,250,100,100,0)
        if ball.rect.x > 870:
            heart_r -=1
            ball = GameSprite(image1,400,250,100,100,0)
        if heart_l <=0:
            win.blit(loser,(225,325))
            finish = True
        if heart_r <=0:
            win.blit(loser1,(225,325))
            finish = True

    display.update()
    time.delay(20)
