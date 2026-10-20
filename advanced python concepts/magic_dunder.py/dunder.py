"""__init__() is the constructor of a class in python"""


class Employee:

    def __init__(self, name, salary):
        """used for initialising instance variables of an object"""
        self._name = name
        self._salary = salary

    """Human-readable representation"""

    def __str__(self):
        return f"name is {self._name} and salary is {self._salary}"

    """Developer-oriented representation"""

    def __repr__(self):
        return f"name : {self._name}\nsalary : {self._salary}"

    """write your own version of length and what it does with your class objects"""

    def __len__(self):
        """length of the object is the number of characters in the name of the employee"""
        return len(self._name)


obj = Employee("aditya", 89000)

print(obj._name)
print(obj._salary)
print(str(obj))
print(repr(obj))
print(len(obj))
