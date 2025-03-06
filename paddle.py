from turtle import Turtle

Player1_segment = [(-620,0), (-620,-20), (-620,-40), (-620,-60)]
Player2_segment = [(610,0), (610,-20), (610,-40), (610,-60)]

class Paddle(Turtle):


    # initializer
    def __init__(self):
        super().__init__()
        self.segment_p1 = []
        self.segment_p2 = []
        self.create_player1()
        self.create_player2()
        self.head1 = self.segment_p1[0]
        self.head1.setheading(90)
        self.head2 = self.segment_p2[0]
        self.head2.setheading(90)



    #Player 1 logic
    def create_player1(self):
        for segs in Player1_segment:
            self.add_player1(segs)




    def add_player1(self, position):
        paddle1 = Turtle()
        paddle1.shape('square')
        paddle1.color("white")
        paddle1.penup()
        paddle1.speed("slow")
        paddle1.goto(position)
        self.segment_p1.append(paddle1)



    # player1 movement

    def move_player1(self):
        for parts in range(len(self.segment_p1)-1, 0, -1):
            x_cor = self.segment_p1[parts-1].xcor()
            y_cor = self.segment_p1[parts - 1].ycor()
            self.segment_p1[parts].goto(x_cor,y_cor)


        self.head1.forward(20)



    def up1(self):
        self.head1.setheading(90)
        self.head1.forward(20)



    def down1(self):
        self.head1.setheading(270)
        self.head1.forward(20)










    # Player 2 logic

    def create_player2(self):
        for segs in Player2_segment:
            self.add_player2(segs)

    def add_player2(self, position):
        paddle2 = Turtle()
        paddle2.shape('square')
        paddle2.color("white")
        paddle2.penup()
        paddle2.speed("fastest")
        paddle2.goto(position)
        self.segment_p2.append(paddle2)

    def move_player2(self):
        for parts in range(len(self.segment_p2) - 1, 0, -1):
            x_cor = self.segment_p2[parts - 1].xcor()
            y_cor = self.segment_p2[parts - 1].ycor()
            self.segment_p2[parts].goto(x_cor, y_cor)

        self.head2.forward(20)

    def up2(self):
        self.head2.setheading(90)
        self.head2.forward(20)

    def down2(self):
        self.head2.setheading(270)
        self.head2.forward(20)

