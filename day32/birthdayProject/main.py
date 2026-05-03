##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import random
import smtplib

import pandas as pd

data = pd.read_csv("./day32/birthdayProject/birthdays.csv")
data_dict = data.to_dict(orient="records")
date = dt.datetime.now()
letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

with open(
    f"./day32/birthdayProject/letter_templates/{random.choice(letter_templates)}"
) as letter_template:
    letter = "".join(letter_template.readlines())


def send_mail(name):
    my_email = "smpt2358@gmail.com"
    password = "alif nuga lssa abya"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="smpt2358@yahoo.com",
            msg=f"subject: Birthday wish \n\n {letter.replace('[NAME]', f'{name}')}",
        )


for i in data_dict:
    if int(i["month"]) == date.month and int(i["day"]) == date.day:
        send_mail(i["name"])
        print('sucess')
    else:
        print('nope')
