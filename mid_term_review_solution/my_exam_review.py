import turtle  # Import the turtle graphics module which allows drawing shapes and images.
import tkinter.messagebox as dialog  # Import tkinter's messagebox module for showing error dialogs.

SCREEN_TITLE = "Mastering the basics"  # A string variable to hold the title of the window.
screen = turtle.Screen()  # Create a turtle screen object to display the graphics.
screen.title(SCREEN_TITLE)  # Set the window title to "Mastering the basics".

def draw_square_spiral(num_turns):  # Define a function to draw a square spiral. It takes an argument 'num_turns'.
    for i in range(num_turns):  # A loop that runs 'num_turns' times, where 'i' is the current iteration number.
       length = i * 10  # The length of the line increases by 10 units with each iteration.
       turtle.forward(length)  # Move the turtle forward by 'length' units.
       turtle.right(90)  # Turn the turtle 90 degrees to the right after drawing each line.

turtle.speed(0)  # Set the turtle's speed to the maximum (0 is the fastest).

# The line below is commented out to prevent the spiral from being drawn every time during testing.
# draw_square_spiral(30)  # Call the function to draw a square spiral with 30 turns.

def square(length):  # Define a function to draw a square. The 'length' argument is the side length of the square.
    for i in range(4):  # Loop 4 times to draw each side of the square.
        turtle.forward(length)  # Move the turtle forward by 'length' units.
        turtle.right(90)  # Turn the turtle 90 degrees to the right after each side.

# The line below is commented out to prevent the square from being drawn every time during testing.
# square(30)  # Call the square function to draw a square with a side length of 30 units.

# Task 4 - Main function starts here.

def main(): 
    length = turtle.numinput("Length", "Enter the square length:")  # Prompt the user for the square's side length.
    turns = turtle.numinput("Turns", "Enter the number of turns:")  # Prompt the user for the number of turns in the spiral.
    
    # Convert the 'turns' input (which is a float) to an integer.
    turns = int(turns)  # Cast 'turns' from float to int to avoid decimal values in the number of turns.

    # While loop to ensure the number of shapes is within a valid range.
    while True:
        shapes = turtle.numinput("Shapes", "How many shapes to draw?:")  # Ask the user how many shapes to draw.
        
        # Check if the input is valid (between 0 and 5).
        if shapes < 0 or shapes > 5:  # If the number of shapes is less than 0 or greater than 5.
            dialog.showerror("Error!", "Shape cannot be negative or more than 5")  # Show an error dialog.
            continue  # Go back to the start of the while loop and prompt the user again.
        else:
            break  # If valid, exit the while loop.

    # Convert 'shapes' from float to int to ensure it's a whole number.
    shapes = int(shapes)

    # Initialize the current shape as "spiral".
    current_shape = "spiral"
    
    # A for loop to draw the specified number of shapes.
    for i in range(shapes):  # Repeat 'shapes' times to draw multiple shapes.
        if current_shape == "spiral":  # If the current shape is "spiral".
            draw_square_spiral(turns)  # Call the function to draw a square spiral with the specified number of turns.
            current_shape = "square"  # After drawing the spiral, change the shape to "square".
        else:  # If the current shape is "square".
            square(length)  # Call the square function to draw a square with the specified side length.
            current_shape = "spiral"  # After drawing the square, change the shape back to "spiral".

        # Reset the turtle's heading so it's always facing east (0 degrees).
        turtle.setheading(0)  
        turtle.penup()  # Lift the pen to move without drawing.
        turtle.forward(250)  # Move the turtle forward by 250 units to avoid overlap.
        turtle.pendown()  # Lower the pen to start drawing again.

# Calling the main function to start the program.
main()   

turtle.done()  # Finish the drawing and keep the turtle graphics window open.
