import turtle
from turtle import Screen
import time
from Snake import Snake
from food import Food
from scorrboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
#screen.bgpic("wall.jpg")
screen.title("MY NEW SNAKE GAME")
screen.tracer(0)
snake = Snake()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)


food = Food()

insem = True
while insem == True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    for segments in snake.list_turtle[1::]:
        if snake.head.distance(segments) < 15:
            scoreboard.reset()
            snake.reset()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()
    if snake.head.xcor() > 300 or snake.head.xcor() < (-300) or snake.head.ycor() < (-300) or snake.head.ycor() > (300) :
        scoreboard.reset()
        snake.reset()





screen.exitonclick()