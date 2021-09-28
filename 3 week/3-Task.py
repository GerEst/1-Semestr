import turtle
#поверхность
turtle.penup()
turtle.goto(400,0)
turtle.pendown()
turtle.goto(-400,0)
#закон движения
t = 0
Vx = 7
Vy = 20
x = -400
y = 0
a = -2
dt = 1

#отскоки, замедлене
while t < 100:
    x += Vx*dt
    y += Vy*dt +a*dt**2
    Vy += a*dt
    turtle.goto(x, y)
    if y <= 0:
        Vy = -Vy
        turtle.goto(x, y)
    t+=1
