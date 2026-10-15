from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.snake_up,"Up")
screen.onkey(snake.snake_down,"Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.snake_move()

screen.exitonclick()