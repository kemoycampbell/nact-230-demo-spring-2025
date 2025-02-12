import turtle


length = 100
shape = "square"
circle_size = 100

def draw_circle():
    global circle_size
    turtle.circle(circle_size)
    circle_size = circle_size - 50

def draw_square():

    global length 
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
    
    #make smaller for the next one
    length = length -50

def draw(x,y):
    global shape

    turtle.penup()
    turtle.setpos(x,y)
    turtle.pendown()

    #is the current shape a square?
    if shape == "square":
        draw_square()
        shape = "circle" #switch to circle for next draw
    else:
        draw_circle()
        shape = "square" #switch to square for next draw


#askt he user for the length
length = turtle.numinput("The size", "Enter the length:")
circle_size = turtle.numinput("The size", "circle:")
turtle.onscreenclick(draw)

turtle.done()