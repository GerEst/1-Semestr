import turtle
from random import *
i = 0
while i < 300:
    go = random()
    angle = randint(-180, 180)
    turtle.speed(0)
    turtle.right(angle)
    turtle.forward(50*go)
    i+=1
while i < 300:
    a = random()
    b = random()
    turtle.speed(0)
    turtle.goto(a, b)
    i+=1
    
