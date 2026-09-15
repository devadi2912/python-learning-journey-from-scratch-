'''
this is a multiline comment 
'''
# this on the other hand is a single line comment 

a= 34 
b= "34"
# this is not valid because the addition of a string to a integer is not possible  this will through an error
# c= a+b     

b= int (b)   # type casting string b into an integer type to perform addition 
c= a + b     # this will not through an error becasue b has been converted to an integer type value 
print (c)    
print (type(c))  

# functions that are generally used for type casting from one data value to another 
# int () converts to int 

test = 34.34 
print (int (test))  # 34 
print (bool (test)) # True because the varable is not 0 or none type 

test = 56 
print (float (test))  # 56.0

test = "this is a string type value "
print ( list (test) ) 
# ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 't', 'y', 'p', 'e', ' ', 'v', 'a', 'l', 'u', 'e', ' ']

print (set (list (test)))
# {'a', 'e', 'r', 'n', 'g', 's', 'l', 'h', 'y', 'p', 'v', 'u', ' ', 't', 'i'} tuple has not duplicate characters 

'''
note that a string can only be converted into anoter type if it has an equivalent value of that type 
test = "number"
print (int (test) ) -- this will lead to an error 
'''
