# here we learn about the methods that are used to check the type of the string or character number space alpha numeric and so on 

str = input ("enter an alpha numeric sentence and we will print the type of the words : ")

arr = str.split(" ")

print (f"here are the indivisual words of the enteres sentence : {arr}")

for i in arr :
    verdict =""
    if (i.isdigit()):
        verdict = "number "
    elif(i.isalnum()):
        verdict = "alpha numeric "
    elif(i.isspace()):
        verdict = "white space "
    else :
        verdict = "aplhabets "
    
    print (f"word: {i} \t verdict: {verdict}")