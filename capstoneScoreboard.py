# Scoreboard for capstone game
import _tkinter
from turtle import Turtle
FONT = ("Courier", 24, "normal")

# Inherits from Turtle class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Level starts out at 1
        self.level = 1
        # Hide actual turtle and lift pen up
        self.hideturtle()
        self.penup()
        # Make the scoreboard display in top left corner
        self.goto(-280, 250)
        # Write the score
        self.update_scoreboard()
    
    # Method for updating scoreboard
    def update_scoreboard(self):
        # Write the level on the screen
        self.write(f"Level: {self.level}", align="left", font = FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
    
    # Method to be called when game is over
    def game_over(self):
        # Text is written in centre of screen
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font=('Courier New', 20, 'normal'))
        