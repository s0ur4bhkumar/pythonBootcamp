from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, co_ord=(350, 0)):
        super().__init__()
        self.co_ord = co_ord
        self.penup()
        self.shape("square")
        self.color("purple")
        self.setpos(co_ord)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.co_ord[0], y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.co_ord[0], y)
    
