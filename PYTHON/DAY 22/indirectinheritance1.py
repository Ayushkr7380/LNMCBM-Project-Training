#Indirect inheritance or Multilevel inheritance
class A:
    def first_method(self):
        print("Method of class A...")
class B(A):
    def second_method(self):
        print("Method of class B...")
class C(B):
    def third_method(self):
        print("Method of class C...")

obj = C()
obj.first_method()
obj.second_method()
obj.third_method()

C().third_method()
#Circular inheritance is not possible 