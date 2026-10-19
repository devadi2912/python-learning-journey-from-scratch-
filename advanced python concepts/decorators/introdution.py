"""a decorator in python is a functions that accepts another function and adds or modifies its behaviour and returns the new function """

def decorator (func):
    def wrapper ():
        print ("before function execution ...")
        func()
        print ("after function execution ...")
        print ()
    return wrapper

def greet ():
    print ("hello")
    
# one way for calling the decorated function 
greet = decorator(greet)
greet()

# better way for this is by using decorater syntax 
@decorator
def thank ():
    print ("thankyou user ...")

thank()


