from turtle import Turtle

MOVE_DISTANCE = 20
UPPER_LIMIT = 250
LOWER_LIMIT = -250

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y <= UPPER_LIMIT:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y >= LOWER_LIMIT:
            self.goto(self.xcor(), new_y)
