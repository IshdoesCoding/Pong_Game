from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_list = []
        self.create_ball()



    def create_ball(self):
        ball = Turtle("circle")
        ball.color("purple")
        ball.penup()
        ball.shapesize(.90,.90)
        self.ball_list.append(ball)

    def move(self, pace):
        self.ball_list[0].speed("slow")
        self.ball_list[0].forward(pace)

    def up_angle(self):
        self.ball_list[0].setheading(-45)

    def down_angle(self):
        self.ball_list[0].setheading(45)


    def ball_boundaries1(self):
        if self.ball_list[0].ycor() > 300:
            self.down_angle()
            print(self.ball_list[0].ycor())
        elif self.ball_list[0].ycor() < -300:
            self.up_angle()
            print(self.ball_list[0].ycor())

    def ball_boundaries2(self):
        if self.ball_list[0].ycor() > 300:
            self.ball_list[0].setheading(330)
            print(self.ball_list[0].ycor())
        elif self.ball_list[0].ycor() < -300:
            self.ball_list[0].setheading(-330)
            print(self.ball_list[0].ycor())

