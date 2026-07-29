# this is about variables and data types 
# the types of data types in python and how to decalre variables 

# a = 23 
# b = "this is a string"
# print (a+b) # this line will throw an error because the types are not compatable int cannot be added to strings 
# print (a,b) # instead use , for conctatination 

#=========================== data types ========================

#------------------------ 1 numeric .. under numeric we have int float and complex ------------------------------
# int  
# a= 34 ,b = 45 ,c = -45 , d = 2344 

# float 
# a=23.343 , b =3453.00 etc 

# complex 
# a= complex(3,4) ; print ( "complex number a is :",a ) # the output is [complex number a is : (3+4j)]



#------------------------ 2 booleam Ture and False  .. default vaue is False  -------------------------

# ----------------------- 3 string "<string enclosed in double quotes>" ------------------------

# ----------------------- 4 sequence data types : list[] and tuple() ------------------------
# list 
list_a = [1,2,334.343,None ,None ,True,["this is a list in a list ",34],"aditya"]  # lists are mutable ordered and allows duplicates 
print ("list before adding element :",list_a)
list_a.append ("this is a new element added to the end of the list ") # thus mutable 
print ("list after adding new element using the append function :",list_a)

# tuple
tuple_b = ("cat" , 34 ,78.34, 3+3 , None ,True) # not mutable is ordered and is allowes duplicates 
 

#------------------------ 5 mapping type dictionary [key value pairs]-----------------
# dict 
result ={
    "student 1":90,
    "student 2":4,
    "student 5":45
}

#------------------------ 6 None [equivallent to NULL type in c ] ------------------------


# type of function 
c= True
d = "anohter stirng"
e = 67.34553


# the type function 
# since vaiables in python do not have a distinct type it is hard to identify in a large program the type of value stores at a varibels in a given time thus we use the type function 

a1 = 456
b1 = 45.34
c1 = "string"
d1 = complex(9,12)
e1 = True
f1 = ["this is a list"]
f2 = ('this is a tuple',45,56.12)
f3 = {
    "key1" : "apple",
    "key2" : 679
    }

print ("the type of value in b is :",type(b1))
print ("the type of value in c is :",type(c1))
print ("the type of value in a is :",type(a1))
print ("the type of value in d is :",type(d1))
print ("the type of value in e is :",type(e1))
print ("the type of value in f1 is :",type(f1))
print ("the type of value in f2 is :",type(f2))
print ("the type of value in f3 is :",type(f3))

# this below is the output value of the above print statements 
# the type of value in b is : <class 'float'>
# the type of value in c is : <class 'str'>
# the type of value in a is : <class 'int'>
# the type of value in d is : <class 'complex'>
# the type of value in e is : <class 'bool'>
# the type of value in f1 is : <class 'list'>
# the type of value in f2 is : <class 'tuple'>
# the type of value in f3 is : <class 'dict'>