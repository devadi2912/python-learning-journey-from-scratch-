"""lsit comprehension is a quick way to create a lsit in which every element has a uniform condition in a range o number or another list """

# create a list of the table of number n 
"""
n = int ( input ("enter a number to print the table of that number"))
table = []

for i in range (1,11):
    table.append(n*i)
    
an easier way to do this is with the helo of list comprehension 
"""
n = int(input("enter a number to print the table of that number: "))
table = [n*i for i in range (1,11)]

square = [i*i for i in table] # square of the table 
print (table,square,sep="\n")
