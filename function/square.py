"""
    This program introduce the concept of a function
"""

import turtle

"""
    This function draw a fixed square with 
    100 length and 90 angle

    parameters: none
"""
def draw_square_fixed():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

"""
    This function will take length and angle then draw the squaare.
    Parameters:
        length - the length of the square
        angle - the angle of the square
"""
def draw_square(length, angle):
    turtle.forward(length)
    turtle.left(angle)
    turtle.forward(length)
    turtle.left(angle)
    turtle.forward(length)
    turtle.left(angle)
    turtle.forward(length)
    turtle.left(angle)


#call and use the function
#draw_square_fixed()

#call and use our flexible variable
draw_square(200, 90)

#move the turtle over to the left side
turtle.penup()
turtle.backward(300)
turtle.pendown()

#draw a bit bigger square
my_prefer_length = 150
my_angle = 90
draw_square(my_prefer_length, my_angle)

#move the turle inside and draw a smaller square
turtle.penup()
turtle.forward(20)
turtle.pendown()
length = 10
draw_square(length, my_angle)

#make the turtle pop up and stay
turtle.done()