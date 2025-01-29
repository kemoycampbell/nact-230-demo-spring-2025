"""
Purpose:
    This is a program that use python
    turtle to draw a square.

    We introduce the concept of variables and constants
    with title, background color and pen colors

Author:
    Kemoy Campbell (kscics@rit.edu)
Date:01/29/2025
"""
import turtle

#create a variable to hold the length
length = 300
# a constant to keep the angle
NINETY_DEGREE_ANGLE = 90

#a constant for the screen title
title = "Spongebob the SQUAREPANT"


screen = turtle.Screen() # we store the turtle screen in a variable called screen
#set the title
screen.title(title)

# a variable to store the background color
background = "purple"
screen.bgcolor(background) # set the screen background color

#a variable for pen color
pen_color = "white"
turtle.pencolor(pen_color) #set the pen to use the color

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
pen_color_second = "blue"
turtle.pencolor(pen_color_second)

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