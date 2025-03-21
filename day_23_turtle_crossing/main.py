import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")
screen.onkeypress(fun=player.move_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if player.ycor() > 280:
        scoreboard.next_level()
        player.restart()
        
    if True: #DISTANCIA CARRO/PLAYER
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()