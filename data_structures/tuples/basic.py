""" a tuple is an ordered immutable collection in python that allows duplicate data values and multiple data types """
# a tuple is created with the help of parenthesis 
test = (3) # note :
"""test is not a tuple because a parenthese can be used to group anything in python
there fore if you wan to have a tuple with a single element you will have to end the tuple with a , 
to indicate that the datastructure is a tuple and not simply another group of members with a ()""" 

print (type(test))  # <class 'int'>
test = (3,)
print (type(test))  # <class 'tuple'>

# accessing a tuple can be done in the same way as accessing a list 
test = ("hello", 45, 6, 9, 90, 110, 12.32, "and many more")
print ( test[0] )  # hello
print ( test[3:5] ) # (9, 90)
print (test[::-1])  # reversed tuple 

