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

number_of_particles = 4
steps_of_time_number = 500
V = 20 # скорость частицы

pool = [turtle.Turtle(shape = 'turtle') for i in range(number_of_particles)]

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
                unit.forward(V)
            else:
                # удар об вертик. стенки
                unit.setheading(-unit.heading())
                unit.speed(0)
                unit.forward(V)
        else:
            unit.setheading(180 - unit.heading()) # удар об горизонт. стенки
            #A[pool.index(unit)] = 360 -2*A[pool.index(unit)]
            unit.speed(0)
            unit.forward(V)
            # реализовать поворот
