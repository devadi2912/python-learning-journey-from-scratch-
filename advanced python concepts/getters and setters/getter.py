"""Getter (@property): Lets you access a method of an object like an attribute without the ()"""
"""
sets a method that can be used as an object attribute
- main purpose if to retrive a value of a parameter or a custom parameter 
"""


class student :
    
    def __init__(self, name):
        self._name = name    # use underscore variables for attribute variables to prevent confusion 
        
    @property    # inbuilt getter predefined 
    def first (self):
        return self._name.split(" ")[0]
    
    @property
    def last (self):
        return self._name.split(" ")[-1]
    
    # ideally we will have two setters each for updating the first and last attribute of the object 
    
    
stud = student(input("enter full name of the student :"))

"""
to call the methods of first and last we have ti usually perform tasks like 
print (e.first())
print (e.last())
- ie call the methods with an object 

with getters we can set a method to a property that can be accessed like any attribute of the object 
"""

print (stud.first)
print (stud.last)


