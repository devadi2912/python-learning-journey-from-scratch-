# this is a single line comment 
'''
this is a multi line comment 
'''

""" 
this is also a multi line comment 
"""

# about print statements 
# the default seperator and the end character of every print statement in python is a " " and a "\n" by default respectively 

# so if we write a program such as 
for i in range(21):
    print (i,i+1)
print ('above the default seeprator in the print statement is a " " and a "\\n" by default respectively ')

print ("these characteristics of python can be over written by the parameters sep and end :")

for i in range (21):
    print (i,i+1,sep="\t<this is the seperator>\t", end="\t:(this is the end\n")