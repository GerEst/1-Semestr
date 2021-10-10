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
    colour_rect = pygame.Surface( ( 2, 2 ) )
    line( colour_rect, right_colour, ( 1,0 ), ( 0,1 ) )
    line( colour_rect, left_colour,  ( 0,1 ), ( 0,0 ) )
    line( colour_rect, left_colour,  ( 0,1 ), ( 1,1 ) )

    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )
    screen.blit( colour_rect, target_rect )

# земля, небо
rect(screen, green, (0, 360, 480, 360))
gradientRect( screen, blue , (255,230,0), pygame.Rect( 0,0, 480, 360 ))
pygame.display.flip()

def trees(xd,yd):
    sc = yd/600 # size coeficient
    rect(screen, (255, 255, 255), (xd, yd, 20, 70*sc))
    ellipse(screen, dark_green, (xd-27,yd - 50*sc,75,63*sc))
    circle(screen, yellow, (xd+35, yd - 5*sc), 10*sc)
    ellipse(screen, dark_green, (xd-52,yd - 105*sc,120,60*sc))
    circle(screen, yellow, (xd + 50, yd - 70*sc), 10*sc)
    circle(screen, yellow, (xd - 40, yd - 75*sc), 10*sc)
    ellipse(screen, dark_green, (xd-30,yd - 158*sc,75,63*sc))
    circle(screen, yellow, (xd + 30, yd - 130*sc), 10*sc)


# unicorn
def unicorn(x,y):
    pass
    #nogi
    a = x
    for i in range(2):
        rect(screen, (white), (a + 5*y/600, y + 60*y/600, 20*y/600, 60*y/600))
        a += 70*y/600
    a = x
    for i in range(2):
        rect(screen, (white), (a+35*y/600, y + 60*y/600, 15*y/600, 50*y/600))
        a += 70*y/600

    telo = (x, y,140*y/600,70*y/600)
    sheja = (x + 130*y/900, y -70*y/1200, 155*y/1800,70*y/600)
    nos = (x + 140*y/850, y -70*y/1200, 70*y/600,30*y/600)
    golova = (x + 140*y/1040, y -70*y/750, 70*y/600,35*y/600)
    # rog
    polygon(screen, (255, 255, 0), [(x + 140*y/650,y -70*y/850), (x + 140*y/625,y -70*y/850),
                                   (x + 140*y/600,y -70*y/850), (x + 140*y/550,y -70*y/400)])
    #telo
    ellipse(screen, white, golova)
    ellipse(screen, white, nos)
    ellipse(screen, white, telo)
    rect(screen, white, sheja)
    #glaza
    circle(screen, (255, 0, 220), (x + 140*y/625,y -70*y/1050), 6*y/600)
    circle(screen, (255, 255, 255), (x + 140*y/625 - 2 ,y -70*y/1050+1 ), 3*y/600)
    circle(screen, (0, 0, 0), (x + 140*y/625+2,y -70*y/1050 ), 2*y/600)
    #hvost i griva
    for i in range(8):
        h = randint(15,20)  # толщина элипса
        colour = (randint(190,255), randint(190,255), randint(190,255))
        ellipse(screen, colour, (x + 140*y/1020 - randint(0,6)*i*y/600 , y -70*y/725 + 10*i*y/600 , h*2*y/600, h*y/600))
    for i in range(8):
        h = randint(15,20)
        colour = (randint(190,255), randint(190,255), randint(190,255))
        ellipse(screen, colour, (x - randint(0,6)*i*y/600 , y + 10*i*y/600 , h*2*y/600, h*y/600))

# 3 edinoroga v randomnih mestah
for i in range (3):
    g = randint(200,400)
    d = randint(360,700)
    unicorn(g, d)


trees(50, 370)
trees(170, 500)
trees(60, 600)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
