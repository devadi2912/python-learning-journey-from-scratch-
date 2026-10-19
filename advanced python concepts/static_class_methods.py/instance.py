"""
Instance methods are the default type of method in Python classes. They require
an instance of the class to be called, and they automatically receive the instance as
the first argument ( self ).

Instance Methods: These are the most common type of method. They operate
on instances of the class (objects) and have access to the instance’s data
through the  self  parameter.

class Dog:

    def __init__(self, name):
        self.name = name  # Instance attribute

    def speak(self):
        return f"{self.name} says Woof!"

    dog = Dog("Buddy")
        print(dog.speak()) # Buddy says Woof!

"""
