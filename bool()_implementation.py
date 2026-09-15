'''
this is a program to identify if the program has a valid input or not 
'''

name = input ("enter your name: ")
print (name)
print (bool(name))

if bool(name):
    print ("a valid name is entered!")
else :
    print ("no name enetered!")
    
# however in python automatically detects if the name is empty : 

test = input ("enter something that u want to say : ")
print (test)

if test :
    print ("the user has entered a valif string input !")
else :
    print ("the user has not eneted a string as input ")