from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scorecard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Scorecard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    snake.move()

    ## collision with food
    if snake.head.distance(food) < 15:
        scorecard.update()
        snake.extend()
        food.refresh()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scorecard.game_over()

    # detect collision in tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scorecard.game_over()
    

screen.exitonclick()
