"""
\033[30m → Black
\033[31m → Red
\033[32m → Green
\033[33m → Yellow
\033[34m → Blue
\033[35m → Magenta
\033[36m → Cyan
\033[37m → White
\033[0m  → Reset
"""

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
reset = "\033[0m"





name = input ("enter your name!: ")

print(f"Hello \033[30m{name}\033[0m, welcome!")
print(f"Hello \033[31m{name}\033[0m, welcome!")
print(f"Hello \033[32m{name}\033[0m, welcome!")
print(f"Hello \033[33m{name}\033[0m, welcome!")
print(f"Hello \033[34m{name}\033[0m, welcome!")
print(f"Hello \033[35m{name}\033[0m, welcome!")
print(f"Hello \033[36m{name}\033[0m, welcome!")
print(f"Hello \033[37m{name}\033[0m, welcome!")
print(f"Hello \033[0m{name}\033[0m, welcome!")


# or we cna use the string in the form of variables like the ones below 

text = input("tell me something about you that u love to do in your free time :\033[35m")
print (reset)
print (f"you said that in your free time u like to {black}\"{text}\"{reset} ")
print (f"you said that in your free time u like to {red}\"{text}\"{reset} ")
print (f"you said that in your free time u like to {green}\"{text}\"{reset} ")
print (f"you said that in your free time u like to {yellow}\"{text}\"{reset} ")
print (f"you said that in your free time u like to {blue}\"{text}\"{reset} ")
print (f"you said that in your free time u like to {magenta}\"{text}\"{reset} ")
print (f"you said that in your free time u like to {cyan}\"{text}\"{reset} ")
print (f"you said that in your free time u like to {white}\"{text}\"{reset} ")



# or we can use a function to print the text to any desirable color only with the help of a function
def print_color(text, color):
    print(f"{color}{text}{reset}")

print_color("Hello Adi!", red)
print_color("Python is fun!", green)
print_color("I am learning!", cyan)