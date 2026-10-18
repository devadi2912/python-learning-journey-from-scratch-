"""oprator_overloading in python"""

class Point :
    
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        
    def print_point (self):
        print(f"point : ({self.x},{self.y})")
        
        
    def add_point (self, p):
        return Point(self.x + p.x , self.y + p.y)
    
    
    def __add__(self, other ):
        return Point(self.x + other.x , self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x , self.y - other.y)
    
    def __mul__(self, other):
        return Point(self.x * other.x , self.y * other.y)
    
    def __truediv__(self, other):
        return Point(self.x // other.x , self.y // other.y)
    
    
# here a and b are two points 
a = Point(3,4)
b = Point(4,-1)

a.print_point()
b.print_point()

p = a.add_point(b)
p.print_point()

"""however the add fucntions can also be accon=mplished with the help of operator overloading 
simply by redefining how the + operator would work on two objects of the type class Point
- these can be done with the help of dunders in python (double underscore functions)"""
print (f"\033[33m{dir(a)}\033[37m")

p = a + b  # unsupported operand type(s) for +: 'Point' and 'Point'
# but with overloaded operator the error is resolved  
p.print_point()
p = a - b
p.print_point()
p = a * b
p.print_point()
p = a / b
p.print_point()



"""
__sub__  ( - ),  __mul__  ( * ),  __truediv__  ( / ),  __eq__  ( == ),  __ne__
( != ),  __lt__  ( < ),  __gt__  ( > ),  __len__  ( len() ),  __getitem__ , 
__setitem__ ,  __delitem__  (for list/dictionary-like behavior 
- allowing you to use  []  with your objects)
"""
