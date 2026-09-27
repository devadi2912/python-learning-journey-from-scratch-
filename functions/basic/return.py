# in the following block of code even tough everything seems rigth the variables o1 and o2 is not initialised by the return value of the function avg 

def avg_no_return (a,b,c):
    print ( (a+b+c)/3.0 )
    
o1 = avg_no_return (2,2,2)
o2 = avg_no_return (9,3,6)  
    
print (f"the value of o1 is {o1}")      # here the value of o1 and o2 are none because the functio dosent return a valtue upon being called 
print (f"the value of o2 is {o2}")      # to get the value we use return keyword to ensure that the return keyword


def avg_return (a,b,c):
    print ( (a+b+c)/3.0 )
    
o1 = avg_return (2,2,2)
o2 = avg_return (9,3,6)  
    
print (f"the value of o1 is {o1}")      # here the value gets printed becase the functios avg_return returns the avg value
print (f"the value of o2 is {o2}")      # 

