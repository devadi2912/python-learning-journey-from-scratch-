"""
Employee Management System 🧑‍💻

Create a class-based employee management system.

Requirements:

Create an Employee class with a class attribute company = "TechCorp".
Its constructor should accept name, employee_id, and salary.
Create a method display_info() to display employee details.
Create a method give_raise(amount) to increase the employee's salary.
Create a class attribute that tracks the total number of employees created.
Create 3 employee objects and store them in a list.
Use a loop to display all employees.
Find the employee with the highest salary.

Challenge: Allow an employee to have a different company without changing the class attribute for other employees.
"""

class Employee :
    company = "TechCorp"
    count = 0 
    
    def __init__(self,name,employee_id,salary): 
        self.name = name 
        self.employee_id = employee_id
        self.salary = salary
        Employee.count = Employee.count + 1
        
        
    def display_info (self):
        print (f"name :{self.name}\nid :{self.employee_id}\nsalary :{self.salary}\ncompany : {self.company}")
        print ()
        
    def give_raise (self, increment ):
        self.salary = self.salary + increment
        self.display_info()

e1 = Employee("employee1","123",56000)
e2 = Employee("employee2","124",57000)
e3 = Employee("employee3","125",89000)

emp_list = [e1,e2,e3]
for i in emp_list:
    i.display_info()
    
ch = input ("enter the employee id of the employee whose company you want to change :")
match ch :
    case "123":
        e1.company = input ("enter new company name: ")
        
    case "124":
        e2.company = input ("enter new company name: ")
        
    case "125":
        e3.company = input ("enter new company name: ")
        
    case _:
        print ("invalid exployee id !") 

for i in emp_list:
    i.display_info()
    
salary_list = [e1.salary, e2.salary, e3.salary]
print ("max salary is",max(salary_list))