from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update()

    def lscore(self):
        self.l_score += 1
        self.clear()
        self.hideturtle()
        self.update()
    def rscore(self):
        self.r_score += 1
        self.clear()
        self.hideturtle()
        self.update()

    def update(self):
        self.goto(-130, 190)
        self.write(f"{self.l_score}", align='center', font=('Courier', 70, 'normal'))
        self.goto(130, 190)
        self.write(f"{self.r_score}", align='center', font=('Courier', 70, 'normal'))


