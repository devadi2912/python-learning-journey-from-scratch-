"""
wap to create a list of fruits = ["apple", "bannana", "cherry"]
- print the first fruit
- replace bannana with orange 
- print the length of the list 
"""


fruits = ["apple", "bannana", "cherry"]

""" - print the first fruit of the list """
print ( fruits )
# fruits.remove("bannana")
# fruits.insert(1,"orange")
""" - replace bannan with orange """
fruits[1] = "orange"

""" - find the length of the list """
print ( fruits )
print (len(fruits))       # finds the length of the list 
print (fruits.__len__())  # function to find the length of the list 
