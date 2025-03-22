from pygame import *
window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
pingpong = transform.scale(image.load("Fon.png"),(700,500))


clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_width,player_height,player_speed):
        super().__init__()
        self.image =transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

    
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y  > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y  <  455:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y  > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y  < 455:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self,player_image,player_x,player_y,player_width,player_height,player_speed):
        super().__init__(player_image,player_x,player_y,player_width,player_height,player_speed)
        self.speed_x = self.speed
        self.speed_y = self.speed
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
    def update(self):
        if ball1.rect.y < 0 or ball1.rect.y > 450:
            ball1.speed_y *= -1
        if ball1.rect.x > 650 or ball1.rect.x < 0:
            ball1.speed_x *= -1
        if ball1.colliderect(raketka_red.rect):
            ball1.speed_y *= -1
        if ball1.colliderect(raketka_blue.rect):
            ball1.speed_y *= -1
        ball1.rect.x += ball1.speed_x
        ball1.rect.y += ball1.speed_y
          


ball1 = Ball('ball.png',320,200,50,50,2)
raketka_red = Player('raketka.png',0,100,100,100,5)
raketka_blue = Player('raketka11.png',600,100,100,100,5)

font.init()
font1 = font.SysFont('Arial',30)

count1 = 0
count2 = 0 

finish = False
game = True
while game:
    if finish != True:
        window.blit(pingpong,(0,0))

        text_count1 = font1.render('Счёт:' +str(count1),1,(255,255,255))
        text_count2 = font1.render('Счёт:' +str(count2),1,(255,255,255))

        window.blit(text_count1,(0,10))
        window.blit(text_count2,(600,10))

        
        raketka_red.reset()
        raketka_red.update_l()

        raketka_blue.reset()
        raketka_blue.update_r()
    
        ball1.reset()
        ball1.update()
    for e in event.get():
         if e.type == QUIT:
             game =  False

    clock.tick(FPS)
    display.update()
