import turtle
from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Classic Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

turtle.listen()
turtle.onkey(snake.up, 'Up')
turtle.onkey(snake.down, 'Down')
turtle.onkey(snake.left, 'Left')
turtle.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) <= 15:
        food.generate_food()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        if screen.textinput(title='Play again', prompt='Yes or No : ').lower() == 'no':
            game_is_on = False
            scoreboard.game_over()
        else:
            snake.snake_reset()
            scoreboard.score_reset()
        screen.listen()  # since the text input screen comes, screen stops listening, so we need to call listen() again

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
            if screen.textinput(title='Continue playing?', prompt='Yes or No? : ').lower() == 'no':
                game_is_on = False
                scoreboard.game_over()
            else:
                snake.snake_reset()
                scoreboard.score_reset()
            screen.listen()

screen.exitonclick()
