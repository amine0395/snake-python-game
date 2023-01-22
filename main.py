import score
from food import  Food
import random
from turtle import Screen
from snake import Snake
from score import Scoreboard
import time
screen= Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("snake project")
screen.tracer(0)
snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_on = True
scoreboard.up()
while game_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    if snake.segments[0].xcor()>=300 or snake.segments[0].xcor()<=-300 or snake.segments[0].ycor()>=300 or snake.segments[0].ycor()<=-300:
        print("GAME OVER")
        game_on=False
    if snake.segments[0].distance(food)<15:
        scoreboard.up()
        food.tp()
        snake.more()
    for segment in snake.segments:
      if snake.segments[0].distance(segment)<10 and segment!=snake.segments[0]:
        print("GAME OVER")
        game_on = False
screen.exitonclick()