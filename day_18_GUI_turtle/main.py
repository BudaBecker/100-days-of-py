import colorgram
import turtle
import random

colors = colorgram.extract('image.jpg', 20)

colors_list = []
for i in range(len(colors)):
    colors_list.append(tuple(colors[i].rgb))

turtle.colormode(255)
dunga = turtle.Turtle()
dunga.speed(0)
dunga.penup()
dunga.hideturtle()

dunga.setheading(225)
dunga.forward(300)
dunga.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    dunga.dot(20, random.choice(colors_list))
    dunga.forward(50)

    if dot_count % 10 == 0:
        dunga.setheading(90)
        dunga.forward(50)
        dunga.setheading(180)
        dunga.forward(500)
        dunga.setheading(0)

screen = turtle.Screen()
screen.exitonclick()