from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 1


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.set_pos()
        
    def set_pos(self):
        random_y = random.randint(-250, 250)
        random_x = random.randint(300, 600)
        self.goto(x=random_x, y=random_y)
        
    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(x=self.xcor() - self.car_speed, y=self.ycor())
    
    def increment_speed(self):
        self.car_speed += MOVE_INCREMENT