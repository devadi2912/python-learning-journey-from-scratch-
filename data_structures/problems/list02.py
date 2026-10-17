"""create a list with numbers from 1 to 10
- print the first three numbers using string slicing 
- print the last three numbers using string slicing """

numbers = [i for i in range (1,11)]
# first three 
print (numbers[:3])
# last three
print (numbers[-3:])