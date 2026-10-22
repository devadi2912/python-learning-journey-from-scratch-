"""args and kwargs in python helps a function accept variable arguments in the form of a tuple"""

# for ex

sum1 = lambda a, b: a + b
print(sum1(56, 44))
try:
    print(sum1(9, 12, 3))
    # this will throw an error because the number of marameters do not match the input expression types
except Exception as err:
    print("error occured :", err)


# this problem can be solved with args
from functools import reduce


def sum(*args):
    # args is a variable that will contain all the values passed to sum function in the form of a tuple
    print(args)
    if len(args) > 1:
        return reduce(lambda a, b: a + b, args)
    else:

        if args:
            return args[0]
        else:
            raise IndexError("arguments is empty! ")


print(sum(4))
print(sum(89, 34, 45))
print(sum(89, 34, 45, 56862))
print(sum(89, 34))
print(sum())
