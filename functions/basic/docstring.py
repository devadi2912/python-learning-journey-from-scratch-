""" documentation string is a string in python that is used to describe the purpose of a functions module method or class using the 
<funciton_name>.__doc__ attribute of a funtion """
# the doc string is always written right after the function definition and it described the purpose of a fucntion

def sum ( a , b ):
    """this is a function to add two numbers and return the integer sum of the following """
    return ( a + b )
    
print (sum.__doc__)

def greet ():
    "this is a function with no bofy declared to greet a user"
    print ( "greetings to you human!" )
    
print (greet.__doc__)