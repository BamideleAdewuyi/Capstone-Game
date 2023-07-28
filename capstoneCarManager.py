# Cars for capstone game
# Import modules
import _tkinter
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        # Make list of all cars
        self.all_cars = []
        # Speed of cars
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        # Pick random number between 1 and 6
        random_chance = random.randint(1, 6)
        # If the random number is 1. Then we create a new car
        # This way, not too many cars are created
        if random_chance == 1:
            # New car is square shape and has a random colour
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # Get a random y coordinate for new cars
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            # Add this car to list of all cars
            self.all_cars.append(new_car)
    
    # Method for moving cars
    def move_cars(self):
        # Iterate through list of all cars
        for car in self.all_cars:
            # Moves them all from right to left
            car.backward(self.car_speed)

    
    # Method for increasing speed of cars. Used when player completes
    # a level
    def level_up(self):
        self.car_speed +=MOVE_INCREMENT