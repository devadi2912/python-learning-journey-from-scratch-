# split is a very important method for string operations in python it helps to split strings into a list of iterables based on one or more reference characters that are considered to be the separators based on the parameter of the split function

str = input ("enter a string :")
str = str.strip() # this function removes the trailing and leading spaces from s string
# str = str.lstrip() # although redundant it removes the leading spaces from the string
# str = str.rstrip() # removes the spaces but from the right end of the string 
print(f"the string entered is \n{str} \nsplit based one whitespace the words are \n:{str.split(" ")}")



'''
the split function cannot take multiple identifiers if specifies it recognises that sequence of characters as the separator to be identified
'''
