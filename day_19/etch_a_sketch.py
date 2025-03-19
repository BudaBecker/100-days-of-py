from turtle import Screen, Turtle

dunga = Turtle()
screen = Screen()

def move_foward():
    dunga.forward(10)
def move_backward():
    dunga.backward(10)
def look_right():
    dunga.right(15)
def look_left():
    dunga.left(15)
def clear_screen():
    screen.reset()

screen.title("Simple Etch-A-Sketch")

screen.listen()
screen.onkey(key="w", fun=move_foward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=look_left)
screen.onkey(key="d", fun=look_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()