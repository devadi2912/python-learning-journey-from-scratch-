'''
print the following patter 
*
**
***
****
*****
'''

for i in range (5):
    for j in range (0 , i+1):
        print ("*",end="")
    print ()
    
print ()

# or 
for i in range(1,6):
    print ("*"*i)