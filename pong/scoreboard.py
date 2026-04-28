from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("arial", 80, "normal"))

    def l_score_increment(self):
        self.l_score += 1
        self.clear()
        self.update()

    def r_score_increment(self):
        self.r_score += 1
        self.clear()
        self.update()
