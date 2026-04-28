import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars: list[Turtle] = []
        self.car_speed = MOVE_INCREMENT

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=4)
            car.color(random.choice(COLORS))
            car.setpos(-250, random.randint(-230, 230))

            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
