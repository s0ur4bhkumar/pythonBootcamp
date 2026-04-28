from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.score = 0
        self.color("blue")
        self.Increment_score()

    def Increment_score(self):
        self.clear()
        top_height = self.screen.window_height() / 2.5
        self.setpos(0, top_height)
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            False,
            align="center",
            font=("arial", 20, "bold"),
        )
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.Increment_score()

    # def game_over(self):
    # self.goto(0,0)
    # self.write("Game over", False, align="center", font=("arial", 20, "bold"))
