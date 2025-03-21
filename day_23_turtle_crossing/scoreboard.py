from turtle import Turtle

FONT = ("Times", 24, "italic")
FONT_GAMEOVER = ("Courier", 40, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.level = 1
        self.goto(-285, 260)
        self.write_display()
    
    def write_display(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)
        
    def next_level(self):
        self.level += 1
        self.write_display()
    
    def game_over(self):
        self.color("red")
        self.goto(0,-20)
        self.write(arg="GAME OVER", align="center", font=FONT_GAMEOVER)