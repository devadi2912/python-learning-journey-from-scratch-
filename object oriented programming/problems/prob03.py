"""
create a base class Animal with a method sound that prints "some sound"
create a derived class Dog that over writes the method sound and prints "Bark!"
create an object of the class and call the funciton sound 
"""

class Animal :
    
    def __init__(self, name):
        self.name = name 
        
    def sound (self):
        print("some sound ..")
        
    def get_info (self):
        print (f"my name is {self.name}")
        self.sound()

class Dog(Animal):
    
    def __init__(self, name):
        super().__init__(name)
        
    def sound (self):
        print ("Bark!")
        
obj = Dog("bruno")
obj.get_info()
Animal.sound("test")