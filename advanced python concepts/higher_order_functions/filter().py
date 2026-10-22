"""the filter() function selects items form an iterable that satisfy a condition
syntax - filter(function , iterable)"""

l1 = [45, 5, 65453, 3434, 242, 243, 4, 32, 65, 89]

"""
def greater_9 (n):
    if n > 9 :
        return True 
    else :
        return False
      
or the lambda equivallent to this function is
lambda n : n > 9
"""

print(
    filter(lambda n: n > 9, l1)  # <filter object at 0x0000022713C94280>
)  # this will simillar to map functions return an object that can be converted to a list
print(list(filter(lambda n: n > 9, l1)))  # [45, 65453, 3434, 242, 243, 32, 65, 89]
