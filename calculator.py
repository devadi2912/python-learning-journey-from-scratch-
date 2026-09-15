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
    return a-b

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
    a= input("enter the name of the operation that you would like to perform (-222 to exit): ")
    
    a = a.strip().lower()
    
    match(a):
        case "add":
            print ()
            print ("the value of the sum are:",add(int(input("enter the first number :")),int (input ("enter the second number :"))))
            #python switch case dosent require a break .. writting a break here exits teh main while loop !
        case "sub":
            print ()
            print ("the value of sumtraction is :",sub(int(input("enter the first number :")),int (input ("enter the second number :"))))
            #python switch case dosent require a break .. writting a break here exits teh main while loop !
        case "multi":
            print ()
            print ("the product is :",multi(int(input("enter the first number :")),int (input ("enter the second number :"))))
            
        case "div":
            print ()
            print ("the quotient is :",div(int(input("enter the first number :")),int (input ("divided by :"))))
            #python switch case dosent require a break .. writting a break here exits teh main while loop !
        case "int_div":
            print ()
            print ("the integer quotient is :",int_div(int(input("enter the first number :")),int (input ("divided by :"))))
            #python switch case dosent require a break .. writting a break here exits teh main while loop !
        case "mod":
            print ()
            print ("the modulus value is :",mod(int(input("enter the first number :")),int (input ("divided by :"))))
            #python switch case dosent require a break .. writting a break here exits teh main while loop !
        case "exponent":
            print ()
            print ("the exponent value is :",mod(int(input("enter the base number :")),int (input ("enter the power :"))))
            #python switch case dosent require a break .. writting a break here exits teh main while loop !
        case "-222":'e'
            print ()
            print ("exiting the program thanks for trying .. have a great day :\n")
            # exit (0)
            break
            #python switch case dosent require a break .. writting a break here exits teh main while loop !
        case _:
            print ()
            print ("this is the default case :\nplease try again")
            print ()