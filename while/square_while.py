import turtle

num = 1

#continue while number is less than or equal to 4
while num <=4:
    turtle.forward(100)
    turtle.left(90)

    #increase num with each loop
    #this will allow to stop when num = 5
    #num = num + 1
    num+=1 #short cut for num  = num + 1

turtle.done()