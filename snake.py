from turtle import  Turtle, Screen
positions = [(0, 0), (-20, 0), (-40, 0)]
step=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
        for index in positions:
            new_segment=Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(index)
            self.segments.append(new_segment)


    def more(self):
        new_segment=Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(positions[len(positions)-1])
        self.segments.append(new_segment)
    def move(self):
            for i in range(len(self.segments)-1, 0, -1):
                x=self.segments[i-1].xcor()
                y=self.segments[i-1].ycor()
                self.segments[i].goto(x,y)
            self.segments[0].forward(step)
    def up(self):
      if self.segments[0].heading() !=270:
        self.segments[0].setheading(90)
    def down(self):
      if self.segments[0].heading() != 90:
        self.segments[0].setheading(270)
    def left(self):
      if self.segments[0].heading() != 0:
        self.segments[0].setheading(180)
    def right(self):
      if self.segments[0].heading() != 180:
        self.segments[0].setheading(0)

