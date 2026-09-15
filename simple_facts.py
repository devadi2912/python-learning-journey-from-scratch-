'''
the return type of print is None so having a print statemnt inside a input function is not ideal for taking an input becase the print function itself returns a value None .. 
a= input (print("hello world")) --> Nonehello world 
a= input ("hello world")        --> hello world 

print (type(print ()))          --> <class 'NoneType'>
'''

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