import turtle

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
    turtle.goto(0, -radius)
    turtle.pendown()
    turtle.color("navy")
    turtle.width(2)
    turtle.circle(radius)

    # Drawing 24 spokes
    for i in range(24):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.setheading(90)  # Pointing north
        turtle.right(15 * i)  # 15-degree increment for 24 spokes
        turtle.pendown()
        turtle.forward(radius)

def display_message(message, x, y, color="blue"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    style = ("Courier", 24, "bold")
    turtle.write(message, align="center", font=style)
    turtle.penup()

# Set up the screen
turtle.speed(6)
turtle.setup(width=800, height=600)
turtle.bgcolor("white")

# Draw the Indian Flag
stripe_width = 400
stripe_height = 100
x_start = -200
y_start = 100

# Display the Happy Independence Day message
display_message("Happy Independence Day!", 0, 250)

# Saffron stripe
draw_rectangle("orange", x_start, y_start, stripe_width, stripe_height)

# White stripe
draw_rectangle("white", x_start, y_start - stripe_height, stripe_width, stripe_height)

# Green stripe
draw_rectangle("green", x_start, y_start - 2 * stripe_height, stripe_width, stripe_height)

# Draw the Ashoka Chakra in the center of the white stripe
turtle.penup()
turtle.goto(0, y_start - stripe_height / 2)
turtle.pendown()
draw_ashoka_chakra(50)

# Display the "Namaste India" message after the flag is drawn
display_message("Namaste India", 0, -250, color="green")

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
