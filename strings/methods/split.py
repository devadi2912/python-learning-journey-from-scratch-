# split is a very inportant method for string operations in python it helps to split strings into a list of iterables based on one or more refernce characters that are considered to be the seperators bases onteh parameter of the plit function

str = input ("enter a string :")
str = str.strip() # this function removes the trailing and leadign spaces from s string 
# str = str.lstrip() # altough redudacn eit removes the leading spaces from the string 
# str = str.rstrip() # removes the spaces but from the right end of the string 
print(f"the string enterd is \n{str} \nsplit based one whitespace the words are \n:{str.split(" ")}")