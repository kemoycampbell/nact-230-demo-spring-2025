"""
Purpose:
    This is a program that use python
    turtle to draw a square.

    We introduce the concept of variables and constants

Author:
    Kemoy Campbell (kscics@rit.edu)
Date:01/29/2025
"""
import turtle

#create a variable to hold the length
length = 300
NINETY_DEGREE_ANGLE = 90

#start by setting the turtle to face up
turtle.left(NINETY_DEGREE_ANGLE)
#draw the top of the sqare
turtle.forward(length)
turtle.right(NINETY_DEGREE_ANGLE)
#draw the right side of the square
turtle.forward(length)
turtle.right(NINETY_DEGREE_ANGLE)
#draw the bottom side of the square
turtle.forward(length)
turtle.right(NINETY_DEGREE_ANGLE)
#draw the left side of the square
turtle.forward(length)
turtle.right(NINETY_DEGREE_ANGLE)


#move the turtle over
turtle.penup()
turtle.right(NINETY_DEGREE_ANGLE)
turtle.backward(350)
turtle.pendown()

#make a second square but smaller
length = 100

turtle.left(NINETY_DEGREE_ANGLE)
#draw the top of the sqare
turtle.forward(length)
turtle.right(NINETY_DEGREE_ANGLE)
#draw the right side of the square
turtle.forward(length)
turtle.right(NINETY_DEGREE_ANGLE)
#draw the bottom side of the square
turtle.forward(length)
turtle.right(NINETY_DEGREE_ANGLE)
#draw the left side of the square
turtle.forward(length)
turtle.right(NINETY_DEGREE_ANGLE)


#keep the windows open
turtle.done()