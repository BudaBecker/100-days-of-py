import turtle
import random

is_racing = False
screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)
user_bet = screen.textinput("Turtle Race Bet", "Which turtle will win the race? Enter a color:")
y_pos = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for t_index in range(0,6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.speed(8)
    new_turtle.color(colors[t_index])
    new_turtle.goto(x=-230, y=y_pos[t_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_racing = True

random.shuffle(all_turtles)
while is_racing:
    for runners in all_turtles:
        runners.forward(random.randint(0, 15))
        if runners.xcor() > 230:
            winner_color = runners.pencolor()
            is_racing = False
            break

if winner_color == user_bet:
    print(f"You've won! The {winner_color} turtle is the winner!")
else:
    print(f"You've lost! The {winner_color} turtle is the winner!")

screen.exitonclick()