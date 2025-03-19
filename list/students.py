#Create a empty list using []

student_names = []

#append is used to add an element to the list
#append are added at the end of the list
student_names.append("Grace Huff")
student_names.append("Cold Cold")
student_names.append("Zi Zi")
student_names.append("Wade")
#We could achieve the same thing if we knew the names ahead of time using
#student_names = ['Grace', 'Wade', 'Zi', 'Cold']
#We dont always have to start a empty list

#show all students
print(f"The elements in the list are: {student_names}")
#show the size
print(f"The list size is: {len(student_names)}")

first_student = student_names[0] #get the first student name
print(f"First student is: {first_student}")

#show all names in the list using a loop
print("Show all names using a loop:")
for student in student_names:
    print(f"Student name:{student}")

#We can remove using pop. Pop are index based
print("Removing the first student")
deleted_student = student_names.pop(0)
#show all students
print(f"The elements in the list are: {student_names}")
#show the size
print(f"The list size is: {len(student_names)}")

print(f"Student removed:{deleted_student}")

print("Removing another student")
student_names.remove("Cold Cold")
#show all students
print(f"The elements in the list are: {student_names}")
#show the size
print(f"The list size is: {len(student_names)}")

#sorting the list(A-Z)
print("Sort the list")
student_names.sort()
print("List sorted (A-Z)")
print(f"The elements in the list are: {student_names}")

#sorting the list(Z-A)
print("Sort the list - A-Z")
student_names.reverse()
print("List sorted (Z-A)")
print(f"The elements in the list are: {student_names}")

# empty the list and remove everything
print('Deleting the full list')
student_names.clear()
print(f"The elements in the list are: {student_names}")
