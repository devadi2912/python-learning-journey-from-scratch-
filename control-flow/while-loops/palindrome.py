# this program checks if a number or a string is a palindrome or not 

n = input ("enter a number or a string to find if it is a plaindrome : ")
cpy = n[::-1]


if n == cpy :
    print ("palindrome!")
else :
    print ("not plaindrome !")