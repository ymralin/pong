from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.pu()
        self.ht()
        self.color("white")
        self.location = (0, 0)
        self.score = 0

    def create_score(self):
        self.goto(self.location)
        self.write(self.score, False, align="center", font=("Arial", 48, "normal"))

    def update_score(self):
        self.clear()
        self.write(self.score, False, align="center", font=("Arial", 48, "normal"))

    def raise_score(self):
        self.score += 1
        self.update_score()
