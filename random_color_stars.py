from turtle import *
from random import randint


def drawStar(x, y):
    pu()
    goto(x, y)
    pd()
    colormode(255)
    # set heading: 0
    seth(0)
    for i in range(5):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        pencolor(r, g, b) 
        fd(40)
        rt(144)


hideturtle()
for x in range(0, 250, 50):
    drawStar(x, 0)

done()
