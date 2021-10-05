import pygame
from random import randint
from pygame.draw import *
pygame.init()
import math

FPS = 30
screen = pygame.display.set_mode((480, 720))
# цвета
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
blue = (0,255,255)
dark_green = (0,125,0)
yellow = (255, 180, 85)
# градиент
def gradientRect( screen, left_colour, right_colour, target_rect ):
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    line( colour_rect, left_colour,  ( 0,0 ), ( 1,1 ) )
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    screen.blit( colour_rect, target_rect )                                    # paint it

# небо земля

rect(screen, green, (0, 360, 480, 360))
gradientRect( screen, blue , (255,230,0), pygame.Rect( 0,0, 480, 360 ))
pygame.display.flip()
# солнце
circle(screen, (255, 221, 85), (460, 40), 65)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
