import turtle

#fdf5e6

t = turtle.Turtle()
t.pencolor("#00008b")
t.fillcolor("#00008b")

# Draw outer light blue outline first
t.pensize(5)  # Set outline thickness
t.pencolor("#87cefa")  # Light blue outline color
for i in range(4):
    t.forward(105)
    t.right(90)

# Draw filled dark blue square inside the outline
t.pencolor("#00008b")
t.fillcolor("#00008b")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.up()
t.forward(50)
t.right(90)
t.forward(15)

t.right(45)
t.width(10)
t.pencolor("#87cefa")
t.down()
t.forward(50)
t.left(135)
t.forward(15)
t.right(90)
t.forward(30)
t.left(90)
t.forward(40)
t.left(90)
t.forward(30)
t.right(90)
t.forward(15)
t.left(135)
t.forward(50)

# Add 3 dots above the logo
t.up()
t.pencolor("#87cefa")
t.fillcolor("#87cefa")
dot_y_position = 10.5  # Position above the main logo
x_positions = [30, 50, 70]  # X-axis positions for each dot

for x_pos in x_positions:
    t.goto(x_pos, dot_y_position)
    t.down()
    t.begin_fill()
    t.circle(1)  # Small circle for the dot(size)
    t.end_fill()
    t.up()

t.hideturtle() # Hide the turtle pointer
