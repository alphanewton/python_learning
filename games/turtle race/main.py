import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you reckon wins the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
turtles = []

x = -230
y = -150

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=x, y=y)
    y += 50
    turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True
else:
    print("Enter a rainbow color. Restart")

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle was the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle was the winner!")
            break

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
