"""
try :
    ----
except :    # to perform some task if there occurs an error in the try block there can be multiple except blocks
            for    multiple errors
    ----
else :      # to perfrom some operation if there was no error in the try : block else it just executes the except block
    ----
finally :   # ececutes always at the end of the try except block it executes a block of code irrespective of error
    ----
"""

try:
    while True:
        ch = int(input("enter either 0 or 1 :"))
        if ch == 0:
            # generating error
            raise PermissionError("this is a custom thrown error")
            num = 345 / 0
            break
        elif ch == 1:
            break
        else:
            print("please enter a vaid choice ::")
            continue

except Exception as err:
    print("error occured :", type(err))
    print("error occured :", err)

else:
    print("no error :")

finally:
    print("program terminating :")
