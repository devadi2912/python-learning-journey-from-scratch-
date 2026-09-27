# input two numbers find if they are positive negative or zero .. find if its even or odd ... fing the greater of the two numbers 

def positive (a) :
    if a>0 :
        return "positive"
    elif a<0 :
        return "negative"
    else :
        return "zero"
    
def even_odd (a) :
    if a%2==0 :
        return "even"
    else :
        return "odd"
    
def great (a,b):
    if a>b :
        return a
    elif a==b :
        return "same"
    else :
        return b
    
a=int (input ("enter the first number : "))
print ("the number is :",positive(a),"and",even_odd(a))
b=int (input ("enter the second number : "))
print ("the number is :",positive(b),"and",even_odd(b))
c = great(a,b)
if (str(c).isdigit()):      # note that isdigit() only workd for string objects
    print ("the greater of the two entered numbers is :",c)
else :
    print ("the numbers are the",c)
