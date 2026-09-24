# in the string "coding in python is fun" replace "fun" with "awesome"

purple = "\033[35m"
reset = "\033[37m"

print (f"this is a demo string with some demo words {purple} this is purple string {reset} now its reset ")



text = "coding in python is fun!"

print (f"new string \033[35m{text.replace("fun","awesome")}\033[37m")
# find the index of the word pyhton in the above string