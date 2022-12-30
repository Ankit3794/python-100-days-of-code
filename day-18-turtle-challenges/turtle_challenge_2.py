from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.bgcolor("pink")

timmy.shape('turtle')

# draw dashed line
for i in range(51):
    if i%2 != 0:
        timmy.pendown()
    else:
        timmy.penup()
    timmy.forward(5)

screen.exitonclick()
