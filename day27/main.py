import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.config(background="black")
window.config(padx=20, pady=20)

# window.minsize(width=500, height=300)


def btn_click():
    value = input.get()
    print(value)
    my_label.config(text=f"{value}")


# label

my_label = tkinter.Label(
    text="Label", fg="blue", bg="black", font=("Arial", 24, "bold")
)
my_label.grid(column=0, row=0)

# button

button = tkinter.Button(text="click me", background="purple", command=btn_click)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="click me", background="purple", command=btn_click)
new_button.grid(column=2, row=0)

# entry

input = tkinter.Entry(foreground="blue")
input.grid(column=3, row=2)


window.mainloop()
