from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Draconian Typewriter', 18)


class ScoreBoard(Turtle):
    # create scoreboard object from Turtle class
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('hi_score.txt') as data_file:
            self.hi_score = int(data_file.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(390, 250)
        self.update_scoreboard()

    # update score
    def update_scoreboard(self):
        self.clear()
        self.goto(390, 250)
        self.write(arg=f'hi score: {self.hi_score}\n\nscore: {self.score}', align=ALIGNMENT, font=FONT)

    # prints game over, highscore if highscore achieved
    def game_over(self, highscore):
        if highscore:
            x = "NEW HIGH SCORE!"
        else:
            x = ""
        self.goto(0, 0)
        self.write(arg=f'GAME OVER!{x}\n\nPress "n" for New Game!\nPress "q" to Quit.', align='center', font=FONT)

    # prints game win, if game won
    def won_game(self):
        self.goto(0, 0)
        self.write(arg='CONGRATS YOU WIN THE GAME!\nPress "n" for New Game!\nPress "q" to Quit.', align='center',
                   font=FONT)
