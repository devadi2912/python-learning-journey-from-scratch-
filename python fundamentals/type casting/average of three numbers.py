'''Take three numbers as input and calculate their average.'''

print ("enter the number whose average si to be found seperated by a single \' \' for ex")
print ("12 34 45 23 12 45 17 52")
# using split function for the seperation of numbers from the enteres string 
# split function returns a lit based on a seperator value 
numbers = input ("enter the numbers based on the format specifies above: ").split (" ")
sum = 0.0
count =0 
for x in numbers :
    sum = sum + float (x)
    count = count +1
    
print ("the avarage of the enteres numbers is: ",sum / count )