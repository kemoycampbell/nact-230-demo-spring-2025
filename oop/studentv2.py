class Student:
    def __init__(self, name, grade):
        #setup the attributes with
        #default values
        self.name = name
        self.grade =grade
        self.scores = []
    
    """
    This takes a name from the parameter
    and assign it to the attribute
    """
    def set_name(self, name):
        self.name = name        # Assign the provided name to the student's name attribute
    
    def get_name(self):
        return self.name        # Return the student's name
    
    def set_grade(self, grade):
        self.grade = grade      # Assign the provided grade to the student's grade attribute
    
    def get_grade(self):
        return self.grade       # Return the student's grade
    
    def add_score(self, score):
        self.scores.append(score)  # Add a score to the student's list of scores
    
    def get_scores(self):
        return self.scores      # Return the list of the student's scores

    def get_average(self):
        sum = 0                 # Initialize sum to 0
        for score in self.scores:
            sum += score        # Add each score to the total sum
        average = sum / len(self.scores)  # Calculate the average score

        return average          # Return the calculated average
    
    "change what __str__ show"
    def __str__(self):
        return f"Name:{self.name}\ngrade:{self.grade}\nscores:{self.scores}"
    

grace = Student("Grace Huff", 100)

print("grace info:")
print(grace)


# print(f"Name:{grace.get_name()}")                      # Print grace's name
# print(f"{grace.get_name()}'s scores: {grace.get_scores()}")   # Print grace's list of scores
# #print(f"{grace.get_name()}'s average: {grace.get_average()}")
