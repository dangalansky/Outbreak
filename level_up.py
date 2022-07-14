from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Draconian Typewriter', 18)


class Level(Turtle):
    # create current level display from Turtle class
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('green')
        self.hideturtle()
        self.penup()
        self.goto(370, -300)
        self.update_level()

    # update level display when bricks are cleared
    def update_level(self):
        self.clear()
        self.goto(370, -300)
        self.write(arg=f'level: {self.level}', align=ALIGNMENT, font=FONT)
