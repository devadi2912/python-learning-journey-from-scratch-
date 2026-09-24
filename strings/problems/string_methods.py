# take a string "  i love python programming  "  remove the spaces from both ends conver it to title case and then coun tthe number fo times o appears in the string 

str = "  i love python programming  "
print (str.strip()+":stripped the spaces from the string ")
print (str.strip().capitalize()+": convertes the string to title case ")

print (str.upper().strip())
print (str.lower().strip())

count =0
for i in str :
    if i == "o":
        count = count +1
print (f"the number of occurace of the character \033[35m\"o\"\033[37m in \033[35m{str}\033[37m is = \033[35m{count}\033[37m")

# or we can do 

print (f"the occurances of \033[35m\"o\"\033[37m in the string is \033[35m{str.count("o")}\033[37m")

print (f"the firrst index of \"python\" in the string \033[32m{str}\033[0m is \033[35m{str.lower().index("python")}\033[0m")