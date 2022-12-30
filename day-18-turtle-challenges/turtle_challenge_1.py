from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.bgcolor("pink")

timmy.shape('turtle')

# draw square
for i in range(4):
    timmy.forward(150)
    timmy.right(90)

screen.exitonclick()