import json
import random
import tkinter as tk
from tkinter import messagebox

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + number_list + symbol_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_credentials():
    website = website_entry
    email = email_entry
    password = password_entry
    new_data = {website.get(): {"email": email.get(), "password": password.get()}}
    data = None

    if len(website.get()) == 0 or len(password.get()) == 0 or len(email.get()) == 0:
        messagebox.showinfo(title="Empty fields", message="Please fill all fields")
    else:
        try:
            with open("./day29/credential.json", mode="r") as credentials:
                data = json.load(credentials)
        except FileNotFoundError:
            with open("./day29/credential.json", mode="w") as credentials:
                json.dump(new_data, credentials, indent=4)
        else:
            data = json.load(credentials)
            with open("./day29/credential.json", mode="w") as credentials:
                data.update(new_data)
                json.dump(data, credentials, indent=4)
        finally:
            website.delete(0, tk.END)
            email.delete(0, tk.END)
            password.delete(0, tk.END)


# ----------------------------Search--------------------------------------------- #
def Search():
    try:
        with open("./day29/credential.json", mode="r") as credentials:
            data = json.load(credentials)
    except FileNotFoundError:
        messagebox.showinfo(message="file not found")
    else:
        result = data[website_entry.get()]
        messagebox.showinfo(
            message=f"email:{result['email']}\n password:{result['password']}"
        )


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(background="black", padx=225, pady=325)

canvas = tk.Canvas(background="black", width=200, height=200, highlightthickness=0)
canvas.grid(column=1, row=0)
logo = tk.PhotoImage(file="./day29/logo.png")
canvas.create_image(100, 100, image=logo)

website_label = tk.Label(
    text="website: ", fg="cyan", bg="black", font=("arial", 15, "normal")
)
website_label.grid(column=0, row=1)
website_entry = tk.Entry(
    highlightthickness=2,
    highlightbackground="cyan",
    highlightcolor="cyan",
    background="black",
    width=40,
    foreground="cyan",
    insertbackground="cyan",
)
website_entry.grid(column=1, row=1, columnspan=2)
search_btn = tk.Button(
    text="Search",
    highlightbackground="cyan",
    highlightcolor="cyan",
    highlightthickness=0,
    background="black",
    foreground="blue",
    width=13,
    command=Search,
)
search_btn.grid(column=2, row=1)

email_label = tk.Label(
    text="email/username: ", fg="cyan", bg="black", font=("arial", 15, "normal")
)
email_label.grid(column=0, row=2)
email_entry = tk.Entry(
    highlightthickness=2,
    highlightbackground="cyan",
    highlightcolor="cyan",
    background="black",
    width=40,
    foreground="cyan",
    insertbackground="cyan",
)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = tk.Label(
    text="password: ", fg="cyan", bg="black", font=("arial", 15, "normal")
)
password_label.grid(column=0, row=3)
password_entry = tk.Entry(
    highlightthickness=2,
    highlightbackground="cyan",
    highlightcolor="cyan",
    background="black",
    width=23,
    foreground="cyan",
    insertbackground="cyan",
)
password_entry.grid(column=1, row=3)

generate_btn = tk.Button(
    text="Generate Password",
    highlightbackground="cyan",
    highlightcolor="cyan",
    highlightthickness=0,
    background="black",
    foreground="blue",
    width=13,
    command=generate_password,
)
generate_btn.grid(column=2, row=3)

add_btn = tk.Button(
    text="add",
    highlightbackground="cyan",
    highlightcolor="cyan",
    highlightthickness=0,
    foreground="blue",
    background="black",
    width=57,
    command=add_credentials,
)
add_btn.grid(column=0, row=4, columnspan=3)


window.mainloop()
