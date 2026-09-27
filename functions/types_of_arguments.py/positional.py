# Positional arguments are arguments passed to a function based on their position/order.
# Python doesn't know what you meant; it simply assigns arguments according to position.
yellow = "\033[33m"
magenta = "\033[35m"
reset = "\033[0m"

def student (name, age , roll , result ):
    return (f"student details :\n{magenta}name{reset}:{yellow}{name}{reset}\n{magenta}age{reset}:{yellow}{age}{reset}\n{magenta}roll{reset}:{yellow}{roll}{reset}\n{magenta}result{reset}:{yellow}{result}{reset}\n")
    
# passing student details
aditya = student("aditya",19,14200124085,99.5)
neha = student("neha",19,14200124075,95.5)
shreya = student("shreya",19,14200124091,87.3)

print (aditya)
print (neha)
print (shreya)

'''one major problem of positional argument is that the position of the funtional parameters must be known at all times to prevent
acedental wrong initialization of the parameters for example'''


rahul = student(34,"rahul",56.56,14200124065)     #------------> wrong positional arguments 
print (rahul)

# student details :
# name:34
# age:rahul
# roll:56.56
# result:14200124065

# to prevent issues like these we use keyword arguments 
rahul = student (name="rahul",age=34 , result= 45.56, roll= 14200124065)         #------------> keyword arguments 
print (rahul)

# student details :
# name:rahul
# age:34
# roll:14200124065
# result:45.56