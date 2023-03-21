import turtle

# Define a function to draw the Hilbert curve recursively
def hilbert(turtle, order, size, angle):
    if order == 0:
        return
    else:
        turtle.right(angle)
        hilbert(turtle, order-1, size, -angle)
        turtle.forward(size)
        turtle.left(angle)
        hilbert(turtle, order-1, size, angle)
        turtle.forward(size)
        hilbert(turtle, order-1, size, angle)
        turtle.left(angle)
        turtle.forward(size)
        hilbert(turtle, order-1, size, -angle)
        turtle.right(angle)

# Create a turtle graphics window
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Hilbert Fractal")

# Create a turtle and set its properties
tess = turtle.Turtle()
tess.speed(0)
tess.penup()
tess.goto(-200, 0)
tess.pendown()
tess.pensize(2)

# Call the Hilbert function to draw the fractal
hilbert(tess, 5, 10, 90)

# Close the turtle graphics window on click
turtle.done()
