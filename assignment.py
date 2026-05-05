import random


class Assignment:
    def __init__(self,course_name: str):
        self.course_name = course_name
    
    def __str__(self):
            return "INSERT INTO Assignment VALUES("+self.course_name

    @staticmethod
    def get_dictionary() -> dict:
        dictionary = {}

        dictionary["Minor Assignment"] = 1
        dictionary["Major Assignment"] = 2
        return dictionary

assignment_count=0
assignment_list = []
assignment_id=1
with open('Courses') as file:
    for line in file:
        for i in range(1,13):
            course_name = Assignment(line.strip())
            assignment_count += 1
            print(course_name.__str__() + " Minor Assignment "+ assignment_count.__str__()+ ", " +str(assignment_id)+", 1, "+str(random.randint(75,100))+");")
            if assignment_count == 12:
                print(f'{course_name}  Major Assignment 1, {str(assignment_id)}  , 2,   {str(random.randint(75, 100))}  );)')
                print(f'{course_name}  Major Assignment 2, {str(assignment_id)}  , 2,   {str(random.randint(75, 100))}  );)')
                print(f'{course_name}  Major Assignment 3, {str(assignment_id)}  , 2,   {str(random.randint(75, 100))}  );)')
                assignment_id+=1
                assignment_count=0
