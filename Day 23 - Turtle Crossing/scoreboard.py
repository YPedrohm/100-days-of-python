from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.write_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.goto(-280, 250)
        self.clear()
        self.color("black")
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(-80, 0)
        self.color("red")
        self.write("Game Over!", font=FONT)

