"""decorators can also be used for repeating a functions multiple time dynamically"""

def repeat (n):
    def decorator (func):
        def wrapper (a):
            for i in range (n):
                func(a)
        return wrapper 
    return decorator 

@repeat(4)
def greet (name):
    print (f"hello {name}")
    
greet ("aditya")


# or i can run the function with a user returned repeat parameter as well .. 
times = int (input ("enter the number of times the repeat function should work : "))

@repeat(times)
def greet (name):
    print (f"hello {name}")

greet ("robin")

