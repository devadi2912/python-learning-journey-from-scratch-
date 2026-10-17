"""
find the highest priced product from a dictionary of products and prices
"""
products = {
    "tv" : 89000,
    "laptop" : 100000,
    "mobile" : 10000
}

max = 0 
for key,value in products.items():
    if value > max :
        max = value
        
for key,value in products.items():
    if value == max :
        print (f"the product with the maxumum value is : {key}")
        break
    
print()

# orrrr we can simply do 
value = products.values()
value = list(value).sort()
max = list[-1]

for key,value in products.items():
    if value == max :
        print (f"the product with the maxumum value is : {key}")
        break
