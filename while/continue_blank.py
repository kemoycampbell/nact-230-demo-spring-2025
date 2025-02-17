import turtle 
import tkinter.messagebox as dialog

while True:
    ask = turtle.textinput("Title", "Enter the input: ")
    if ask=="":
        dialog.showerror("Error", "Input cannot be blank!")
        continue
    dialog.showinfo("you typed:", ask)