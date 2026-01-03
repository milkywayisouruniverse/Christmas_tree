import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("lightyellow")

c = turtle.Turtle()
c.speed(0)
c.width(2)

# Head
c.penup()
c.goto(0, -20)
c.pendown()
c.color("orange")
c.begin_fill()
c.circle(60)
c.end_fill()

# Left ear
c.penup()
c.goto(-40, 40)
c.pendown()
c.begin_fill()
c.setheading(60)
c.forward(40)
c.setheading(180)
c.forward(40)
c.setheading(-60)
c.forward(40)
c.end_fill()

# Right ear
c.penup()
c.goto(40, 40)
c.pendown()
c.begin_fill()
c.setheading(120)
c.forward(40)
c.setheading(0)
c.forward(40)
c.setheading(-120)
c.forward(40)
c.end_fill()

# Eyes
c.penup()
c.goto(-20, 15)
c.pendown()
c.color("black")
c.begin_fill()
c.circle(5)
c.end_fill()

c.penup()
c.goto(20, 15)
c.pendown()
c.begin_fill()
c.circle(5)
c.end_fill()

# Nose
c.penup()
c.goto(0, 0)
c.pendown()
c.color("pink")
c.begin_fill()
c.circle(4)
c.end_fill()

# Mouth
c.penup()
c.goto(0, -5)
c.pendown()
c.setheading(-90)
c.forward(10)
c.left(45)
c.circle(10, 90)
c.penup()
c.goto(0, -15)
c.pendown()
c.right(90)
c.circle(-10, 90)

# Whiskers
c.penup()
c.goto(-10, 0)
c.setheading(180)
c.pendown()
c.forward(30)

c.penup()
c.goto(-10, -5)
c.pendown()
c.forward(30)

c.penup()
c.goto(10, 0)
c.setheading(0)
c.pendown()
c.forward(30)

c.penup()
c.goto(10, -5)
c.pendown()
c.forward(30)

# Body
c.penup()
c.goto(0, -150)
c.pendown()
c.color("orange")
c.begin_fill()
c.circle(90)
c.end_fill()

# Tail
c.penup()
c.goto(90, -120)
c.pendown()
c.setheading(-30)
c.width(6)
c.circle(80, 120)

# Finish
c.hideturtle()
screen.mainloop()

