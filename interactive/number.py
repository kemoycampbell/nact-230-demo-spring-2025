import turtle

"""
    A function that draw a square based on the
    given length
    parameters:
        - length - the length of the square
"""
def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)


#ask the user 4 times
for i in range(4):
    #ask the user for the length
    length = turtle.numinput("Length", "Enter the length:")
    turtle.clear() # clear the screen

    #take the length from the user and draw the square
    draw_square(length)

#pause the turtle
turtle.done()

