"""
Problem 2: Student Marks 📚

Create a Student class with the following requirements:

Initialize the student's name and marks using __init__().
Create a getter for marks.
Create a setter that accepts marks only between 0 and 100, inclusive.
If the marks are outside this range, print "Invalid marks!" and retain the previous marks.

Expected behaviour:

student = Student("Aditya", 85)

print(student.marks)  # 85

student.marks = 95
print(student.marks)  # 95

student.marks = 150
print(student.marks)  # 95
"""

class Student :
    def __init__(self, name, marks):
        self._name = name 
        self._marks = marks 
        
    @property 
    def marks (self):
        return self._marks 
    
    @marks.setter
    def marks (self, marks):
        if (marks > 0 and marks <101):
            self._marks = marks 
        else :
            print ("invald input")
            
            
stud = Student("aditya", 88)
print (stud.marks)
stud.marks = int (input ("enter new marks :"))
print (stud.marks)
stud.marks = int(input("enter a negative marks for testing :"))
print (stud.marks)
            