from pygame import *
import time 
#высота и ширина
win_height = 500
win_width = 700

#фон
mw = pygame.display.set_mode((500, 500))
back = (200, 255, 255)
mw.fill(back)

#надписи
font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))

#параметры платформ
platform_x1 = 200
platform_y1 = 330

platform_x2 = 200
platform_y2 = 330

#время
clock = time.Clock()
FPS = 60

#music
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

game_over = False 
moving_left = False
moving_right = False

#начальные координаты мяча:
ball_x = 3
ball_y = 3


#классы
class GameSprite(sprite.Sprite):
    def __init__(self, ):
        super().__init__() 
    
#класс платформ
class Racket():
    pass

#класс мяча
class Ball():
    pass

#экземпляры классов
racket = GameSprite()
ball = Ball()

#пока все условия выполняются
while not game_over:
