"""this file covers some common functions of the data structure set"""
s = {45,"hello",89,63.5}

s.add("new element") # functions to add elements into the set 
s.remove("new element") # function to remove an already present element in the set throws error otherwise 
s.discard("hello world") # function to remove element if present it does not throw an error if element is not preset 
s.pop() # removes a random element from the set ( this happens because the set it not ordered )

# set operations in python using built in functions 
a= {1,2,3,4,5}
b= {1,2,3}

c= a.union(b)  # all the distinct elements of a and b 
d= a.intersection(b) # all the elements of a that are also present in b 
e = a.difference(b) # set operation a-b = a intersections b complement 

print (c)
print (d)
print (e)