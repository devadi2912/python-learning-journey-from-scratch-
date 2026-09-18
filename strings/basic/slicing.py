'''
string slicing is a tricky concept [::] it has three parameters 
[<parameter 1>::]  -  this is the start index of the string 
[:<parameter 2>:]  -  this is the end index .. string unto this is returned excluding the parameter index 
[::<parameter 3>]  -  this skips n - 1 charaters .. 

the thrid paramter can be understood in a way that the slice returns the sliced string 
then starting from the start charatacter we skip one character at a time 
'''


"""
str[<start index> : <end index> : <step> ]
the slices string returns the string 
starting from the start index unto the end index (exclusive) and skipping <step - 1> characters 
"""

name = "aditya12345678"

for i in name :
    print (i, sep="",end="\t")
print ("string")

for i in range (len(name)):
    print (i, sep="\t",end="\t")
print ("index")


print (name[:])    # prints the entire string 
print (name[5:])   # prints the entire string starting from index 8 
print (name[:7])   # prints the part of the string starting from 0 to 6 index 
print (name[7:13]) # '' ''           '' ''         7 to 12 
print (name[2])    # prints only a single index 2 
print (name[2:13:3]) # prints the string from 2 to 12 skipping 3-1 = 2  characters .. 
