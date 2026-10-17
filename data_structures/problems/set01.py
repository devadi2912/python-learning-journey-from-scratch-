"""
create a set my_set = {1,2,3,3,4} and print it to see what happens to duplicate three
- add 5 to the set remove 2 , and check if 4 is in the set 
"""
my_set = {1,2,3,3,4}
print (my_set)
my_set.add(5)
print (my_set)
my_set.discard(2)
print (my_set)
