"""apply for driving liscence"""

name = input("enter name :")
age = int(input("enter age :"))

if age < 18:
    raise ValueError("condition not meet come back when you grow up")
else:
    print(f"drivers lisence with name :{name} and age :{age} sacntioned !")

# i can raise any error i want in python as and when required by the program using raise
