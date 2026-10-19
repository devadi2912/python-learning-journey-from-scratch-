"""
in python getters and setters should have the same name as the work on the same attribute 
- getters : are basically used to retrive a value of a property 
- setters : are used to modufy that attribute 

a pair of setters an getters are usually used to work on the same attribute one for retriving and on efor updating the value as sinlge as aggigning enw value to it 

obj.property  -> if a getter retrives some property 
obj.property = new_property_value  -> setter that updates the value of that property 
"""

class student :
    def __init__(self, name):
        name = name.strip()
        self._name = name 
    
    @property  
    def first (self):
        return self._name.split(" ")[0]
    
    @first.setter
    def first (self,str):
        """this is a setter to changs the first name directly affecting the name attribute of the object"""
        l = self._name.split(" ")
        l.remove(l[0])
        l.insert(0,str)
        self._name = " ".join(l)
        
    @property 
    def last (self):
        return self._name.split(" ")[-1]
    
    @last.setter
    def last (self, str):
        """sets a new last name for the student name attribute"""
        l = self._name.split(" ")
        l.remove(l[-1])
        l.append(str)
        self._name = " ".join(l)
        
        
obj = student("aditya is the first name and the last name is pramanik ")
print (obj.name)
print (obj.first)
obj.first = input ("enter new first name :")
print (obj.name)
print (obj.first)
print ()

obj .last = input ("enter new last name :")
print (obj.name)
print (obj.last)
print ()

print ()