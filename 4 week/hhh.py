from os import system
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

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
