"""
any method written by defult in a class is consideres as an instance method that has the parameter self that are usually the peoperties of the objects of the class and work on some attributes of the object

static methods are those that can be termes as utility methods in a class that do not require the object to perform an operation (since object passing is heavier and cometimes make the process complex)
declaring a method static with the help of a decorator @staticmethod makes the function a static function

Static Methods: These methods are associated with the class, but they don't
have access to either the instance ( self ) or the class ( cls ). They are
essentially regular functions that are logically grouped within a class for
organizational purposes
"""


class Employee:

    _company = "lenovo"

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    # instance methods
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            print("negative salary not allowed :")

    def print_info(self):
        info = f"name :{self._name}\nsalary :{self._salary}"
        print(info)

    """how ever if i want to have a simple function that just adds any two passed numbers i can do it by declaring the method static with the decorator @staticmethod"""

    # static method
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b

    @classmethod
    def change_company(cls, company):
        cls._company = company


e1 = Employee("kushal", 98333)
e2 = Employee("shruti", 100000)

print(e1.salary)
print(e2.salary)

e1.print_info()
e2.print_info()

print("sum of two numbers :", e1.sum(23.361, 45.210))
# static method was called with the help of the object e1 without actually passing the object to the function


# changing company to asus
print(Employee._company)
Employee.change_company("asus")
print(Employee._company)
