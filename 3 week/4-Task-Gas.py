from random import randint
import turtle

#draw pool
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
zabor = 0
while zabor < 4:
    turtle.forward(400)
    turtle.right(90)
    zabor += 1
turtle.ht()

number_of_particles = 5
steps_of_time_number = 100


pool = [turtle.Turtle(shape='circle') for i in range(number_of_particles)]

for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.speed(50)
        unit.goto(randint(-200, 200), randint(-200, 200))
