# wap to enter a string and check if the string is a aplindrome or not 

magenta = "\033[35m"
yellow = "\033[33m"
reset = "\033[0m"

text = input (f"enter a string to  check if the string is plaindrome or not :{magenta}")
print (reset)

text = text.strip().lower()
if (text == text[::-1]):
    print (f"the string {magenta}{text}{reset} {yellow}is a plaindrome{reset} ")
else :
    print (f"the string {magenta}{text}{reset} {yellow}is not a plaindrome{reset} ")
