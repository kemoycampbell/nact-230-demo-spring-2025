import turtle
import tkinter.messagebox as dialog


#set to go on forever
error = True
while error:
    length = turtle.numinput("Size", "Enter the length:")
    if length <= 0 or length >=200:
        dialog.showerror("Error", "Length must be greater than 0 but less than 200")
    else:
        error = False

for i in range(4):
    color = turtle.textinput("Color", "pick a color:")
    
    #default set length to 100
    length = 100

    #if the color is blank
    if color == "":
        color = "black" #assign black as the default
    
    turtle.pencolor(color)
    turtle.forward(length)
    turtle.left(90)

#pause
turtle.done()