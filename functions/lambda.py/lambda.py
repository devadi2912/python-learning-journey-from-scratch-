"""
lamnbda functions are one line fucntions in python
thay are use for writting simple or complex functions in form that they can be stores in a sigle variable 
so that functions can be passed in python by just passing a variable that has a lambda function .. 
"""


# syntax for writting a lambda function 
# <function name as the variable> = lambda <parameter list without brace> : <function body usually return value> 

sum =  lambda a,b : a+b
product = lambda a,b : a*b
square = lambda a : a*a
cube = lambda a : a*a*a

print (f"the sum of 2 and 3 is {sum(2,3)}")
print (f"the product of 2 and 3 is {product(2,3)}")
print (f"the square of 2 is {square(2,3)}")
print (f"the cube of 3 is {cube(2,3)}")

