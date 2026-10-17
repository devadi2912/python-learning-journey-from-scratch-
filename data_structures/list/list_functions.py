""" this file will cover all the important list functions ... """
my_list = ["hello", 'g', False, None, 45, 56, 92, 12, 30, 3, 5, 7]

print (my_list.__doc__) # docstring of the list functions 
print (my_list.count(45)) # counts the number of occurences of the specifier value in the list 


print (my_list.append("new element")) # note that the return type is none 
"""this is because list is a mutable data structure and every list finction changes the original list and dosent return a new list object unlike string that are immutable and thus every string method that is run needs to be assigned back to the original string """
print (my_list) # this will show the new element in the list because it was appended 

# other functions 
my_list.remove("new element")
print (my_list)

my_list.insert(3,1102) # takes two parameters ( <index> , <value> )
# the insert function in the list adds the values to the start unlike the append function that adds to the end of the list 
print (my_list)

my_list.extend(["welcome", "user"]) 
# the extends function combine the elements of the new lsit into the target lsit mentioned to make a list containg both the elements ( note that a list can have duplicate elements )
print (my_list)

print (my_list.index("welcome"))

my_list.reverse() # reverses a list 
print (my_list)

"""
my_list.sort()
will throw an error because the list has both strings and integers and python cannot compare then directly 
to sort them use homogeneous data or sort them as strings 
my_list.sort(key=string)
"""

my_list.sort(key=str)
print (my_list)  # prints the sorted list comparing everything as strings 

numbers = [47, 12, 89, 3, 56, 21, 74, 8, 63, 35, 91, 16, 42, 5, 78, 29, 60, 14, 83, 37]
numbers.sort()
print (numbers) # sorted list of numbers 

print (len(numbers))      ## to find the number of elements present in the list numbers 
print (numbers.__len__()) ## also to find the number of elements present in the list numbers 