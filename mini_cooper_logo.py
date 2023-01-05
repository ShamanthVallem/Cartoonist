import turtle

win = turtle.Screen()
win.title("Mini Cooper")
win.bgcolor("White")

t = turtle.Turtle()
t.pencolor("Black")
t.pensize(3)
t.speed(100)
radius = 100
t.penup()
t.setposition(0, -radius)
t.pendown()
t.circle(radius)
t.left(90)
t.penup()
t.forward(3*radius/2)
t.left(90)
t.forward((3**0.5)*radius/2)
t.pendown()
t.forward(radius*2)
t.right(180)
t.penup()
t.forward((radius*2)+((3**0.5)*radius))
t.pendown()
t.forward(radius*2)

# line_t2
t.penup()
t.right(90)
t.forward(radius/4)
t.right(90)
t.forward(radius/4)
t.pendown()
t.forward(2*radius-(radius/4)-13)
t.penup()
t.forward(2*radius)
t.pendown()
t.forward(2*radius-(radius/4)-13)

# line_t3
t.penup()
t.left(90)
t.forward(radius/4)
t.left(90)
t.forward(radius/4)
t.pendown()
t.forward(2*radius-(radius/4)-39)
t.penup()
t.forward(2*radius)
t.pendown()
t.forward(2*radius-(radius/4)-39)

# line_t4
t.penup()
t.right(90)
t.forward(radius/4)
t.right(90)
t.forward(radius/4)
t.pendown()
t.forward(2*radius-(radius/4)-60)
t.penup()
t.forward(2*radius-5)
t.pendown()
t.forward(2*radius-(radius/4)-60)

t.penup()
t.right(180)
t.forward(2*radius-(radius/4)-60+((radius)/4))
t.left(90)
t.forward(radius/4)


turtle.done()
