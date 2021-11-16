import pygame
from Ball import *
from Constantine import *
from random import randint

class Game():
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.run = True
        self.loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')
                print('x = ', event.pos[0])
                print('y = ', event.pos[1])

    def render(self):
        self.screen.fill(BLACK)
        ##

    def loop(self):

        clock = pygame.time.Clock()

        while self.run:
            clock.tick(FPS)
            self.handle_events()
            self.render()
            pygame.display.update()




screen1 = pygame.display.set_mode((1200, 900))
game1 = Game(screen1, "geroin")
