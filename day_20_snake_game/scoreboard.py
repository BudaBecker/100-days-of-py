import turtle

ALIGNMENT = "center"
FONT = ('Arial', 22, 'normal')

class Scoreboard(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, 270)
        self.update_scoreboard()
        
    def reset_score(self):
        self.clear()
        self.goto(0, 270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.clear()
        self.write(arg=f"Score: {self.score}      High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def game_over(self):
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=-20)
        self.write(arg="click the screen to leave", align=ALIGNMENT, font=('Arial', 10, 'normal'))
        self.score = 0