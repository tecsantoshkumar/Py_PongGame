from turtle import *
from paddle import Paddle
from ball import Ball
import time
from score import Score
screen=Screen()
screen.listen()
screen.setup(800,600)
screen.bgcolor("#123")
screen.title("PING PONG GAME !")
screen.tracer(0)

paddle1=Paddle((350,0))
paddle2=Paddle((-350,0))
ball = Ball()
score= Score()

screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")


game=True

while game:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(paddle1) < 50 and ball.xcor() >320\
            or ball.distance(paddle2) <50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360 :
        print("point to Player2")
        # move ball towards player 1
        score.lscore()
        ball.reset()

    if ball.xcor() < -360 :
        print("point to player 1")
        #move ball towards player 2
        score.rscore()
        ball.reset()

screen.exitonclick()