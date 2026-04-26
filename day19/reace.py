import random
import turtle as t

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="which turtle will win the race? choose color: "
)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
turtles = []

c = -150
for i in colors:
    new_tim = t.Turtle("turtle")
    new_tim.color(i)
    new_tim.penup()
    new_tim.goto(x=-250, y=c)
    turtles.append(new_tim)
    c += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won!, the {winning_color} turtle is the winner")
                is_race_on = False
            else:
                print(f"you lost!, the {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
