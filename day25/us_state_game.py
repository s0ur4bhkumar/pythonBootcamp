import turtle

import pandas as pd

states = pd.read_csv("./day25/50_states.csv")
score = 0

screen = turtle.Screen()
screen.title("U.S States Game")
screen.bgcolor("black")
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

image = "./day25/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title="Guess the state", prompt=f"what's another state name {score}/50"
    )
    if answer_state:
        answer_state = answer_state.title()
        if answer_state == "Exit":
            break
        elif answer_state in states["state"].to_list():
            state_data = states[states.state == answer_state]
            x = state_data.x.item()
            y = state_data.y.item()
            pen.goto(x, y)
            pen.write(answer_state, align="left", font=("arial", 6, "bold"))
            if answer_state not in guessed_state:
                guessed_state.append(answer_state)
                score += 1

remaining_state = [
    state for state in states["state"].to_list() if state not in guessed_state
]

states_to_learn = pd.DataFrame(remaining_state)
states_to_learn.to_csv("./day25/states_to_learn.csv")

turtle.mainloop()
