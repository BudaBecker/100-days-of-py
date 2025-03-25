import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle(visible=False)
writer.penup()
writer.speed(0)

data = pandas.read_csv("./us-states-game/50_states.csv")
states_name = data.state.to_list()
coords = list(zip(data.x, data.y))
score = 0
index_guess = []

while True:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name? (or 'exit' to give up)").title()
    if answer_state in states_name:
        score += 1
        index = states_name.index(answer_state)
        index_guess.append(index)
        writer.goto(coords[index])
        writer.write(arg=states_name[index], align="center")
    if score == 50:
        writer.goto(0,0)
        writer.color("Green")
        writer.write(arg="You Win!", align="center", font=("Courier", 80, "bold"))
        writer.goto(0,-20)
        writer.write(arg="click to exit", align="center", font=("Courier", 20, "bold"))
        break
    if answer_state == "Exit":
        for i in range(50):
            writer.color("red")
            if i in index_guess:
                continue
            else:
                writer.goto(coords[i])
                writer.write(arg=states_name[i], align="center")
        writer.goto(-100,-350)
        writer.write(arg=f"Your score: {score}", align="center", font=("Courier", 30, "bold"))
        break

        
screen.exitonclick()