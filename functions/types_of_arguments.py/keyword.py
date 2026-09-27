# keyword arguments 
# Keyword arguments are arguments passed to a function using the parameter name.

def greet(name, age):
    print("Name:", name)
    print("Age:", age)

greet( age=20,name="Aditya")      # order dosent matter when using keyword arguments
# however all the key words neeed to be known befh=ore hand ot use these types of arguments 


''' positional and keyword arguments can be mixed up and used simultanously but 
the positional arguments must always come before the keyword arguments '''

greet ("ashmita",age = 50000)       # positional before the keyword arguments 