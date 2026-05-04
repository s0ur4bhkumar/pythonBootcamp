import tkinter as tk
from mimetypes import common_types
from turtle import bgcolor

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=225, pady=375)

        self.canvas = tk.Canvas(height=250, width=500)
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.score = tk.Label(
            text="score:0",
            font=("arial", 15, "bold"),
            fg="white",
            background=THEME_COLOR,
        )
        self.score.grid(column=1, row=0, pady=20)

        self.question = self.canvas.create_text(
            250, 125, width=300, text="lorem ipsum dolor", font=("arial", 15, "italic")
        )

        self.CORRECT = tk.PhotoImage(file="./day34/images/true.png")
        self.INCORRECT = tk.PhotoImage(file="./day34/images/false.png")

        self.correct = tk.Button(
            image=self.CORRECT,
            highlightthickness=0,
            command=self.correct_button_command,
        )
        self.correct.grid(column=0, row=2, pady=20)

        self.incorrect = tk.Button(
            image=self.INCORRECT,
            highlightthickness=0,
            command=self.incorrect_button_command,
        )
        self.incorrect.grid(column=1, row=2, pady=20)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.score.config(text=f"score:{self.quiz.score}")
        else:
            self.canvas.itemconfig(
                self.question, text="You hav reached the end of the quiz"
            )
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")

    def correct_button_command(self):
        answer = self.quiz.check_answer(user_answer="true")
        self.next_question()
        return answer

    def incorrect_button_command(self):
        answer = self.quiz.check_answer(user_answer="false")
        self.next_question()
        return answer

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
