import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
            random_chance = random.randrange(1, 6)
            if random_chance == 1:
                car = Turtle()
                car.shape("square")
                car.color(random.choice(COLORS))
                car.penup()
                car.shapesize(stretch_wid=1, stretch_len=2)
                car.goto(300, random.randrange(-230, 230))
                self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            new_y = car.ycor()
            car.goto(new_x, new_y)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
