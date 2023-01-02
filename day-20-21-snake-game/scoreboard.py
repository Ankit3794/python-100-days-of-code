from turtle import Turtle
import random as rd

class Scorecard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))
        self.hideturtle()
        
    
    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=('Arial', 20, 'normal'))