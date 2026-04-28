import random
from turtle import Turtle

ANGLES = [30, 45, 60, 75]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("purple")
        self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10

    def collided(self):
        return self.ycor() > 280 or self.ycor() < -280

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
