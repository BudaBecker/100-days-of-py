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

car_list = []
for _ in range(10):
    car = CarManager()
    car_list.append(car)

screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")
screen.onkeypress(fun=player.move_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    
    if player.ycor() > 280:
        scoreboard.next_level()
        player.restart()
        for cars in car_list:
            cars.increment_speed()
        
        
    for cars in car_list:
        if cars.distance(player) < 24:
            scoreboard.game_over()
            game_is_on = False
        if cars.xcor() < -280:
            cars.set_pos()
        cars.move()

screen.exitonclick()