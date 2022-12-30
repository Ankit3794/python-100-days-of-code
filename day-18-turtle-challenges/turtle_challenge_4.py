from turtle import Turtle, Screen
import random

# random walk

directions = [0, 90, 180, 270]

timmy = Turtle()
screen = Screen()

timmy.shape('turtle')
timmy.pensize(5)
timmy.speed('fastest')

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    timmy.color(R, G, B)

for _ in range(200):
    timmy.forward(20)
    timmy.setheading(random.choice(directions))
    change_color()


