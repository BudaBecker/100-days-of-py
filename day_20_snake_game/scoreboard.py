import turtle
ALIGNMENT = "center"
FONT = ('Arial', 22, 'normal')

class Scoreboard(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(x=0, y=270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=-20)
        self.write(arg="click to exit", align=ALIGNMENT, font=('Arial', 10, 'normal'))