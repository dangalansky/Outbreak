import time
import random
from board import ScoreBoard
from bricks import Brick
from paddle import Paddle
from ball import Ball
from turtle import Turtle, Screen


def game_start():
    # Screen set-up
    screen = Screen()
    screen.clear()
    screen.setup(width=1000, height=800)
    screen.bgcolor('black')
    screen.title('Outbreak!')
    screen.tracer(0)

    # Scoreboard

    board = ScoreBoard()

    # Draw Border
    border = Turtle(shape='square')
    border.turtlesize(.25, .25)
    border.color('green')
    border.width(7)
    border.penup()
    border.goto(-280, -360)
    border.pendown()
    for _ in range(2):
        border.forward(570)
        border.left(90)
        border.forward(730)
        border.left(90)

    # create list of bricks
    bricks = []
    colors = ['white', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
    for i in range(48):
        brick = Brick(random.choice(colors))
        bricks.append(brick)

    print(len(bricks))

    # place bricks:
    x = -240
    y = 370
    for brick in bricks:
        if bricks.index(brick) % 8 == 0:
            x = -240
            y -= 30
        brick.goto(x, y)
        x += 70





    # create bricks
    # x = -250
    # y = 350
    # colors = ['white', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
    # for n in range(4):
    #     for n in range(8):
    #         brick = Brick(colors[n], (x, y))
    #         x += 70
    #     colors.reverse()
    #     x = -250
    #     y -= 30
    #     for n in range(8):
    #         brick = Brick(colors[n], (x, y))
    #         x += 70
    #     colors.reverse()
    #     x = -250
    #     y -= 30

    # brick = Brick('red')
    # brick.goto(-240, 350)

    # create paddle
    paddle = Paddle((0, -300))

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

        if ball.xcor() > 255 or ball.xcor() < -265:
            ball.bounce_x()

        if ball.ycor() > 350:
            ball.bounce_y()

        if ball.distance(paddle) < 80 and ball.ycor() < -280:
            ball.bounce_y()

        if ball.ycor() < -350:
            game_on = False
            board.game_over()
            screen.onkey(game_start, "n")
            screen.onkey(screen.bye, "q")

        if ball.distance(brick) < 10:
            bricks.remove(brick)
            ball.bounce_y()

    screen.exitonclick()


game_start()
