# Player for capstone game. A turtle that user controls
# Import modules
import _tkinter
from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Class inherits from Turtle class
class Player(Turtle):
    def __init__(self):
        super().__init__()
        # Make turtle shape
        self.shape("turtle")
        self.penup()
        # Starts from bottom middle of screen
        self.go_to_start()
        # Make turtle face north
        self.setheading(90)
    
    # Method for moving up screen
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    
    # Method for moving player back to start
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Method for detecting whether player is at finish line
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False