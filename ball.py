import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move=20
        self.y_move=20

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move*=-1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()