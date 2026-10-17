"""
have two dictionaries and merge them
"""
dict01 = {
    "a": 1,
    "b": 2
}

dict02 = {
    "c": 3, 
    "d": 4
}

print (dict01)
print (dict02)
for key, value in dict02.items():
    dict01[key] = value
    
print (dict01)