'''
Student Grade Calculator
Take marks and assign:

90-100 → A
80-89 → B
70-79 → C
60-69 → D
Below 60 → F
'''
grade = int(input("enter your marks: "))
if (grade > 100 or grade < 0 ):
    print ("invalid input !")
elif grade >89 :
    print ("assigned grade : A")
elif grade > 79 :
    print ("assigned grade : B")
elif grade > 69 :
    print ("assigned grade : C")
elif grade > 59 :
    print ("assigned grade : D")
else :
    print ("sorry the assigned grade is : F")