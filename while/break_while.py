import turtle 
import tkinter.messagebox as dialog


EXIT_WORD = "EXIT"

#An forever prompt
while True:

    word = turtle.textinput("Information", "Enter a word")

    if word == EXIT_WORD:
        dialog.showinfo("Thank you using our program", "get out of here!")
        break
    #show the word
    dialog.showinfo("You typed:", word)
    