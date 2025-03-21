from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up",fun=right_paddle.move_up)
screen.onkeypress(key="Down",fun=right_paddle.move_down)
screen.onkeypress(key="w",fun=left_paddle.move_up)
screen.onkeypress(key="s",fun=left_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(right_paddle) < 55 and ball.xcor() == 340 or ball.distance(left_paddle) < 55 and ball.xcor() == -330:
        ball.bounce_x()
    
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.left_point()
    
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.right_point()
    
    if scoreboard.right_score == 5 or scoreboard.left_score == 5:
        scoreboard.game_over()
        game_is_on = False
    
        
    

screen.exitonclick()