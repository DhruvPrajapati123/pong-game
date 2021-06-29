from turtle import Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
from line import Line
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
list1 = [-280, -240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240, 280, 320]

for i in list1:
    line = Line(i)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect the collision with uper and downer wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detect the collision with right and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # detect when white paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect when white paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
