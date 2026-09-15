# more on print statements .......... prarpeter sep and end 
# normal print statement comes with hidden optional parameter that makes formating output strings easier 
# .sep = "<seperator character >" this is a parameter of the print function that helps replace the default white space character with another favourable character 

print ("hello","world","this","is","a","declaration that i am going to be the best python developer in","the world")
print ("hello","world","this","is","a","declaration that i am going to be the best python developer in","the world",sep = "@@")
# note that the default seperator in the second print statement is over written by @@ wherever , is used 
 

# there is another parameter that changes the end character for that current print statemnt 
# the end parameter by default is \n to change this we use end ="<custom end character>"
for i in range (0,11):
    print (i)
    # the default value in python for every print statement is \n so every print statement is printed on the new line 
print ("\n")
for i in range(0,11):
    print (i,end="") # \n replaced by null 
print ("\n")
for i in range(0,11):
    print (i,end=" <i am the new end character> ")
print ("\n")
for i in range(0,11):
    print (i,end=" $ ")
print ("\n")


