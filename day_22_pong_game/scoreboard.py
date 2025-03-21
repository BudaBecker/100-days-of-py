from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.left_score = 0
        self.right_score = 0
        self.write_scores()
        
    def write_scores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.left_score, align="center", font=("courier", 80, "normal"))
        self.goto(100,200)
        self.write(arg=self.right_score, align="center", font=("courier", 80, "normal"))
    
    def right_point(self):
        self.right_score += 1
        self.write_scores()
    
    def left_point(self):
        self.left_score += 1
        self.write_scores()
        
    def game_over(self):
        self.color("red")
        self.goto(0,-20)
        if self.right_score == 5:
            self.write(arg=f"GAME OVER.\nright won {self.right_score}-{self.left_score}",align="center", font=("courier", 40, "normal"))
        else:
            self.write(arg=f"GAME OVER.\nleft won {self.left_score}-{self.right_score}",align="center", font=("courier", 40, "normal"))
        