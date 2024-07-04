import turtle as t

tim = t.Turtle()
screen = t.Screen()
tommy = t.Turtle()

def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def clear():
    tim.reset()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
