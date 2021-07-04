from turtle import Turtle
ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 20, 'normal')
GAME_OVER_FONT = ('Courier', 30, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as data:
            self.high_score = int(data.read())
        self.color('violet')
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 10
        self.update_score()

    def score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Your Final Score: {self.score}", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -40)
        self.write(arg=f"Click on screen to exit.", align=ALIGNMENT, font=GAME_OVER_FONT)

        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as data:
                data.write(str(self.high_score))
