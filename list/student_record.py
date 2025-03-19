options = ["Add a student", "Remove a student", "View Student","Exit"]

#create a list to hold our student records
students = []

#function to add a student
def add_student():
    while True:
        student = input("Enter the student first and last name(separate with space):")
        #prevent empty
        if len(student) == 0:
            print('name cannot be empty')
            continue

        #add the student to the list
        students.append(student)
        #inform the user that the student was added
        print(f"{student} was successfully added to the list")
        break

#build an interactive program with while True
while True:
    #show the menu options
    print("Menu")
    print("=========")
    for i in range(len(options)):
        print(f"{i+1} -- {options[i]}")
    
    #ask the user for their selection
    selection = int(input("Enter your selection:"))

    #make decision based on user input
    if selection == 1:
        add_student()
    
    elif selection == 2:
        #show the student a list
        print("Students\n======")
        for j in range(len(students)):
            print(f"{j+1} -- {students[j]}")
        
        #ask for selection of user to remove
        target_student_index = input("Enter the number of student to remove:")
        target_student_index = int(target_student_index)

        #we subtract 1 because we showed the user from 1, 2,3 etc
        student = students.pop(target_student_index-1)
        print(f"{student} was successfully removed")

    elif selection == 3:
        #show all user in the list
        print("Student list:")
        for name in students:
            print(name)
    
    elif selection == 4:
        #thank the user and end
        print("Thank you for using our mini SIS")
        break
    else:
        print("Invalid selection!")
        print(f"Please select option 1 - {len(options)}")
    
    #spaces
    print("\n")


