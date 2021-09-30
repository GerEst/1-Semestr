from random import randint
import turtle

#draw pool
r = 200
turtle.penup()
turtle.goto(-r, r)
turtle.pendown()
zabor = 0
while zabor < 4:
    turtle.forward(2*r)
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
    x = randint(-r, r)
    y = randint(-r, r)
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
        if abs(unit.xcor()) <= r:
            if abs(unit.ycor()) <= r:
                unit.speed(0)
                unit.forward(V)
            else:
                # удар об вертик. стенки
                unit.setheading(-unit.heading())
                unit.speed(0)
                unit.forward(V)
        else:
            unit.setheading(180 - unit.heading()) 
            unit.speed(0)
            unit.forward(V)
