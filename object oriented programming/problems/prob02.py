"""
create a class person with a constructor __init__ in it that accepts age and name as arguements and stores them as instance vales for an object 

create an object and print the persons name and age 
"""

class person:
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age

a = person("aditya" ,34)
print (a.name,a.age,sep="\n",end="")