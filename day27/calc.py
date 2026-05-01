import tkinter

window = tkinter.Tk()
window.config(background="black")
window.config(padx=100, pady=100)


def calculate():
    miles = int(entry.get())
    result_label.config(text=f'{round(miles*1.6,2)}')
    return ""


entry = tkinter.Entry()
entry.grid(column=1, row=0)

entry_label = tkinter.Label(
    text="Miles", foreground="blue", background="black", font=("arial", 15, "normal")
)
entry_label.grid(column=2, row=0)

equal = tkinter.Label(
    text="is equal to",
    foreground="blue",
    background="black",
    font=("arial", 15, "normal"),
)
equal.grid(column=0, row=2)

result_label = tkinter.Label(
    text="", background="black", foreground="blue", font=("arial", 15, "normal")
)
result_label.grid(column=1, row=2)


km_label = tkinter.Label(
    text="KM", background="black", foreground="blue", font=("arial", 15, "normal")
)
km_label.grid(column=2, row=2)

button = tkinter.Button(text="calulate", command=calculate)
button.grid(column=1, row=4)

window.mainloop()
