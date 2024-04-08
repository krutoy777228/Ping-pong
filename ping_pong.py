from pygame import *


img_back = "fon.jpg"
img_ball = 'ball.jpg'
img_raket = 'stena.png'


class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 115:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 115:
            self.rect.y += self.speed





#класс спрайта-врага  
class Enemy(GameSprite):
   #движение врага
    def update(self):
        self.rect.x += self.speed









win_width = 700
win_height = 500
display.set_caption("Ping pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


ball = Enemy(img_ball, 300, 300, 100, 100, 1)
raketka_l = Player(img_raket, 30, 300, 30, 110, 1)
raketka_r = Player(img_raket, 300, 300, 30, 110, 1)


a = True
while a:
    for e in event.get():
        if e.type == QUIT:
            a = False
    
    window.blit(background,(0,0))
    ball.update()
    raketka_l.update_l()
    raketka_r.update_r()
    ball.reset()
    raketka_l.reset()
    raketka_r.reset()
    display.update()