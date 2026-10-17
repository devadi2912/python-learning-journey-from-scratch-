"""a dictionary in python is a mutable collection key value pair that allow quick look up into values for an attribute """
# note : the keys in a dictionary must be hashable 
# a hashable object is a one that is immutable and remains constand through its lifespan 
marks = {
    "rohan" : 34,
    "suresh" : 45, 
    "vivek" :12, 
    "sudha" : 89, 
    "mehek" : 78
}


# accessing dictionary : can be done with the help of the keys directly 
for i in marks :
    print (f"marks of {i:<8} is {marks[""+i]}")    
print ()

# changing the content of a key in a dictionary can be done easily 
marks["suresh"] = 89900
for i in marks :
    print (f"marks of {i:<8} is {marks[""+i]}")    
print ()
    
# adding more entries and values into the dictionary is also possible 
marks["new stud"] = 99 
print ( type(marks) )
print ( marks ) # mornal print layout of a dictionary 