# the find method in python helps find the first occurance of the sequence of characters in the string it returns an index value if present 

''' syntax of the find method in python   string.find(sub, start, end) '''

str= "aditya!!12345 <find this>"
print (str.find("aditya"))
print (str.find("aditya",3))                   # the find fucntion return -1 if the sub string is not found !

print (str.find("find this"))

# the replace functions goes hand it hand with teh find funtion it helps replace a sub string with a new substring .. 
''' syntax of the replace methon in pthon  string.replace(old, new, count) here count is the number of occurances to be replaced its optional'''

print (f"old string: {str}")
print (str.replace("find this","found and replaced"))
print (str.replace("a","$",1))    # replaced only one occurance of a in the string str