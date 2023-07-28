import time
from turtle import Screen
from capstonePlayer import Player
from capstoneCarManager import CarManager
from capstoneScoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player for game
player = Player()

# Create car manager
car_manager = CarManager()

# Create scoreboard to show levels
scoreboard = Scoreboard()

# Get screen to listen
screen.listen()

# Move turtle when up key is pressed
screen.onkey(player.move_up, "Up")

# Create boolean for keeping game on
game_is_on = True

# While loop for game
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    # Iterate over cars in list
    for car in car_manager.all_cars:
        # If the car is less than 20 pixels from the player, game ends
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    
    # Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
screen.exitonclick()