from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.color("white")
        self.goto(0,265)
        self.hideturtle()
    def up(self):
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
        self.score += 1

