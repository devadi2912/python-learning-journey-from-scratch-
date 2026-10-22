"""reduce is a fucntion that takes and function an iterable and reduced to a single item"""

from functools import reduce

# reduce is a function available in a built in module functools

sum = lambda n, m: n + m
l1 = [56, 45, 6, 65, 56, 82, 3, 8, 53, 316, 6881, 3, 516, 789]

print(reduce(sum, l1))
# reduces the iterable to one single value based on the function ..
