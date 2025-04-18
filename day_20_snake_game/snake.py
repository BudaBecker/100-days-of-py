import turtle, time

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def reset_snake(self):
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self): 
        for positions in STARTING_POS:
            self.add_segment(positions)
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def add_segment(self, position):
            new_segment = turtle.Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def snake_game_over(self, screen):
        for segment in self.segments:
            segment.ht()
            segment.goto(1000,1000)
            screen.update()
            time.sleep(0.25)  
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
         
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)