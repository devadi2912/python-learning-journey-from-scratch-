"""inheritance and polymorphism"""

class Animal :
    location = "animal world"

    def __init__(self, name):
        self.name = name 
    
    def speak (self):
        print ("animal is speking (parent class method Aminal)")
        

# inherited class form animal 
class Dog(Animal):
    
    def speak (self):
        print (f"Woof! i am a {self.name}")
              
class Cat(Animal): # this is how a sub(clid) class inherits form a super(parent) class 
    
    def __init__(self, name):
        super().__init__(name) # the super() keyord calles the parent constrcutor 
        # it is not called implicitly and should be written always to invoke the parent constructor 
    
    def speak (self):
        super().speak()
        print (f"meaow! i am a {self.name}")
        
d = Dog("bruno")
c = Cat("luna")

d.speak()
c.speak()

# class attributes can also be attributes through objects since they have not been overwritten here 
print (d.location)
print (c.location)

# print ( d.speak(),c.speak() ) returns none becasue the functions speak() returns nothing (None)
# super keyword lts us access the aprent classes attributes and methods directly from the subclass 