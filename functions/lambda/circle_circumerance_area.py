# this program is to find the circumferance of the circle and area using only lambda funcitons
'''
ares = pi*r*r
cir  = 2*pi*r    or   pi * (r + r)
'''
pi = lambda : 3.14                              # returns the constant value of pi
sum = lambda a,b : a+b                          # returns the sum of two numbers 
product = lambda a,b : a*b                      # returns the product of two numbers 
square = lambda a : a*a                         # returns the square of a number 

# circumferance 
cir = lambda product,sum,pi,r : product (pi() ,sum (r,r))           # returns the circumferance of a circle with radius r 

#area 
area = lambda pi ,r,square  : product(pi(),square(r))               # returns the circumferance of a circle with radius r 

radius = int ( input ("enter the value of the radius of the circle : "))
print (f"the circumferance of the circle is \033[35m{cir (product = product , sum = sum , pi = pi , r= radius )} \033[37mand ares is \033[35m{area (pi=pi , r= radius , square = square )}\033[37m")


print ("\033[0m")
