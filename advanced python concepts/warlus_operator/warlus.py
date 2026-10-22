"""
warlus (:=) is a simple assignment expresseion inn python that helps you assign values to variables directly inside an expression

it dosent exponentially casuse any difference just that it helps reduce some lines of code
"""

# use case 1 (menu driven while, loop)
while ch := input("enter a number (q to exit) :"):
    if ch == "q":
        break
    else:
        print(ch)

""" 
this is the code without warlus oeprator 
while True :
    ch = input("enter a number (q to exit) :")
    if ch == 'q':
        break 
    else :
        print ( ch )
"""
