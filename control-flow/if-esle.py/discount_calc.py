'''
Shopping Discount Calculator
Take the total purchase amount:

< ₹1,000 → No discount
₹1,000-₹4,999 → 5%
₹5,000-₹9,999 → 10%
₹10,000+ → 20%

Print the discount and final amount.
'''

purchase_amount = int(input ("enter the purchase amount: "))
discount =0

if purchase_amount < 1000 :
    print ("no discount - the final amount is : " ,purchase_amount)
elif purchase_amount < 5000 :
    discount = (5 / 100) * purchase_amount
    print ("discount amount is",discount," - the final ammount is :",purchase_amount+ discount)
elif purchase_amount < 10000 :
    discount = (10 / 100) * purchase_amount
    print ("discount amount is",discount," - the final ammount is :",purchase_amount+ discount)
elif purchase_amount < 0 :
    print ("please buy something first :)")
else :
    discount = (20 / 100) * purchase_amount
    print ("discount amount is",discount," - the final ammount is :",purchase_amount + discount)
    
