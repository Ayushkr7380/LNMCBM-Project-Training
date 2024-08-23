#Inheritance is a away to share functionality between classes.
class Animal: #superclass
    def __init__(self,name,color):
        self.name = name
        self.color = color

#Cat and Dog are subclass 
class Cat(Animal): #to inherit a class from another class,put the superclass name    
                            #in parentheses after the class name
    def mew(self):
        print("Cat meows..")
class Dog(Animal):
    def bark(self):
        print("Woof")

pet1 = Dog("Tommy","Brown")
print(pet1.name)
pet1.bark()
pet2 = Cat("lucy","white")
print(pet2.name)
pet2.mew()

