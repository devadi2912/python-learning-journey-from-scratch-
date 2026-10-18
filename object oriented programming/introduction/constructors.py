"""constructors are special methods in object oriented programming that have the same name as the class name and can be used to initialise an object .. they can be overloaded to create parameterized constructors"""

class Employee :
    # this is the constructor for the class
    def __init__(self,name,company,salary,bond=4):
        self.salary = salary
        self.name = name # create a new instance for this object called name and assign the value name into it ..
        self.company = company 
        """in python we declare the attributed of a class (variables) inside the init function that is called when ever an object is created with the help of the self parameter"""
        self.bond = bond  
        
    def get_salary (self):
        return self.salary
    
    def get_info (self):
        print (f"name of the employee is {self.name}")
        print (f"company of the employee is {self.company}")
        print (f"salary of the employee is {self.salary}")
        print (f"bond of the employee is {self.bond}")
        print()
    
# self is the key word for the current object that invokes the constructor 
# the __init__ () function is used to initialise the current object 

e1 = Employee("john","microsoft",56000,5)
e2 = Employee("lily","nvidia",45000)
e3 = Employee("bruno","google",100000,10)

print (f"{e1.name} {e1.company} {e1.bond}")
print (f"{e2.name} {e2.company} {e2.bond}")
print (f"{e3.name} {e3.company} {e3.bond}")
print ()

e1.get_info()
e2.get_info()
e3.get_info()
