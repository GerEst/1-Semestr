from pygame import draw
from Constantine import *
from random import randint



class Ball:
    '''
    Класс создаёт мишени - шары
    x - x координата
    y - y координата
    r - радиус шара
    Vx - x кмпонента скорости
    Vy - y компонента скорости
    '''
    def __init__(self, game):

        self.game = game

        self.x = randint(100,700)
        self.y = randint(100,500)
        self.r = randint(30,50)

        self.Vx = randint(-10,10)
        self.Vy = randint(-10,10)

        self.color = COLORS[randint(0, 5)]


    def render(self, screen):
        ''' Отрисовка шара '''
        draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        ''' Движение шара '''
        self.x += self.Vx
        self.y += self.Vy

        if self.x + self.r > SCREEN_WIDTH:
            self.Vx = randint(-10, 0)
            self.Vy = randint(-10, 10)

        if self.x - self.r < 0:
            self.Vx = randint(0, 10)
            self.Vy = randint(-10, 10)


        if self.y + self.r > SCREEN_HEIGHT:
            self.Vx = randint(-10, 10)
            self.Vy = randint(-10, 0)
        if self.y - self.r < 0:
            self.Vx = randint(-10, -10)
            self.Vy = randint(0, 10)

    def remove(self):
        '''  удаление шара '''
        self.game.balls.remove(self)
