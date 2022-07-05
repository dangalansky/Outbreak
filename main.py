import time

from bricks import Brick
from paddle import Paddle
from ball import Ball
from turtle import Screen

# Screen set-up
screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor('black')
screen.title('Outbreak!')
screen.tracer(0)

# create bricks
x = -250
y = 350
colors = ['white', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
for n in range(4):
    for n in range(8):
        brick = Brick(colors[n], (x, y))
        x += 70
    colors.reverse()
    x = -250
    y -= 30
    for n in range(8):
        brick = Brick(colors[n], (x, y))
        x += 70
    colors.reverse()
    x = -250
    y -= 30

# create paddle
paddle = Paddle((0, -330))

# create ball
ball = Ball()

# enable keys
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

# game start
game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    if ball.distance(paddle) < 50 and ball.ycor() < -300:
        ball.bounce_y()
        ball.increase_speed()

    if ball.distance(brick) < 50:
        ball.bounce_y()
        brick.()


screen.exitonclick()
