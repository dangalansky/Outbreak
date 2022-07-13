from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Draconian Typewriter', 18)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # with open('data.txt') as data_file:
        #     self.hi_score= int(data_file.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(350, 300)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(370, 300)
        self.write(arg=f'score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER!\n\nPress "n" for New Game!\nPress "q" to Quit.', align='center', font=FONT)
