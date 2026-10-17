"""a set is an unordered mutable collections of objects (values) , where suplicate values are not allowed"""
# a set is created with curly braces 
s = {45,"hello",89,63.5}
print ( type(set) )

# accessing set elements is not possile in the manner 
# print ( s[0] ) # becasue a set is not ordered  ('set' object is not subscriptable)
"""
imagine set to be like a basket where things are dumped in any random order therefore at any time we can add elements to the set with .add() or remove with .remove() but we cannot access elements from a set 

s.add("hello") dosent throw an error but it dosent add another instanve of "hello" now that hellos is present in s 
"""

s.add("hello")
print ( s )