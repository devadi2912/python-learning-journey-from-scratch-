# printing the truth table of the basic logic gates one after another 
# based on the logic 

def convert (a):
    if (a == True):
        return 1 
    else :
        return 0
    


print ("bool (0): ",bool (0) ,"\t", "bool (1) :",bool (1), end="\n\n")

print ("and (.) gate logic :\na\t b\tand")
for i in range (0,2):
    for j in range(0,2):
        print (i,"\t",j,"\t",i and j)
print ()

print ("or (+) gate logic :\na\t b\tor")
for i in range (0,2):
    for j in range(0,2):
        print (i,"\t",j,"\t",i or j)
print ()

print ("not (!) gate logic :\na\tnot")
for i in range (0,2):
    print (i,"\t",convert(not(i)) )
print ()

print ("nand (!.) gate logic :\na\t b\tnand")
for i in range (0,2):
    for j in range(0,2):
        print (i,"\t",j,"\t",not(i and j))
print ()

print ("nor (!+) gate logic :\na\t b\tnor")
for i in range (0,2):
    for j in range(0,2):
        print (i,"\t",j,"\t",not(i or j))
print ()