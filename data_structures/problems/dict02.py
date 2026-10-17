"""
create a dictionary  of three friends with their phone numbers 
- keys() to get all names  
- values() to get all phone numbers 
- items() to loop over key value paris to print them 

"""

friends = {
    "john" : 8564231564,
    "markus" : 4523165987,
    "lily" : 7512365498
}

print (friends.keys())
print (friends.values())
print (friends.items())
print ()

for i in friends.items() :
    print (f"name {i[0]} : phone number {i[1]}")
    
print()


for key,value in friends.items() :
    print (f"name {key} : phone number {value}")

