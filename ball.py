from turtle import Turtle
import random

random_start = random.randint(0, 1)


class Ball(Turtle):
    # create Turtle Ball object from Turtle Class
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.left(90)
        self.color('green')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    # how Turtle moves
    def move(self):
        if random_start == 1:
            new_y = self.ycor() - self.y_move
            new_x = self.xcor() + self.x_move
            self.goto(new_x, new_y)
        else:
            new_y = self.ycor() - self.y_move
            new_x = self.xcor() - self.x_move
            self.goto(new_x, new_y)

    # how Turtle bounces
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    # reset Turtle position and increase speed
    def reset_position(self):
        self.move_speed *= .75
        self.goto(0, -300)
