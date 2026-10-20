"""exception handling is a mmethod in python in which we prevent the program from crashing by specifying soem alternatives to performa in case a situation ocurs that crashed the program"""

while True:
    try:
        a = int(input("enter the 1st number :"))
        b = int(input("enter the 2nd number :"))

        print("sum :", a + b)
        ch = int(input("enter a number < 0 to exit the loop :"))
        if ch < 0:
            break
    except:
        print("invalid input")

print("\n")

# python has a lot of different types of error can be seen in the docs
# we can catch that error using the except and acess different attributes of that error as well


while True:
    try:
        print("enter a number to exit the loop")
        word = input("enter a word :").strip().split(" ")[0]
        if word.isdigit():
            # creating an error
            num = 0 / 0
            break

    except Exception as err:
        print(f"error occured :{err}")
        break
