import turtle
import time

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_ashoka_chakra(radius):
    turtle.penup()
    turtle.goto(0, 0 - radius)  
    turtle.pendown()
    turtle.color("navy")
    turtle.width(2)
    turtle.circle(radius)

    # Drawing 24 spokes
    for _ in range(24):
        turtle.penup()
        turtle.goto(0, 0)  # Start from the center of the Chakra
        turtle.setheading(90)  # Pointing north
        turtle.right(15 * _)  # 15-degree increment for 24 spokes
        turtle.pendown()
        turtle.forward(radius)

def display_message(message, x, y, delay=0.1):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("blue")
    style = ("Courier", 24, "bold")
    
    for char in message:
        turtle.write(char, align="center", font=style)
        time.sleep(delay)
        x += 15  # Adjust the horizontal position for each character
        turtle.goto(x, y)

# Set up the screen
turtle.speed(6)
turtle.setup(width=800, height=600)
turtle.bgcolor("white")

# Display the "Happy Independence Day" message slowly at runtime
display_message("Happy Independence Day!", -150, 250)

# Draw the Indian Flag
stripe_width = 600
stripe_height = 100
x_start = -300
y_start = 150

# Saffron stripe
draw_rectangle("orange", x_start, y_start, stripe_width, stripe_height)

# White stripe
draw_rectangle("white", x_start, y_start - stripe_height, stripe_width, stripe_height)

# Green stripe
draw_rectangle("green", x_start, y_start - 2 * stripe_height, stripe_width, stripe_height)

# Draw the Ashoka Chakra in the center of the white stripe
draw_ashoka_chakra(50)

# Display the "Namaste India" message slowly at runtime
display_message("Namaste India", -100, -250, delay=0.1)

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
