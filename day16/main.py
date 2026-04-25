# from turtle import Screen, Turtle

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("purple")
# timmy.forward(100)
# my_screen.bgcolor("black")
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("name", ["p1", "p2", "p3"])
table.add_column("type", ["fire", "electric", "water"])

print(table)
