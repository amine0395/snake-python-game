import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.75,stretch_wid=0.75)
        self.penup()
        self.goto(random.randint(-200,200),random.randint(-200,200))
        self.color("Red")
    def tp(self):
        self.goto(random.randint(-200,200),random.randint(-200,200))