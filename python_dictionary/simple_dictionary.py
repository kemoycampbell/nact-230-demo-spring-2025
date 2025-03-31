#create a dictionary

#option 1
students = {}
print(students)

#option 2
students = dict()
print(students)

#create a dictionary with some value
grace = {
    "id":123456777,
    "first":"Grace",
    "last":"Huff",
    "GPA":3.3,
    "major":"ACT"
}

print(grace)

#get the id from the dictionary
id = grace["id"]
print(id)

#change the id
grace["id"] = "00001"
print(grace)

#show first and last name
print(f"{grace["first"]} {grace["last"]}")

#remove the last name
del grace["last"]
print(grace)

#add the last name
grace["last"] = "Huff"
print(grace)

#loop through the dictionary
for key in grace:
    print(f"Key:{key}--> value:{grace[key]}")

#key and values using items
print("Using items")
for key,value in grace.items():
    print(f"Key:{key}--> value:{value}")


#print all keys
print(grace.keys())

#show all values
print(grace.values())

#check if a key exist before trying to access it
if "inventKeyFooMeh" in grace:
    print(grace["inventKeyFooMeh"])
else:
    print("There is no inventKeyFooMeh key in grace...skip printing")