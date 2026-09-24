'''
the return type of print is None so having a print statemnt inside a input function is not ideal for taking an input becase the print function itself returns a value None .. 
a= input (print("hello world")) --> Nonehello world 
a= input ("hello world")        --> hello world 

print (type(print ()))          --> <class 'NoneType'>
'''

# the type function can also tell us the return type of a function 
def test (a):
    if a==1 :
        return (True)
    elif a==2:
        return ([1,2,3])
    elif a==3:
        return ("this is a string!")
    else :
        return (56.34)
        
print (type(test(1))) # type function returns the return type of a fuction      <class 'bool'>
print (type(test(2))) # type function returns the return type of a fuction      <class 'list'>
print (type(test(3))) # type function returns the return type of a fuction      <class 'str'>
print (type(test(4))) # type function returns the return type of a fuction      <class 'float'>


# int("10") + 5 is 15 
print (int("10") + 5)


def great (a,b):
    if a>b :
        return a
    elif a==b :
        return "same"
    else :
        return b
c = great(int(input("enter the first number : ")),int(input("enter the second number : ")))
if (str(c).isdigit()):      # note that isdigit() only works for string objects
    print ("the greater of the two entered numbers is :",c)
else :
    print ("the numbers are the",c)
    
    
'''
print the following patter 
*
**
***
****
*****
'''
for i in range(1,6):
    print ("*"*i)      # this is sooooo easy and simple you can multiply string also ... in python 
    
    
"""this is the basic of how to use strings in python !!"""

# multi line string 
multi = '''this is a multi line string
and we can easily write paragraphs in this line 
like a poem or a short para 
and print it as is '''

print (multi)


print(end="\n\n")

print ("string indexing :")
'''
in strings indexing starts with 0 .. to print the last character we do -1 this is the last charater of the string
'''

"""
to  convert a character to its equivallent ascii value in python we use string functions chr() and ord() 
ord ('A') : converts a character to its equivallent ascii value 
chr (65)  : converts the ascii vale of the character into their actual character encoding 
"""

print (ord ("F"))                            # 70
print (chr (ord("F")))                       # F 

# to split a string into words in the form of a list use the split functions it takes a string and converts the string into a list sepereating groups of the words with the help of a given reference value 

str = "this is a string with a number of words and the purpose of this string is to demonstrate the fact that the split function has a use case that makes life so much more   easier ! "
print (f"the words in the string above in line 85 are : \n{str.split(" ")} \n this is done with the help of the split function !")


# to print the last n characters of any given string 
str = "any given string ???"
n = 7 # lets say we want the last 7 characters of any given string 
print (str[-n:])