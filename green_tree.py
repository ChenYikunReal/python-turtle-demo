from turtle import *


# 递归绘制一棵树
def tree(branchLength, turtle):
    if branchLength > 5:
        turtle.forward(branchLength)
        turtle.right(20)
        tree(branchLength-15, turtle)
        turtle.left(40)
        tree(branchLength-10, turtle)
        turtle.right(20)
        turtle.backward(branchLength)


myTurtle = Turtle()
myWindow = myTurtle.getscreen()
myTurtle.left(90)
myTurtle.up()
myTurtle.backward(300)
myTurtle.down()
myTurtle.color('green')
tree(110, myTurtle)
