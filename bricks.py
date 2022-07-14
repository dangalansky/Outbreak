from turtle import Turtle


class Brick(Turtle):
    # create brick from Turtle class
    def __init__(self, color):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
