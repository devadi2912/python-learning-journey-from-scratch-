# this program is to print the nultiplication table of the number 

n = int (input ("enter the number whose multiplicaiton table is to be displayed: "))
lim = int ( input ("enter the max value till which the multiplication table must print the multipication value: "))

print ()
for i in range (1,lim+1):
    print (f"{n} * {i} =",i*n)