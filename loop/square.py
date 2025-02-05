import turtle

def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)

"""
    This function uses a loop to draw a triangle
    parameters:
        length - the length of the triangle
"""
def draw_triangle(length):
    #this will loop 3 times
    for i in range(3):
        turtle.forward(length) # move the turtle 100 in length
        turtle.left(120) # turn left at 120 degree


#draw_square(100)
draw_triangle(200)

turtle.done()