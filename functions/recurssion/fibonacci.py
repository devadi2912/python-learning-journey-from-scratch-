# recurssion is a method in a programming language in which a function calls it self to solve a problem by breaking it into smaller sub problems 
# a recursive function usually has two cases the base case and the recurssive case 
# the recursive case is the actual sub problem that is repeatedly executed to solve the problem 
# the base case is the termination condition that stops the recussive call of the function 
# a recurssive funtiona is implemented to reduce the loc in a funcion with a simple logic implementation 


def fibonacci (n):
    if n == 0:
        return (0)
    elif n == 1 :
        return  (1) 
    else :
        return  (fibonacci(n-2) + fibonacci(n-1))

a= int(input("enter the number of terms to be printed! : "))
for i in range (a):
    print (fibonacci (i))