import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
t = turtle.Turtle()
t.pensize(2)
t.speed(5)

# Function to draw a square centered at the origin
def draw_square(size):
    t.penup()
    t.goto(-size / 2, -size / 2)  # move to bottom-left corner
    t.pendown()
    for _ in range(4):
        t.forward(size)
        t.left(90)

# List of square sizes (largest to smallest)
sizes = [200, 150, 100, 50]

# Draw each nested square
for size in sizes:
    draw_square(size)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
