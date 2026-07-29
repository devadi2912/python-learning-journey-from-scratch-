# simple calculator progam to apply basic skills 
# using basic skills and string function and basic input with mathch case to write the program 

# the operations to be performed 
# addition subtraction multiplication division integer division modulo and exponential operation 

def add(a,b):
    # this is a funciton to add two values and return the value 
    return a+b

def multi(a,b):
    # this is a function to multiply two functions 
    return a*b

def sub (a,b):
    # function to subtract 
    return a+b

def div (a,b):
    return a/b

def int_div(a,b):
    return ( int (a/b))

def mod (a,b):
    return a%b

def exponent (base , power ):
    return base ** power 

# now writiting the match case part to call the functions accrdingly
while (True):
     
    a=input (print ("enter the function that u want to perfrom \nto exit press -222"))
    if (not a.isalpha()):
        a=a.lower ()
    
    
    match a:
        case "add":
            print ("the sum of both the numbers is :",add(int (input (print ("enter the first number "))),int (input (print ("enter the second number :")))),end ="\n\n")
        case "sub":
            print ("the answer is :",sub(int (input (print ("the first number is :")),int (input (print ("the second number is:"))))),end="\n\n")
        case "multi":
            print("the answer is :",multi(int (input (print ("the first number :"))),int (input (print ("the second number to multiply:")))),end ="\n\n")
        case "div":
            print ("the answer is :",div(int(input (print("enter the numerator :"))),int (input (print ("enter the denominator :")))),end="\n\n")
        case "int_div":
            print ("the answer is :",int_div(int(input(print("enter the numerator:"))),int(input(print("the denominator:")))),end="\n\n")
        case "mod":
            print ("the required answer is:",mod(int (input (print ("enter the value:"))),int (input (print ("mod by:")))),end="\n\n")
        case "exponent":
            print ("the asnwer for the exponent is :",exponent(int(input(print("enter the base:"))),int(input(print("enter the power:")))),end="\n\n")
        case "-222":
            print ("the program is now terminating !!",end ="\n\n")
            exit()
        case _:
            print ("sorry not an option that exists <type in a name the corresponds to one of the functions >")
        
        
        
# this is the end of the program enjoyy !!


