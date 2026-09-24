# wap to enter a string and check if the string is alpha numeric or not 

str = input ("enter a string : ")
if (str.isalnum()) :                                          # if the string has space the string will not be considerd to be alphanumeric 
    print (f"the entered string \033[34m{str}\033[37m is alpha numeric")
else :
    print (f"the entered string \033[33m{str}\033[37m is not alpha numeric")