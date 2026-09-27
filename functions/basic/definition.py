# a functions is a reusable block of code in python that helps perform a specific task without having ot write the logic repeatedly for that task 
# it improves the modularity and the robustess of a python program 

# the definition of a fucntion in  python comprise of 
'''
def          -  a key word that indicates that the specific block of code is a functions and not a normal indented block of code
unique identifier - this namming follows the same namming rules that are used for variable identifiers 
paramter list - may be empty or have a list of variables depending on the operations performed 
def <identifier_name> (<list of parameters>) :
    # function body 
    # return (<value or variable if any>)
'''


def greetings (name):
    return (f"hello {name}!")

a= input ("please enter your name: ")
print (greetings(a))