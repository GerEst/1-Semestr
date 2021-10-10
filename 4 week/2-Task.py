import pygame
from os import system
from random import randint
from pygame.draw import *
pygame.init()
import math

FPS = 30
screen = pygame.display.set_mode((400, 600))

# цвета
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
blue = (0,255,255)
dark_green = (0,125,0)
yellow = (255, 180, 85)
# цвет экрана
rect(screen, blue, (0, 0, 400, 600))
rect(screen, green, (0, 300, 400, 600))

# ноги
x = 185
for i in range(2):
    rect(screen, (white), (x, 470, 20, 60))
    x += 80
x = 185
for i in range(2):
    rect(screen, (white), (x+30, 460, 15, 50))
    x += 85
# тело голова
rect1 = (172, 410, 150, 75)
rect2 = (272, 360, 60, 30)
rect3 = (292, 375, 60, 30)
circle(screen, (255, 221, 85), (390, 10), 70) # солнце
ellipse(screen, white, rect1)
ellipse(screen, white, rect2)
ellipse(screen, white, rect3)
#sheja
rect(screen, white, (272, 374, 50, 70))
#rog
polygon(screen, (255, 255, 0), [(300,360), (310,361),
                               (315,362), (310,300)])
# хвост, грива
for i in range(8):
    h = randint(15,20)  # толщина элипса
    colour = (randint(190,255), randint(190,255), randint(190,255))
    ellipse(screen, colour, (270 - randint(0,6)*i , 345 + 10*i , h*2, h))
for i in range(8):
    h = randint(15,20)
    colour = (randint(190,255), randint(190,255), randint(190,255))
    ellipse(screen, colour, (170 - randint(0,6)*i , 410 + 10*i , h*2, h))
# глаза
circle(screen, (255, 0, 220), (320, 375), 6)
circle(screen, (255, 255, 255), (321, 373), 3)
circle(screen, (0, 0, 0), (322, 375), 2)

# дерево
xd = 70
yd = 350
rect(screen, (255, 255, 255), (xd, yd, 20, 70))
ellipse(screen, dark_green, (xd-27,yd - 50,75,63))
circle(screen, yellow, (xd+35, 345), 10)
ellipse(screen, dark_green, (xd-52,yd - 105,120,60))
circle(screen, yellow, (120, 280), 10)
circle(screen, yellow, (30, 275), 10)
ellipse(screen, dark_green, (xd-30,yd - 158,75,63))
circle(screen, yellow, (100, 220), 10)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
            system("cls")
            print(f"x = {pygame.mouse.get_pos()[0]}")
            print(f"y = {pygame.mouse.get_pos()[1]}")
            if event.type == pygame.QUIT:
                finished = True


pygame.quit()
