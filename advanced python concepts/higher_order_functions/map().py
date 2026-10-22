"""map is a higher order function that applied a funciton to every item in an iterable (such as a list or a tuple)"""

# syntax of map ...  map (function , interable)
l1 = [2, 3, 4, 5, 6, 7, 8, 9]
str = "this is a string object"
str = str.split(" ")

print(map(lambda n: n * n, l1))  # <map object at 0x00000200AF4B4160>
# this map function returns by default an object
# however this object can be type casted to list explicitly

print(list(map(lambda n: n * n, l1)))  # [4, 9, 16, 25, 36, 49, 64, 81]
print(list(map(lambda n: n.upper(), str)))


# this is another way for list comprehension
