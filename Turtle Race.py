import random
from turtle import Turtle, Screen

# does not start the race until the user places
race = False

# lists for turtle starting locations, turtles, and turtle colors
y_positions = [-60, -40, -20, 0, 20, 40, 60]
all_turtles = []
colors = ["red", "blue", "green", "pink", "orange", "purple", "black"]

# screen size and pop-up asking for turtle selection
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Pick a turtle", prompt="Which turtle will win the race? \n"
                                                          "(Red, Blue, Green, Pink, Orange, Purple, Black)").lower()

# adds new turtle to list of turtles (all_turtles)
for turtle_index in range(0, 7):

    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-225, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# starts race after the user has picked a turtle
if user_bet:
    race = True

while race:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won!!")
            else:
                print("Better luck next time")
            race = False
        move_distance = random.randint(0, 10)
        turtle.forward(move_distance)

# closes screen
screen.exitonclick()