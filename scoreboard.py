from turtle import Turtle
ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 25, 'normal')
GAME_OVER_FONT = ('Courier', 50, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('orange')
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 10
        # self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
