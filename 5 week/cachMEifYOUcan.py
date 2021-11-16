import pygame
from Ball import *
from Constantine import *
from random import randint

class Game():
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.run = True
        self.balls = []
        self.start()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for j in self.balls:
                    if abs(event.pos[0] - j.x) < j.r and abs(event.pos[1] - j.y) < j.r:
                        j.remove()

    def main_render(self):
        self.screen.fill(BLACK)
        for i in self.balls:
            i.render(self.screen)

    def start(self):

        for i in range(0, 5):
            self.balls.append(Ball(self))
        print(self.balls)

        clock = pygame.time.Clock()

        while self.run:
            clock.tick(FPS)
            self.handle_events()
            if len(self.balls) == 0:
                self.run = False
            for i in self.balls:
                i.move()
            self.main_render()
            pygame.display.update()




screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game1 = Game(screen1, "geroin")
