import sys
sys.path
import turtle
turtle.__file__

window = turtle.Screen()
turtle.speed(5)
turtle.pensize(5)

#draw the outline of a square 
turtle.penup()
turtle.goto(-350, 100)
turtle.pendown()
turtle.color("black")

turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.penup()

