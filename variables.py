age = 43 # integer type value 
name = "aditya" # sting type 
cgpa = 9.902  # float type 
#  = is the assignment operator 
 
#  the types of variables in python include integer , float , boolean , string , list , tuples , dictionaries 

print (type(age))        # <class 'int'>
print (type(cgpa))       # <class 'float'>
# the type function can also tell us the return type of a function 
def test (a):
    if a==1 :
        return (True)
    elif a==2:
        return ([1,2,3])
    elif a==3:
        return ("this is a string!")
    else :
        return (56.34)
    
    
print (type(test(1))) # type function returns the return type of a fuction      <class 'bool'>
print (type(test(2))) # type function returns the return type of a fuction      <class 'list'>
print (type(test(3))) # type function returns the return type of a fuction      <class 'str'>
print (type(test(4))) # type function returns the return type of a fuction      <class 'float'>