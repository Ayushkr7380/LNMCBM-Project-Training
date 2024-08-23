#Dog class inherits from Wolf class with the same attribute or methods,
#it overrides them.
class Wolf:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof...")

pet1 = Dog("Tommy","Brown")
pet1.bark()

pet2 = Wolf("Jimmy","Grey")
pet2.bark()

Dog("abc","xyz").bark()