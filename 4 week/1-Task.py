import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

FPS = 30
screen = pygame.display.set_mode((400, 400))
# серый фон
rect(screen, (130, 130, 130), (0, 0, 400, 400))
# лицо
circle(screen, (225, 225, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 2)

circle(screen, (225, 0, 0), (230, 180), 20)
circle(screen, (0, 0, 0), (230, 180), 7)
circle(screen, (0, 0, 0), (230, 180), 20, 2)

circle(screen, (225, 0, 0), (166, 185), 30)
circle(screen, (0, 0, 0), (166, 185), 7)
circle(screen, (0, 0, 0), (166, 185), 30, 2)
rect(screen, (0,0,0), (150, 255, 100, 20))

line(screen, (0, 0, 0), (237-40, 202-35), (185-40, 168-35), 12)
line(screen, (0, 0, 0), (210, 202-39), (255, 145), 12)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
