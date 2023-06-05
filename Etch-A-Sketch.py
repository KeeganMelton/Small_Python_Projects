from turtle import Turtle, Screen

# sets the cursor and the screen
draw = Turtle()
screen = Screen()


# moves the cursor forward
def move_forward():
    draw.forward(10)


# moves the cursor backwards
def move_backward():
    draw.backward(10)


# turns the cursor to the right
def turn_right():
    draw.right(10)


# turns the cursor to the left
def turn_left():
    draw.left(10)


# clears the screen and resets the cursor
def reset():
    draw.penup()
    draw.home()
    draw.clear()
    draw.pendown()


# moves the cursor using the WASD keys
# clears screen using 'C' key
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)

# exits screen
screen.exitonclick()