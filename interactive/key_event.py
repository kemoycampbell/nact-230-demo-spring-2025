import turtle

length = 100
def move_forward():
    turtle.forward(length)

def move_backward():
    turtle.backward(100)
#start listening for event
turtle.listen()
turtle.onkey(move_forward, "Up")
turtle.onkey(move_backward, "Down")



turtle.done()
