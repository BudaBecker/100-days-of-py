import turtle, snake, time, food, scoreboard

DIFICULTY = [0.2, 0.1, 0.05]

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = food.Food()
snake = snake.Snake()
scoreboard = scoreboard.Scoreboard()

input_diff = screen.numinput("Difficulty", "0- Easy\n1- Normal\n2- Hard", 1, minval=0, maxval=2)
difficulty = DIFICULTY[int(input_diff)]

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    screen.update()
    time.sleep(difficulty)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        screen.update()
        scoreboard.game_over()
        snake.snake_game_over(screen=screen)
        if screen.textinput(title="GAME OVER", prompt="type 'yes' to play again.").lower() != "yes":
                break
        else:
            scoreboard.reset_score()
            snake.reset_snake()
            screen.listen()
                
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            screen.update()
            scoreboard.game_over()
            snake.snake_game_over(screen=screen)
            if screen.textinput(title="GAME OVER", prompt="Do you want to keep playing? (yes/no)").lower() != "yes":
                break
            else:
                scoreboard.reset_score()
                snake.reset_snake()
                screen.listen()
            
    
screen.exitonclick()