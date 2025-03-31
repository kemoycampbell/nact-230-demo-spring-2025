# The `students` dictionary holds information about students, where each student is identified by a unique `id`.
# Each student is stored as a nested dictionary with keys: id, first name, last name, major, GPA, and year in school.
students = {
    1: {
        "id": 1,
        "first": "John",
        "last": "Doe",
        "major": "Computer Science",
        "gpa": 3.8,
        "year": "Sophomore",
    },
    2: {
        "id": 2,
        "first": "Jane",
        "last": "Smith",
        "major": "Biology",
        "gpa": 3.6,
        "year": "Junior",
    },
    3: {
        "id": 3,
        "first": "Emily",
        "last": "Davis",
        "major": "Chemistry",
        "gpa": 3.9,
        "year": "Senior",
    },
    4: {
        "id": 4,
        "first": "Michael",
        "last": "Brown",
        "major": "Physics",
        "gpa": 3.7,
        "year": "Freshman",
    },
    5: {
        "id": 5,
        "first": "Sarah",
        "last": "Williams",
        "major": "Mathematics",
        "gpa": 3.95,
        "year": "Senior",
    },
    6: {
        "id": 6,
        "first": "David",
        "last": "Miller",
        "major": "Engineering",
        "gpa": 3.4,
        "year": "Sophomore",
    },
    7: {
        "id": 7,
        "first": "Sophia",
        "last": "Taylor",
        "major": "Economics",
        "gpa": 3.5,
        "year": "Junior",
    },
    8: {
        "id": 8,
        "first": "James",
        "last": "Wilson",
        "major": "History",
        "gpa": 3.2,
        "year": "Senior",
    },
    9: {
        "id": 9,
        "first": "Olivia",
        "last": "Moore",
        "major": "Psychology",
        "gpa": 3.85,
        "year": "Freshman",
    },
    10: {
        "id": 10,
        "first": "Ethan",
        "last": "Anderson",
        "major": "English",
        "gpa": 3.7,
        "year": "Sophomore",
    },
}

# Initialize global id variable for generating new student IDs.
id = 1

# Function to add a new student to the `students` dictionary
def add_student():
    global id  # Access the global variable `id`

    # Collecting student information from user input
    first = input("Enter the student's first name:")
    last = input("Enter the student's last name:")
    major = input("Enter the student's major:")
    gpa = float(input("Enter the student's GPA:"))
    year = int(input("Enter the student's year:"))

    # Create a dictionary to store the student's information
    student_info = {
        "id": id,
        "first": first,
        "last": last,
        "major": major,
        "gpa": gpa,
        "year": year,
    }

    # Add the new student to the `students` dictionary with the current `id`
    students[id] = student_info
    print(f"{student_info} was successfully added to the dictionary")

    # Increment the `id` for the next student to be added
    id = id + 1

# Function to view all students in the `students` dictionary
def view_students():
    print("Students in the list:")
    for key in students:
        print(students[key])  # Print each student's dictionary

# Function to find a specific student by their ID
def find_student():
    student_id = int(input("Enter the student's id:"))

    # Check if the provided `student_id` exists in the dictionary
    if student_id in students:
        print(students[student_id])  # Print the student's information
    else:
        print(f"Student with id:{student_id} was not found in the system!")

# Function to update a student's information
def update_student_info():
    # List of possible fields that can be updated
    update_options = [
        "first",  # First name
        "last",   # Last name
        "major",  # Major
        "gpa",    # GPA
        "year",   # Year in school
    ]

    # Get the student ID to update
    student_id = int(input("Enter the student's id:"))

    # Check if the student exists in the dictionary
    if student_id in students:
        print("Options\n=======")
        for update_option in update_options:
            print(update_option)  # Display update options

        choice = input("What do you want to update:")  # Get user input for what to update
        choice = choice.lower()  # Convert to lowercase to handle case insensitivity

        # Check if the choice is valid
        if choice not in update_options:
            print("Invalid choice. You can't do that!")
        else:
            # Prompt for the new value based on the choice of field to update
            if choice == "first" or choice == "last" or choice == "major":
                update = input(f"Enter the new {choice}:")
            elif choice == "gpa":
                update = float(input(f"Enter the new {choice}:"))
            elif choice == "year":
                update = int(input(f"Enter the new {choice}:"))
            
            # Update the student's information in the dictionary
            students[student_id][choice] = update
    else:
        print(f"Student with id:{student_id} was not found in the system!")

# Menu options for user interaction
menu_options = [
    "Add Student",         # Option 1: Add a new student
    "View Students",       # Option 2: View all students
    "Find Student",        # Option 3: Find a specific student
    "Update student info", # Option 4: Update a student's information
    "Exit"                 # Option 5: Exit the program
]

# Main function that runs the program
def main():
    while True:  # Loop continuously until the user exits
        print("Options:")
        for i in range(len(menu_options)):  # Display the menu options
            print(f"{i+1}. {menu_options[i]}")

        selection = input("Selection:")  # Get the user's selection

        # Call the appropriate function based on the user's selection
        if selection == "1":
            add_student()
        elif selection == "2":
            view_students()
        elif selection == "3":
            find_student()
        elif selection == "4":
            update_student_info()
        elif selection == "5":  # Exit the program
            print("Exiting program...")
            break

# Call the main function to start the program
main()
