class Student:
    def __init__(self):
        #setup the attributes with
        #default values
        self.name = ""
        self.grade = 0
        self.scores = []
    
    """
    This takes a name from the parameter
    and assign it to the attribute
    """
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_grade(self, grade):
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
    def add_score(self, score):
        self.scores.append(score)
    
    def get_scores(self):
        return self.scores

    def get_average(self):
        sum = 0
        for score in self.scores:
            sum+=score
        average = sum / len(self.scores)

        return average

#creating objects
grace = Student()
grace.set_name("Grace Huff")
grace.add_score(100)
grace.add_score(70)
grace.add_score(80)
print(f"Name:{grace.get_name()}")
print(f"{grace.get_name()}'s scores: {grace.get_scores()}")
print(f"{grace.get_name()}'s average: {grace.get_average()}")
jose = Student()
jose.set_name("Jose Ramirez")
print(f"Name:{jose.get_name()}")



    
        


    