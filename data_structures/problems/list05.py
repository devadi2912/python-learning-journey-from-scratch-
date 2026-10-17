"""
take input of a list and remove all duplicate elements using a set 
"""

test = []
n = int(input ("enter the limit of the number of element in the list : "))
for i in range (n):
    test.append(int(input(": ")))
    
test = list(set(test))
print ("removed allteh duplicate elements from the list :")
print (test)

