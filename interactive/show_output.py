import tkinter.messagebox
import turtle


#tkinter.messagebox.showinfo("Info", "Thank you!")
#tkinter.messagebox.showerror("error", "Not allowed")
#tkinter.messagebox.showwarning("Caution", "You have been warned!")


name = turtle.textinput("Your name", "What is your name:")

tkinter.messagebox.showinfo("Greeting", f"Hello {name}")