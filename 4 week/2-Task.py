import pygame
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

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
