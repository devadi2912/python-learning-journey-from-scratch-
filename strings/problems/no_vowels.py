# this progrma is to heck th number of vovels in the given string 

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
reset = "\033[0m"



text = input (f"enter a verry large strign with lots of vovels to test the limits : {magenta}")
print (reset)
text = text.lower()
vov = ["a","e","i","o","u"]
count =0 

for v in vov :
    count = count + text.count(v)

print (f"the number of vovels in the string {yellow}{text}{reset} is :{magenta}{count}{reset}")