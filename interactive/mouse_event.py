import turtle


length = 100

def draw_square(x,y):

    global length 
    print(length)
    #set the pen location based on the click x,y
    turtle.penup()
    turtle.setpos(x,y)
    turtle.down()
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    
    #make smaller for the next one
    length = length -50


#askt he user for the length
length = turtle.numinput("The size", "Enter the length:")
turtle.onscreenclick(draw_square)

turtle.done()