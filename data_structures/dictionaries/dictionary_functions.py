"""explores the functions of dictionary object """
test = {
    "rohan" : 34,
    "suresh" : 45, 
    "vivek" :12, 
    "sudha" : 89, 
    "mehek" : 78
}

print (test.keys())    # print the tuple of all the keys of the dictionary 
print (test.values())  # print all the values of all the keys in the dictionary 
print (test.items())   # print the tuples of all the items (key : value) pairs in the dictionary 
print (test.pop("suresh")) # pops the item suresh form the dictionary 
print (test)   # no suresh 

test.clear () # clears all the items in the dictionary 

print ( test, "\nempty dictionary after .clear()")