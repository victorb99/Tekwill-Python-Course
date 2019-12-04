class Student:
    
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_average(self, grades=[]):
        self.grades = sum(grades)/len(grades)

student_name = input()

student = Student(student_name)
print(student.name)