import turtle


turtle.speed(1)
turtle.color("red")
turtle.width(10)
turtle.shape("turtle")


def draw_nshape(x, y, corners):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    x = 0
    while x < corners:
        turtle.forward(100)
        turtle.left(360/corners)
        x = x + 1


draw_nshape(150, 200, 3)
draw_nshape(-150, 100, 4)
draw_nshape(-150, -200, 5)

draw_nshape(0, 0, 1)

turtle.done()
