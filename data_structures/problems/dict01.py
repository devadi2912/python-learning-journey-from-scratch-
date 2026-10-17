"""
create a dictionary student = {"name" : "john" , "age" : 20, "grade" : "A" }
- print value of name 
- change the grade to "A++"
- add  a new city delhi to the dictionary 
"""
student = {
    "name" : "john" ,
    "age" : 20,
    "grade" : "A"
}

print(student)
print(student["name"])
student["grade"] = "A++"
print(student)
student["city"] = "delhi"
print (student)

print (student.keys())
print (student.values())
print (student.items())


