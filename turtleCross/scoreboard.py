from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setpos(-280, 230)
        self.hideturtle()
        self.color("purple")
        self.write(self.score, align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write("Game Over", align="center", font=FONT)
