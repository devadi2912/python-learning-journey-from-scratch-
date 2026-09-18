# this is a program to find the sum of digits of the entered number 

n = input ("enter a number : ")
sum=0 
for i in n :
    sum =  sum + int(i)
    
print ("the sum of the digits of the entered number are:", sum )