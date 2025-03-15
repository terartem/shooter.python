
from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption('Шутер')
galaxy = transform.scale(image.load('galaxy.jpg'),(700,500))

clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.load('fire.ogg')



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
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x  > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx-5,self.rect.top,10,15,6)
        bullets.add(bullet)
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -10:
            self.kill()
            

lost = 0
class Ufo(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = -60
            self.rect.x = randint(0,635)
            self.rect.y = 0
            lost = lost +  1

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = -60
            self.rect.x = randint(0,635)
            self.rect.y = 0
            










rocket = Player('rocket.png',600,430,50,50,8)


asteroids = sprite.Group()
for i in range(3):
    asteroid = Asteroid('asteroid.png',randint(0,635),-100,randint(30,75),randint(50,75),randint(1,7))
    asteroids.add(asteroid)

bullets = sprite.Group()


monsters = sprite.Group()
for i in range(4):
    monster = Ufo('ufo.png',randint(0,635),-100,50,50,randint(1,3))
    monsters.add(monster)

font.init()
font1 = font.SysFont('Arial',30)

count = 0
health = 3


finish = False
game = True
while game:
    if finish != True:
        window.blit(galaxy,(0,0))
        

        text_health = font1.render('Жизни:' +str(health),1,(255,255,255))
        text_count = font1.render('Счёт:' +str(count),1,(255,255,255))
        text_lose = font1.render('Пропущено:' +str(lost),1,(255,255,255))
        spritemonster = sprite.spritecollide(
            rocket,monsters,True)
        spriteasteroid = sprite.spritecollide(rocket,asteroids,True)
        if spritemonster or spriteasteroid:
            health -= 1
            for m in spritemonster:
                monster = Ufo('ufo.png',randint(0,635),-100,60,60,randint(1,3))
                monsters.add(monster)
            for m in spriteasteroid:
                asteroid = Asteroid('asteroid.png',randint(0,635),-100,randint(30,75),randint(50,75),randint(1,7))
                asteroids.add(asteroid)
        if  health < 0 or lost > 5:
            lose = font1.render('ТЫ ПРОИГРАЛ',60,(230,0,0))
            window.blit(lose,(300,200))
            finish = True

        sprites_list = sprite.groupcollide(bullets,monsters,True,True)
        for n in sprites_list:
            count += 1
            monster = Ufo('ufo.png',randint(0,635),-100,60,60,randint(1,3))
            monsters.add(monster)

        if count >= 10:
            win = font1.render('ТЫ ПОБЕДИЛ',60,(0,220,0))
            window.blit(win,(300,200))
            finish = True


        window.blit(text_lose,(0,10))
        window.blit(text_count,(0,40))
        window.blit(text_health,(0,70))
        
        rocket.reset()
        rocket.update()

        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        asteroids.update()
        asteroids.draw(window)
    for e in event.get():
        if e.type == QUIT:
            game =  False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()
            if e.key == K_r and finish == True:
                for monster in monsters:
                    monster.rect.y = -100
                for asteroid in asteroids:
                    asteroid.rect.y = -100    

                count = 0
                lost = 0
                finish = False

    clock.tick(FPS)
    display.update()