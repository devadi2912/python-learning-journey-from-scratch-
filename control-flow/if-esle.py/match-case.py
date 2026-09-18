# this is the python equivallent of switch case and helps createe a menu driven construct .. it is a comparatively recent addition and was added in python 3.1


'''
syntax
choice =34
match choice :
    case 1 :
        < code block no break statement required >
    case 2 :
        <code block no break required >
    case 3 :
        < make sure that the indentation is accurate >
    case _ : 
        < this is the default case for handling exceptions >

'''


# implementing a lottery system 

choice = int (input("enter a number between 1 to 10 : "))

match choice :
    case 5 :
        print ("you won a car !")
    case 2 :
        print ("you won a bike !")
    case 7 :
        print ("you won a camera !")
    case 9 :
        print ("you won 2$ !")
    case _ :
        print ("better luck next time !")
