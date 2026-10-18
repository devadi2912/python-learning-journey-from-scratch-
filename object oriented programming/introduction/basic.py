"""object oriented programming is a concept that models real world entities and attributes into our program"""

"""a class is a template similllar to any object oriented language like jave etc it has the same functions to provide with the base attributes and members on which other classes or models can be build on 

- object is an instance of a class i.e it is a branch of a class that has the basic template provided by the class along with some extra definitons and values as per its requirements .. it uses the basis class template but modulede as per requirements .. """

class Employee:
    company = "Rubrik"
    # self is mandatory as the first parameter for every method in a class 

    def get_salary (self):     # self here is simillar to this is java it referes to the current object calling the method
        return 34000 
    
# the keyword self is required in every method of a class 

# creation of an object 
e = Employee()   # calling the class constructor 
print(type(e))   # <class '__main__.Employee'>

print(e.get_salary())
e2 = Employee()
print(e2.get_salary())   

"""no need to pass a parameter for the self in the method definition that is implied from the object that calls the method"""


