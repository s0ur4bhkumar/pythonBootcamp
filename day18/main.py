import random
import turtle

import colorgram

color = colorgram.extract("day18/art.jpg", 30)

color_list = [(i.rgb.r, i.rgb.g, i.rgb.b) for i in color]

turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor("black")
timmy = turtle.Turtle()
timmy.color("purple")
timmy.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)

    return color


# def dashed_line():

#     for i in range(10):
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()


# for i in range(4):
#     dashed_line()
#     timmy.right(90)
def polygons():
    for i in range(3, 11):
        timmy.pencolor(random_color())
        for _ in range(i):
            timmy.right(360 / i)
            timmy.forward(100)


def random_walk():
    for i in range(50):
        timmy.pensize(5)
        timmy.pencolor(random_color())
        timmy.forward(50)
        timmy.setheading(random.choice([0, 90, 180, 270]))


def spiral():
    for i in range(50):
        timmy.pencolor(random_color())
        timmy.speed("fastest")
        timmy.circle(100)
        timmy.left(i)


def art():
    timmy.ht()
    for i in range(1, 10):
        timmy.penup()
        timmy.setposition(0, i * 30)
        for _ in range(1, 11):
            timmy.pendown()
            timmy.speed("fastest")
            timmy.dot(20, random.choice(color_list))
            timmy.penup()
            timmy.forward(30)


art()

screen.exitonclick()
