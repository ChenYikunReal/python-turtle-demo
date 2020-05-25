import turtle


def koch(len, n):
    if n == 0:
        turtle.fd(len)
    else:
        for i in [0, 60, -120, 60]:
            turtle.left(i)
            koch(len/3, n-1)


level = int(input())


def main():
    turtle.penup()
    turtle.goto(-250, 150)
    turtle.pensize(2)
    turtle.color('orange')
    turtle.pendown()
    koch(500, level)
    turtle.right(120)
    koch(500, level)
    turtle.right(120)
    koch(500, level)
    turtle.right(120)
    turtle.hideturtle()
    turtle.done()


main()
