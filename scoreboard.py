from turtle import Turtle

SCORE_1 = 0
SCORE_2 = 0
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.player1_score()
        self.score1 = 0
        self.score2 = 0



    def player1_score(self):
        self.score1 = SCORE_1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-300, 300)
        self.write(f"score: {self.score1}", align = "left", font = ("Arial",20, "normal"))

        return self.score1

    def calc_p1(self):
        global SCORE_1
        SCORE_1 += 1
        self.clear()
        self.player1_score()


    def player2_score(self):
        self.score2 = SCORE_2
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(300, 300)
        self.write(f"score: {self.score2}", align="right", font=("Arial", 20, "normal"))

        return self.score2

    def calc_p2(self):
        global SCORE_2
        SCORE_2 += 1
        self.clear()
        self.player2_score()


