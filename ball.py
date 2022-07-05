from turtle import Turtle
import random

random_start = random.randint(0, 1)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        if random_start == 1:
            new_y = self.ycor() - self.y_move
            new_x = self.xcor() + self.x_move
            self.goto(new_x, new_y)
        else:
            new_y = self.ycor() - self.y_move
            new_x = self.xcor() - self.x_move
            self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.y_move *= -1
        self.x_move *= -1
        self.goto(0, 0)

    def increase_speed(self):
        self.move_speed *= 0.9
