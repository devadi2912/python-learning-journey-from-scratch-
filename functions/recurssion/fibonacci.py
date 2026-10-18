# recursion is a method in a programming language in which a function calls it self to solve a problem by breaking it into smaller sub problems
# a recursive function usually has two cases the base case and the recursive case
# the recursive case is the actual sub problem that is repeatedly executed to solve the problem 
# the base case is the termination condition that stops the recursive call of the function
# a recursive function is implemented to reduce the loc in a function with a simple logic implementation
# infinite recursion is when the base case is not executed and the logic is not correct

def finbonacci ( n ):
    # base case 
    if n == 0:
        return 0
    elif n ==1 :
        return 1
    else :
        return ( finbonacci( n-1 ) + finbonacci ( n-2 ))

num = int ( input (f"enter the number of fibonacci series terms to be printed on the terminal screen :"))
for i in range ( num ):
    print (f"{i+1:<4} term :{finbonacci(i)}")