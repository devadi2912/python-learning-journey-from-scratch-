# this program is to find the reverse of an enterd string using the concept of negative indices 

str = input ("enter a word : ")

for i in str :
    print (i, sep="",end="\t")
print ("string")

for i in range (len(str)):
    print (i, sep="\t",end="\t")
print ("index")

print ("printing the string in reverse: ")
print (str)


i=1
while (True):
    if (i-len(str) > 0 ):    # if i is greater then the length then the string is out of bounds .. 
        break
    print (str[-i],sep="",end="")
    i=i+1
    
