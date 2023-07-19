import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")
t.speed(2)

# Function to draw a square
def draw_square():
    for _ in range(4):
        t.forward(100)
        t.right(90)

# Function to draw a circle
def draw_circle():
    t.circle(50)

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        t.forward(100)
        t.left(120)

# Function to draw a star
def draw_star():
    for _ in range(5):
        t.forward(100)
        t.right(144)

# Function to write "Hello Rutu Jevlis ka?"
def write_message():
    t.penup()
    t.goto(-150, -150)
    t.pendown()
    t.write("Hello Rutu Jevlis ka?", font=("Arial", 16, "bold"))

# Move turtle to starting position
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw various designs
draw_square()
t.penup()
t.forward(150)
t.pendown()

draw_circle()
t.penup()
t.forward(150)
t.pendown()

draw_triangle()
t.penup()
t.forward(150)
t.pendown()

draw_star()
t.penup()
t.forward(150)
t.pendown()

# Write the message
write_message()

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.done()




