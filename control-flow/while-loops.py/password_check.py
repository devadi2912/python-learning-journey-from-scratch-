# enter a password and verify if the password is the same one or not 
import getpass # this helps hide passwords while entering password 

password = getpass.getpass("enter your password: ")
ver_password = getpass.getpass("re enter your password: ")
while (password != ver_password):
    ver_password = getpass.getpass("incorrect assword please try again: ")
    
print ("successfull re entry of password !")
print ("welcome back !")
