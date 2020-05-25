import turtle


def drawSnake(rad, angle, len, neckrad):
    for _ in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.forward(rad/2) 
    turtle.circle(neckrad, 180)
    turtle.forward(rad/4)


turtle.setup(1500, 1400, 0, 0)
turtle.pensize(30)
turtle.pencolor("purple")
turtle.seth(150)
drawSnake(70, 80, 2, 15)
