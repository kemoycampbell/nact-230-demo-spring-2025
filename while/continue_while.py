#show only even numbers

import tkinter.messagebox as dialog
num = 1
MAX = 15

while num < MAX:
    num+=1
    #even if there are no reminder after divide by 2
    if num % 2 != 0:
        continue
    
    dialog.showinfo("Even number:", num)
    