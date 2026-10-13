import random
import turtle
from turtle import Turtle

colors_list = [
    (199, 175, 117), (125, 36, 24), (187, 158, 51),
    (170, 104, 56), (5, 57, 83), (200, 216, 204),
    (108, 67, 85), (39, 36, 35), (86, 142, 59),
    (20, 122, 176), (110, 161, 175), (75, 39, 47),
    (9, 67, 47), (64, 153, 137), (133, 41, 43),
    (184, 98, 80), (179, 201, 186), (209, 200, 115),
    (179, 174, 177), (151, 176, 165), (93, 142, 156),
    (28, 80, 59), (194, 190, 192), (17, 78, 99),
    (212, 184, 174), (142, 117, 123), (175, 198, 204)
]

screen = turtle.Screen()
screen.colormode(255)

pet = Turtle()
pet.speed(0)
pet.hideturtle()

start_x = -225
start_y = -225

def draw():
    for i in range(10):
        pet.dot(20, random.choice(colors_list))
        if i < 9:
            pet.penup()
            pet.forward(50)
            pet.pendown()

for j in range(10):
    pet.penup()
    pet.goto(start_x, start_y)
    pet.pendown()
    draw()
    start_y += 50

screen.exitonclick()
