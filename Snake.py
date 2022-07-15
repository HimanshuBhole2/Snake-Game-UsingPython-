import turtle
from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.list_turtle = []
        self.create_snake()
        self.head = self.list_turtle[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position)


    def add_segments(self,position):
        new_turtle = Turtle()
        new_turtle.shape("square")
        # new_turtle.shapesize(1.1)
        new_turtle.fillcolor("white")
        new_turtle.goto(position)
        self.list_turtle.append(new_turtle)

    def extend_snake(self):
        self.add_segments(self.list_turtle[-1].position())


    def move(self):
        for one_shape in range(len(self.list_turtle) - 1, 0, -1):
            new_x = self.list_turtle[one_shape - 1].xcor()
            new_y = self.list_turtle[one_shape - 1].ycor()
            self.list_turtle[one_shape].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    def reset(self):
        for segements in self.list_turtle:
            segements.goto(1000,1000)
        self.list_turtle.clear()
        self.create_snake()
        self.head = self.list_turtle[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)