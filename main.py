import pygame
#from random import randint

lost = 0
pygame.font.init()
font2 = pygame.font.Font(None,36)

W, H = 1000, 700
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Теннис')
clock = pygame.time.Clock()
FPS = 100
run = True
finish = False

img_back = "fon.jpg"
img_ball = "ball.png"
background = pygame.transform.scale(pygame.image.load(img_back) ,(W,H))



class Gamesprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  size_x, size_y, player_speed = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed



class Ball(Gamesprite):
    def __init__(self, player_image, player_x, player_y,  size_x, size_y, player_speed = 0):
        Gamesprite.__init__(self, player_image, player_x, player_y,  size_x, size_y, player_speed = 10)
        self.life=5
        self.speed_x = -5
        self.speed_y = -7
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y +=self.speed_y
        if self.rect.y <= 0 or self.rect.bottom >= H:
            self.speed_y *= -1
        is_catch1 = pygame.sprite.collide_rect(self,roketka1)
        if is_catch1:
            self.speed_x *= -1
            self.rect.x += self.speed_x
        is_catch2 = pygame.sprite.collide_rect(self, roketka2)
        if is_catch2:
            self.speed_x *= -1
            self.rect.x += self.speed_x


    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Rocketka(Gamesprite):
    def __init__(self, player_image, player_x, player_y,  size_x, size_y, player_speed = 0):
        Gamesprite.__init__(self, player_image, player_x, player_y,  size_x, size_y, player_speed = 10)
        self.life=5

    def updateL(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 550:
            self.rect.y += self.speed

    def updateR(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed
    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))


def game():
    ball.draw(win)
    ball.update()
    roketka1.draw(win)
    roketka2.draw(win)
    roketka2.updateL()
    roketka1.updateR()




ball=Ball("ball1.png",W//2,H//2,60,60,10)
roketka1=Rocketka("roketka1.png",800,350,120,120,10)
roketka2=Rocketka("roketka2.png",50,350,120,120,10)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    win.blit(background,(0, 0))
    game()
    pygame.display.update()
    clock.tick(60)
