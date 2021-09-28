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

number_of_particles = 1
steps_of_time_number = 500
spped = 5 # скорость частицы

pool = [turtle.Turtle(shape = 'circle') for i in range(number_of_particles)]

# генерируем координаты частиц
Xc = [] # x koordinata
Yc = [] # y koordinata
A  = [] # ugol dvizenija

for unit in pool:
    unit.penup()
    unit.speed(50)
    x = randint(-200, 200)
    y = randint(-200, 200)
    Xc.append(x)
    Yc.append(y)
    unit.goto(x,y)
    alpha = randint(-180, 180)
    unit.right(alpha)
    A.append(alpha)

print(Xc)
print(Yc)
print(A)

turtle.tracer()

for i in range(steps_of_time_number):
    for unit in pool:
        if abs(unit.xcor()) <= 200:
            if abs(unit.ycor()) <= 200:
                unit.speed(0)
                unit.forward(3)
            else:
                unit.right(360 - 2*A[pool.index(unit)]) # удар об y
                #A[pool.index(unit)] = 180 - 2*A[pool.index(unit)]
                unit.speed(0)
                unit.forward(3)
        else:
            unit.right(180 - 2*A[pool.index(unit)]) # удар об x
            #A[pool.index(unit)] = 360 -2*A[pool.index(unit)]
            unit.speed()
            unit.forward(3)
            # реализовать поворот
