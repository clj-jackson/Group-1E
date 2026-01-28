import turtle

#fdf5e6

t = turtle.Turtle()
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

