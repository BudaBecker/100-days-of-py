from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, player_side: str):
        '''Player side must be "left" or "right"'''
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1, outline=0)
        
        if player_side == "right":
            self.goto(x=350, y=0)
        else:
            self.goto(x=-350, y=0)
            
    def move_up(self):
        if self.ycor() < 240:
            self.forward(40)
    
    def move_down(self):
        if self.ycor() > -240:
            self.backward(40)