"""there can be instance attributes and class attributes in python .. """

class Employee:
    company = "lenovo" # this is the class attribute 

    def __init__(self, name, salary, designation, company = None ):
        self.name = name 
        self.salary = salary 
        self.designtion = designation
        if company :
            self.company = company # these are the instance attribute associated to the objects
        else :
            pass 
        # class attribute companny is being overwritten to an object attribute 

    def get_company (self):
        return self.company 
    
    def get_salary (self):
        return self.salary 
    
    def get_info (self):
        print (f"name of the employee is {self.name}")
        print (f"company of the employee is {self.company}")
        print (f"salary of the employee is {self.salary}")
        print()
        
e1 = Employee("aditya",120000,"ai developer","DELL") # leaving the company as default 
e2 = Employee("john doe",35000,"product manager", "HP") # overwritting the company attribute  


print (e1.get_company())
print (e2.get_company())

# printing any attribute using an object prints the object attribute for that instance 
print ("instance attributes : ",e1.company,",",e2.company)

# printing the class attribute of the class can also be done in the following manner 
print ("class attributes : ",Employee.company)