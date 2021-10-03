import pygame
from random import randint
from pygame.draw import *
pygame.init()
import math

FPS = 30
screen = pygame.display.set_mode((400, 600))
# цвет экрана
rect(screen, (0, 255, 255), (0, 0, 400, 600))
rect(screen, (0, 255, 0), (0, 300, 400, 600))

white = (255,255,255)

# объекты

rect1 = (172, 410, 150, 75)
rect2 = (272, 360, 60, 30)
rect3 = (292, 375, 60, 30)
circle(screen, (255, 221, 85), (390, 10), 70)
ellipse(screen, white, rect1)
ellipse(screen, white, rect2)
ellipse(screen, white, rect3)
rect(screen, (255, 255, 255), (272, 374, 50, 70))
polygon(screen, (255, 255, 0), [(300,360), (310,361),
                               (315,362), (310,300)])
for i in range(7):
    colour = (randint(190,255), randint(190,255), randint(190,255))
    ellipse(screen, colour, (270 - randint(0,6)*i , 345 + 10*i , 40, 20))

for i in range(7):
    colour = (randint(190,255), randint(190,255), randint(190,255))
    ellipse(screen, colour, (170 - randint(0,6)*i , 410 + 10*i , 40, 20))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
