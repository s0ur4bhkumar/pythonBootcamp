import calendar
import datetime as dt
import random
import smtplib

my_email = "smpt2358@gmail.com"
password = "alif nuga lssa abya"

with open("./day32/quotes.txt") as data:
    quotes = data.readlines()


now = dt.datetime.now()
date = now.date()
day = calendar.day_name[date.weekday()]

if day == "Sunday":
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="smpt2358@yahoo.com",
            msg=f"subject:quote of the day \n\n {random.choice(quotes)}",
        )
