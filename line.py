from turtle import Turtle


class Line(Turtle):
    def __init__(self, y):
        super(Line, self).__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=0.2, stretch_wid=0.9)
        self.penup()
        self.goto(0, y)
