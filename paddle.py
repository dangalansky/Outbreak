from turtle import Turtle


class Paddle(Turtle):
    # create paddle from Turtle class
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)

    # enable paddle movement along x-axis
    def go_left(self):
        if self.xcor() > -240:
            new_x = self.xcor() - 40
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 240:
            new_x2 = self.xcor() + 40
            self.goto(new_x2, self.ycor())
