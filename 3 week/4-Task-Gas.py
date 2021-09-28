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
steps_of_time_number = 300
spped = 5 # скорость частицы

pool = [turtle.Turtle(shape = 'circle') for i in range(number_of_particles)]

# генерируем координаты частиц
Xc = []
Yc = []
A  = []

for unit in pool:
    unit.penup()
    unit.speed(50)
    x = randint(-200, 200)
    y = randint(-200, 200)
    Xc.append(x)
    Yc.append(y)
    unit.goto(x,y)
    alpha = randint(-180 , 180)
    unit.right(alpha)
    A.append(alpha)

print(Xc)
print(Yc)
print(A)

for i in range(steps_of_time_number):
    for unit in pool:
        if abs(unit.xcor()) < 200:
            if abs(unit.ycor()) < 200:
                unit.speed(0)
                unit.forward(4)
            else:
                unit.right(90 - 2*A[pool.index(unit)]) #реализовать поворот
                unit.speed(0)
                unit.forward(4)
        else:
            unit.right(180 -2*A[pool.index(unit)]) #реализовать поворот
            unit.speed()
            unit.forward(4)
            # реализовать поворот
