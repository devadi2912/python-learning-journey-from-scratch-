# A default argument is a parameter that already has a value assigned to it. If the user doesn't provide a value, Python uses the default.
magenta = "\033[35m"
reset = "\033[37m"
yellow = "\033[33m"


print (reset)

def welcome (name="default", age=-55555):          
    # the default parameter must always be at the end of the parameter list if positional arguments are present 
    
    
    # this is a function to just print a warm welcome message on the terminal screen 
    print (f"this is the terminal screen welcome {yellow}{name}{reset} of age {yellow}{age}{reset} to my git hub repo python journey")
    
choice = int(input (f"do you want to see an output with default age or without default age:\n1st choice a +ve num >0\n2nd choice -ve num <0\nchoice: {magenta}"))

print (reset)
if choice > 0 :
    choice = 1 
elif choice == 0 :
    choice = "something random"
else :
    choice = -1
    
    
match choice :
    case 1:
        name = input (f"enter your name :{magenta}") 
        print (reset)
        welcome (name)
    case -1:
        name = input (f"enter your name :{magenta}") 
        age = input (f"{reset}enter yout age :{magenta}")
        print (reset)
        welcome (name,age)
    case _:
        print (reset)
        welcome ()

        
        
        
print (reset)