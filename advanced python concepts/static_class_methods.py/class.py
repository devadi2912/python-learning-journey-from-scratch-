"""
Class Methods: These methods are bound to the class itself, not to any
particular instance. They have access to class-level attributes and can be used
to modify the class state. They receive the class itself (conventionally named
cls ) as the first argument.

Class Methods ( @classmethod )
A class method is marked with the  @classmethod  decorator. It takes the class itself
( cls ) as its first parameter, rather than the instance ( self ). Class methods are
often used for:
- Modifying class attributes: They can change the state of the class, which
affects all instances of the class.
- Factory methods: They can be used as alternative constructors to create
instances of the class in different ways.
"""


class Employee:

    _company = "lenonvo"
    _employees = 8000

    # instance method
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        Employee.add_employee()

    def print_employee_info(self):
        info = f"name :{self._name} and salary = {self._salary}"
        print(info)

    @classmethod
    def add_employee(cls):
        cls._employees = cls._employees + 1

    @classmethod
    def change_company(cls, new_company):
        cls._company = new_company

    @classmethod
    def print_company_info(cls):
        info = f"company = {cls._company} and no of employees = {cls._employees}"
        print(info)


e1 = Employee("employee 1", 8975560)
e2 = Employee("employee 2", 1111160)
e1.print_employee_info()
e2.print_employee_info()


Employee.print_company_info()
new_company = input("enter the new comapny name :")
Employee.change_company(new_company)
Employee.print_company_info()
