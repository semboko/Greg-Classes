import turtle

SIZE = 200
TURN = True
OCCUPIED_CELLS = dict()
WINNER = None

turtle.speed(0)
turtle.width(10)


def draw_line(start_x, start_y, length):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.forward(length)


turtle.color("grey")
draw_line(-1.5 * SIZE, 0.5 * SIZE, 3 * SIZE)
draw_line(-1.5 * SIZE, -.5 * SIZE, 3 * SIZE)

turtle.right(90)

draw_line(-.5 * SIZE, 1.5 * SIZE, 3 * SIZE)
draw_line(.5 * SIZE, 1.5 * SIZE, 3 * SIZE)

turtle.left(90)


def draw_cross(x, y):
    turtle.color("blue")
    turtle.right(45)
    draw_line(x - .4 * SIZE, y + .4 * SIZE, 1.13 * SIZE)
    turtle.right(90)
    draw_line(x + .4 * SIZE, y + .4 * SIZE, 1.13 * SIZE)
    turtle.left(135)


def draw_circle(x, y):
    turtle.color("red")
    turtle.penup()
    turtle.goto(x, y - 0.4 * SIZE)
    turtle.pendown()
    turtle.circle(0.4 * SIZE)


def is_outside(x, y):
    if x > 1.5 * SIZE:
        return True
    if x < -1.5 * SIZE:
        return True
    if y > 1.5 * SIZE:
        return True
    if y < -1.5 * SIZE:
        return True
    return False


def detect_vertical(x, y):
    if x > 0.5 * SIZE:
        return 1
    if x < -0.5 * SIZE:
        return -1
    return 0


def detect_horizontal(x, y):
    if y > 0.5 * SIZE:
        return 1
    if y < -.5 * SIZE:
        return -1
    return 0


def detect_winner():
    global WINNER
    a = -1
    while a <= 1:
        column = (
            OCCUPIED_CELLS.get((a, 1)),
            OCCUPIED_CELLS.get((a, 0)),
            OCCUPIED_CELLS.get((a, -1)),
        )

        row = (
            OCCUPIED_CELLS.get((1, a)),
            OCCUPIED_CELLS.get((0, a)),
            OCCUPIED_CELLS.get((-1, a)),
        )

        if None not in column and len(set(column)) == 1:
            turtle.right(90)
            draw_line(a * SIZE, 1.5 * SIZE, 3 * SIZE)
            WINNER = column[0]

        if None not in row and len(set(row)) == 1:
            draw_line(-1.5 * SIZE, a * SIZE, 3 * SIZE)
            WINNER = row[0]

        a = a + 1

    left_diag = (
        OCCUPIED_CELLS.get((-1, 1)),
        OCCUPIED_CELLS.get((0, 0)),
        OCCUPIED_CELLS.get((1, -1))
    )

    right_diag = (
        OCCUPIED_CELLS.get((1, 1)),
        OCCUPIED_CELLS.get((0, 0)),
        OCCUPIED_CELLS.get((-1, -1)),
    )

    if None not in left_diag and len(set(left_diag)) == 1:
        turtle.right(45)
        draw_line(-1.5 * SIZE, 1.5 * SIZE, 4.24 * SIZE)
        WINNER = left_diag[0]

    if None not in right_diag and len(set(right_diag)) == 1:
        turtle.right(135)
        draw_line(1.5 * SIZE, 1.5 * SIZE, 4.24 * SIZE)
        WINNER = right_diag[0]


def click_handler(x, y):
    global TURN

    if WINNER is not None:
        return

    if is_outside(x, y):
        return

    h = detect_horizontal(x, y)
    v = detect_vertical(x, y)

    cell = (v, h)
    if cell in OCCUPIED_CELLS:
        return

    OCCUPIED_CELLS[cell] = TURN
    print(OCCUPIED_CELLS)

    if TURN is True:
        draw_cross(v * SIZE, h * SIZE)
        TURN = False
    else:
        draw_circle(v * SIZE, h * SIZE)
        TURN = True

    detect_winner()


turtle.onscreenclick(click_handler)
turtle.done()
