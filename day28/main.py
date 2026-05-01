import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(heading, text="Timer", fill=RED)
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        canvas.itemconfig(heading, text="Break", fill=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        canvas.itemconfig(heading, text="Break", fill=PINK)
    else:
        count_down(work_sec)
        canvas.itemconfig(heading, text="Work", fill=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomdoro")
window.config(background="black", padx=200, pady=200, bg=YELLOW)

canvas = tkinter.Canvas(width=500, height=500, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="./day28/tomato.png")
canvas.create_image(250, 250, image=tomato_image)
timer_text = canvas.create_text(
    250, 280, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")
)
heading = canvas.create_text(
    250, 50, text="Timer", fill=GREEN, font=(FONT_NAME, 25, "bold")
)

start = tkinter.Button(window, text="start", background="white", command=start_timer)
start.grid(column=0, row=1)

check = tkinter.Label(
    text="✓", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 50, "bold")
)
check.grid(column=1, row=1)

reset = tkinter.Button(window, text="reset", background="white", command=reset_timer)
reset.grid(column=2, row=1)

canvas.grid(column=1, row=0)


window.mainloop()
