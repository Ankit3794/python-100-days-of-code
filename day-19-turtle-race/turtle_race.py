import turtle as t
import random as rd

colors = ["red", "green", "black", "pink", "yellow", "blue", "orange"]
y_cord = [-150, -100, -50, 0, 50, 100, 150]

screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []
for i in range(len(colors)):
    tim = t.Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=y_cord[i])
    tim.speed(rd.choice(range(10)))
    turtles.append(tim)

game_on = False
if user_bet:
    game_on = True

while game_on:
    for t in turtles:
        if t.xcor() < 230:
            t.forward(rd.randint(0, 10))
        else:
            game_on = False
            winning_turtle = t.pencolor()
            result = "won" if user_bet == winning_turtle else "lose"
            print(f"you {result}. {winning_turtle} won the race!!")

screen.exitonclick()