from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

BALL_PACE = 30

screen = Screen()
screen.screensize(800,600)
screen.bgcolor("black")
screen.tracer(20)

line1 = Turtle()
line2 = Turtle()


paddle = Paddle()
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle.up1, "w")
screen.onkey(paddle.down1, "s")
screen.onkey(paddle.up2, "Up")
screen.onkey(paddle.down2, "Down")


## dashed line (asthetic)

for i in range(20):
    line1.setheading(90)
    line1.forward(10)
    line1.color("white")
    line1.forward(10)
    line1.color("black")

for c in range(20):
    line2.setheading(270)
    line2.forward(10)
    line2.color("white")
    line2.forward(10)
    line2.color("black")





# Game logic

game_on = True


while game_on:
    screen.update()
    time.sleep(0.1)

    # Score logic
    score.player1_score()
    score.player2_score()

    # Player Logic
    paddle.move_player1()
    paddle.move_player2()


    #boundaries for player 1
    if paddle.head1.ycor() > 350:
        paddle.down1()
    elif paddle.head1.ycor() < -350:
         paddle.up1()

    # boundaries for player 2
    if paddle.head2.ycor() > 350:
        paddle.down2()
    elif paddle.head2.ycor() < -350:
        paddle.up2()


    # Ball logic

    ball.move(BALL_PACE)

    # ball boundaries
    if BALL_PACE == 30:
        ball.ball_boundaries2()
    if BALL_PACE == -30:
        ball.ball_boundaries1()








    # if ball.ball_list[0].ycor() > 300:
    #     ball.down_angle()
    # elif ball.ball_list[0].ycor() < -300:
    #     ball.up_angle()


    # win or loss metric
    if ball.ball_list[0].xcor() > 700:
        score.calc_p1()
        score.player2_score()
        ball.ball_list[0].goto(0, 0)
        ball.ball_list[0].setheading(0)

        if score.player1_score() == 10:
            score.goto(0,0)
            score.write("Player 1 has won! ", align = "center", font = ("Arial", 50, "normal"))
            game_on = False

    elif ball.ball_list[0].xcor() < -700:
        score.calc_p2()
        score.player1_score()
        ball.ball_list[0].goto(0,0)
        ball.ball_list[0].setheading(0)

        if score.player2_score() == 10:
            score.goto(0,0)
            score.write("Player 2 has won! ", align = "center", font = ("Arial", 50, "normal"))
            game_on = False



    #player 1
    for segs1 in paddle.segment_p1[0:2]:
        if ball.ball_list[0].distance(segs1) < 15:
            ball.up_angle()
            BALL_PACE = 30

    for segs1 in paddle.segment_p1[2:4]:
        if ball.ball_list[0].distance(segs1) < 15:
            ball.down_angle()
            BALL_PACE = 30


    # player 2
    for segs in paddle.segment_p2[0:2]:
        if ball.ball_list[0].distance(segs) < 15:
            ball.up_angle()
            BALL_PACE = -30
    for segs in paddle.segment_p2[2:4]:
        if ball.ball_list[0].distance(segs) < 15:
            ball.down_angle()
            BALL_PACE = -30




screen.exitonclick()
