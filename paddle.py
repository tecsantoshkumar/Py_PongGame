from turtle import *


class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.setpos(pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

