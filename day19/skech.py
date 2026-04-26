import turtle as t

tim = t.Turtle()
screen = t.Screen()
screen.bgcolor("black")
tim.hideturtle()
tim.pencolor("blue")


def forward():
    tim.forward(100)


def backward():
    tim.backward(100)


def left():
    tim.left(90)
    tim.forward(100)


def right():
    tim.right(90)
    tim.forward(100)


screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")


screen.listen()
screen.exitonclick()
