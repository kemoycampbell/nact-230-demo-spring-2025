import turtle
import tkinter.messagebox as dialog

def ask_name():
    #continously prompt the user
    while True:
        #ask for their name and store in a variable
        name = turtle.textinput("Name", "Enter your name:")
        #check if empty
        if name == "":
            dialog.showerror("You cant do that!", "name must not be blank")
            #go back
            continue 

        #return the name
        return name

#prompt for name and store in person_name
person_name = ask_name()
turtle.Screen().title(person_name)

turtle.done()