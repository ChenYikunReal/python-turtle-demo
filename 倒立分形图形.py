import turtle


def fractal(myTurtle, x1, y1, x2, y2, level):
    # 从(x1, y1)坐标画到(x2, y2)坐标
    newX = 0
    newY = 0
    if level == 0:
        drawLine(myTurtle, x1, y1, x2, y2)
    else:
        newX = (x1+x2)/2 + (y2-y1)/2
        newY = (y1+y2)/2 - (x2-x1)/2
        fractal(myTurtle, x1, y1, newX, newY, level-1)
        fractal(myTurtle, newX, newY, x2, y2, level-1)


def drawLine(myTurtle, x1, y1, x2, y2):
    # 绘制从(x1, y1)到(x2, y2)的线
    myTurtle.up()
    myTurtle.goto(x1, y1)
    myTurtle.down()
    myTurtle.goto(x2, y2)


t = turtle.Turtle()
myWindow = t.getscreen()
t.hideturtle()
# 最快速度
t.speed(0)
level = 12
fractal(t, -80, 60, 80, 60, level)
# 窗口不会自动关闭
myWindow.exitonclick()

