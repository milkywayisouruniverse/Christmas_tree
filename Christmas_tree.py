import turtle
import random
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("skyblue")

flower = turtle.Turtle()
flower.speed(0)
flower.hideturtle()

# Draw stem
flower.penup()
flower.goto(0, -250)
flower.setheading(90)
flower.pendown()
flower.color("green")
flower.width(6)
flower.forward(200)

# Move to flower center
flower.penup()
flower.goto(0, -50)
flower.pendown()

# Draw dandelion seeds
flower.color("white")
flower.width(2)

for angle in range(0, 360, 6):
    flower.penup()
    flower.setheading(angle)
    flower.forward(10)
    flower.pendown()
    flower.forward(120)

    # Seed head
    flower.penup()
    flower.forward(5)
    flower.dot(4)

    flower.backward(135)

# Center
flower.penup()
flower.goto(0, -50)
flower.pendown()
flower.color("yellow")
flower.dot(20)

screen.mainloop()
