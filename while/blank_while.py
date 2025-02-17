import turtle

blank = True # a variable to track if blank or not

#continue as long as blank is true
#while blank: --> #short cut
while blank == True:
    word = turtle.textinput("Your information", "Enter your name:") 
    #check if not blank
    if word!="":
        blank = False #update this so that it can stop if false

