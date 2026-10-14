from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("#202020")
user_bet = screen.textinput("Make your bet", "Which turtle will win the race?  Enter a color: ")
colors = ["red", "yellow", "green", "blue", "purple", "orange"]
all_turtles = []

x = -230
y = - 100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 40

if user_bet:
    user_bet = user_bet.lower()
    if user_bet in colors:
        is_race_on = True
    else:
        print("Invalid color! Please restart and choose a valid color!")

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break

screen.exitonclick()