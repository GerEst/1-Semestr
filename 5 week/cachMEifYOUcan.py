import pygame
from Ball import *
from Constantine import *
from random import randint

class Game():
    '''
    Основной класс игры
    balls - список с шарами
    counter - счёт удалённых шаров
    self.start() - запускает игру при инициализации объекта класса
    '''
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.counter = 0
        self.run = True
        self.balls = []
        self.start()

    def handle_events(self):
        '''
        Метод класса Game
        Обработка событий
        Удаляет шар после клика в его области
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for j in self.balls:
                    if abs(event.pos[0] - j.x) < j.r and abs(event.pos[1] - j.y) < j.r:
                        self.counter += 1
                        j.remove()

    def main_render(self):
        '''
        Создание экрана и отрисовка каждого из шаров
        '''
        self.screen.fill(BLACK)
        for i in self.balls:
            i.render(self.screen)

    def start(self):
        '''
        создание шаров
        основной цикл программы
        '''

        for i in range(0, randint(0, 15)):
            self.balls.append(Ball(self))

        clock = pygame.time.Clock()

        while self.run:
            clock.tick(FPS)
            self.handle_events()
            if len(self.balls) == 0:
                self.run = False
                print(f"вы набрали {self.counter} очков")
            for i in self.balls:
                i.move()
            self.main_render()
            pygame.display.update()

screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game1 = Game(screen1, "bbballs")
