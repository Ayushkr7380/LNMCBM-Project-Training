#<-----------------Identitiy operator-------------------->

#is and is not operator
def isandisnot(x,y,z):
    x = ['lotus' , 'rose']
    y = ['ayush' , 'sonu']
    z = x
    return x,y,z
a , b , c = isandisnot([] , [] ,[] )
print(a is c)  #true
print(a is not c) #false
print(a is b) #false
print(a is not b) #true
print(a == b) #false
print(a != b) #true