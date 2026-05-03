import random
import tkinter as tk

from data_handling import vocabulary

word = random.choice(vocabulary)


def change_word():
    global flip_timer, word
    window.after_cancel(flip_timer)
    canvas.itemconfig(language, text=word["French"], fill="black")
    canvas.itemconfig(head, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip)


def flip():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(head, text="English", fill="white")
    canvas.itemconfig(language, text=word["English"], fill="white")


def is_known():
    vocabulary.remove(word)


# -------------------------ui setup------------------------------------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.config(background=BACKGROUND_COLOR, padx=50, pady=250)
flip_timer = window.after(3000, flip)

canvas = tk.Canvas(
    background=BACKGROUND_COLOR, width=810, height=526, highlightthickness=0
)
card_front = tk.PhotoImage(file="./day31/images/card_front.png")
card_back = tk.PhotoImage(file="./day31/images/card_back.png")
canvas_image = canvas.create_image(410, 260, image=card_front)
head = canvas.create_text(400, 50, text="", font=("arial", 40, "italic"))
language = canvas.create_text(400, 250, text="", font=("arial", 60, "bold"))

right_img = tk.PhotoImage(file="./day31/images/right.png")
right_button = tk.Button(image=right_img, highlightthickness=0, command=change_word)
right_button.grid(column=0, row=1)

wrong_img = tk.PhotoImage(file="./day31/images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong_button.grid(column=1, row=1)

change_word()
canvas.grid(column=0, row=0, columnspan=2)


window.mainloop()
