# the find method in python helps find the first occurrence of the sequence of characters in the string it returns an index value if present

''' syntax of the find method in python   string.find(sub, start, end) '''

str= "aditya!!12345 <find this>"
print (str.find("aditya"))
print (str.find("aditya",3))                   # the find function return -1 if the sub string is not found !

print (str.find("find this"))

# the replace functions goes hand it hand with the find function it helps replace a sub string with a new substring ..
''' syntax of the replace method in python  string.replace(old, new, count) here count is the number of occurrences to be replaced its optional'''

print (f"old string: {str}")
print (str.replace("find this","found and replaced"))
print (str.replace("a","$",1))    # replaced only one occurrence of a in the string str