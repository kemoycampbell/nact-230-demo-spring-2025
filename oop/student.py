class Student:
    def __init__(self):
        #setup the attributes with
        #default values
        self.name = ""          # Student's name initialized as an empty string
        self.grade = 0          # Student's grade initialized to 0
        self.scores = []        # List to store student's scores, starts empty
    
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

#creating objects
grace = Student()               # Create a Student object named grace
grace.set_name("Grace Huff")             # Set grace's name to an empty string
grace.add_score(100)           # Add a score of 100 to grace's scores
grace.add_score(70)            # Add a score of 70 to grace's scores
grace.add_score(80)            # Add a score of 80 to grace's scores
print(f"Name:{grace.get_name()}")                      # Print grace's name
print(f"{grace.get_name()}'s scores: {grace.get_scores()}")   # Print grace's list of scores
print(f"{grace.get_name()}'s average: {grace.get_average()}") # Print grace's average score

jose = Student()               # Create another Student object named jose
jose.set_name("Jose Ramirez")              # Set jose's name to an empty string
print(f"Name:{jose.get_name()}")  # Print jose's name
