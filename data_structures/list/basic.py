
"""a list is an ordered mutable collection in python that allows duplicate data values and multiple data types """
marks = [34, 51, 23, 6, 89, 34] # index starting from 0 to list length -1 
mixed = ["hello", 56, True, [34, 51, 23, 6, 89, 34], None]

print ( marks )
print ( mixed )
for i in marks :
    print (i)
for i in mixed :
    print (i)

# accessing elements of a list can always be done with the help of for loops but they can also be accessed indivisually
print ( marks[4] ) # this will access the element at the 4th index of marks 


# list slicing ( follows the same rules as string slicing )
print ( marks[3:4] ) # [6]
print ( mixed[::-1] ) # reversing a list  

print ( marks[3:6] ) # no error 