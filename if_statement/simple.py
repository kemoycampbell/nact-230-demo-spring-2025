import turtle
import tkinter.messagebox

#ask the user for a number
length = turtle.numinput("Number Selection", "Enter a number:")
print(type(length))

#check if length is zero
if length == 0:
    tkinter.messagebox.showerror("You cant do that", "Length cannot be zero!")

#check if negative by checking less than 0
elif length < 0:
    tkinter.messagebox.showerror("You cant do that", "Length cannot be negative!")

#finally we will allow
else:
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
    tkinter.messagebox.showinfo("Congratulation", "You did it!")

turtle.done()