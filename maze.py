from pygame import *

win_width = 700
win_height = 500

font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

#music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

window = display.set_mode((win_width, win_height))
display.set_caption("Догонялки")
background = transform.scale(image.load("background.jpg"), (700, 500))


class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x +=self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -=self.speed 
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__ (self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))        

player = Player('hero.png', 5, win_height - 80, 4)
enemy = Enemy('cyborg.png', win_width - 80, 200, 2)
treasure = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
wall_1 = Wall(255, 255, 255, 100, 20, 450, 10)
wall_2 = Wall(255,255, 255, 100, 480, 350, 10)
wall_3 = Wall(255,255, 255, 100, 20, 10, 380)

speed = 10
x1 = 50
y1 = 300
x2 = 300
y2 = 305
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))
        player.update()
        enemy.update()

        player.reset()
        enemy.reset()
        treasure.reset()

        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()

        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()

        if sprite.collide_rect(player, treasure):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(FPS)
    