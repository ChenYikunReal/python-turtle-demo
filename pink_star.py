import turtle


def drawFivePointStar(t, x, y, lengthOfSide):
    # 从(x, y)向东南方向出发
    t.up()
    t.goto(x, y)
    t.left(36)
    t.down()
    for i in range(5):
        t.forward(lengthOfSide)
        # 144 = 180 - 36
        t.left(144)


myTurtle = turtle.Turtle()
myTurtle.hideturtle()
myTurtle.color("deeppink")
myWindow = myTurtle.getscreen()
lengthOfSide = 200
drawFivePointStar(myTurtle, 0, 0, lengthOfSide)
myWindow.exitonclick()
