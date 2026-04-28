import time
import turtle as t

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle()
l_paddle = Paddle(co_ord=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.up, "d")
screen.onkey(l_paddle.down, "f")
screen.onkey(r_paddle.up, "k")
screen.onkey(r_paddle.down, "j")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.collided():
        ball.bounce_y()

    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_score_increment()
        print("R lost")
        ball.setpos(0, 0)
        ball.bounce_x()
    if ball.xcor() < -380:
        scoreboard.r_score_increment()
        print("L lost")
        ball.setpos(0, 0)
        ball.bounce_x()

screen.exitonclick()
