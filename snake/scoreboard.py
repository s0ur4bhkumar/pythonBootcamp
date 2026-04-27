from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("blue")
        self.Increment_score()

    def Increment_score(self):
        self.clear()
        top_height = self.screen.window_height() / 2.5
        self.setpos(0, top_height)
        self.write(
            f"Score: {self.score}", False, align="center", font=("arial", 20, "bold")
        )
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", False, align="center", font=("arial", 20, "bold"))
