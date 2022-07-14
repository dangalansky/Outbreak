import time
from board import ScoreBoard
from level_up import Level
from bricks import Brick
from paddle import Paddle
from ball import Ball
from turtle import Turtle, Screen


def game_start():
    # Screen set-up
    screen = Screen()
    screen.clear()
    screen.setup(width=1000, height=800)
    screen.bgpic('turtle fling.gif')
    screen.title('Turtle Fling!')
    screen.tracer(0)

    # Scoreboard, Level
    board = ScoreBoard()
    level = Level()

    # Draw Border
    border = Turtle(shape='square')
    border.turtlesize(.25, .25)
    border.color('yellow')
    border.width(7)
    border.penup()
    border.goto(-280, -360)
    border.pendown()
    for _ in range(2):
        border.forward(570)
        border.left(90)
        border.forward(730)
        border.left(90)

    # place bricks:
    bricks = []
    colors = ['white', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
    num_bricks = 8

    def build_wall():
        for i in range(num_bricks):
            brick = Brick('red')
            bricks.append(brick)
        x = -240
        y = 350
        for brick in bricks:
            if bricks.index(brick) % 8 == 0:
                x = -240
                y -= 30
            brick.goto(x, y)
            x += 70

    build_wall()

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
        # set wall boundaries, enable x-bounce
        if ball.xcor() > 265 or ball.xcor() < -265:
            ball.bounce_x()
        # enable y-bounce off top wall
        if ball.ycor() > 350:
            ball.bounce_y()
        # enable turtle bounce off paddle
        if ball.distance(paddle) < 50 and ball.ycor() < -270:
            ball.bounce_y()
        # game over if turtle passes paddle
        if ball.ycor() < -350:
            game_on = False
            # high score re-write, if high score achieved
            if board.score > board.hi_score:
                highscore = True
                board.hi_score = board.score
                with open('hi_score.txt', mode='w') as data_file:
                    data_file.write(str(board.hi_score))
            else:
                highscore = False
            # write game over, enable user to quit or restart
            board.game_over(highscore)
            screen.onkey(game_start, "n")
            screen.onkey(screen.bye, "q")
        # remove bricks if turtle hits, add one point per brick
        for brick in bricks:
            if ball.distance(brick) < 30:
                board.score += 1
                board.update_scoreboard()
                ball.bounce_y()
                brick.hideturtle()
                bricks.remove(brick)
            # if no bricks, next level!
            if len(bricks) == 0:
                level.level += 1
                level.update_level()
                num_bricks += 8
                # last level!
                if num_bricks > 128:
                    game_on = False
                    board.won_game()
                    screen.onkey(game_start, "n")
                    screen.onkey(screen.bye, "q")
                else:
                    build_wall()
                    ball.reset_position()

    screen.exitonclick()


game_start()
