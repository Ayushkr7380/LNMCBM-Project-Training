#<-----------------Bitwise operator-------------------->

#bitwise AND operator
def bitwiseand(x,y):
    return x&y
n1 = int(input('Enter 1st number : '),10)
n2 = int(input('Enter 2nd number : '),10)
print(bitwiseand(n1,n2)) #2


#bitwise OR operator
def bitwiseor(x,y):
    return x|y
n1 = int(input('Enter 1st number : '),10)
n2 = int(input('Enter 2nd number : '),10)
print(bitwiseor(n1,n2)) #23

#leftshift operator
def leftshift(x,y):
    return x<<y
n1 = int(input('Enter 1st number : '),10)
n2 = int(input('Enter 2nd number : '),10)
print(leftshift(n1,n2)) #809240558043136

#rightshift operator
def rightshift(x,y):
    return x>>y
n1 = int(input('Enter 1st number : '),10)
n2 = int(input('Enter 2nd number : '),10)
print(rightshift(n1,n2)) #1

#bitwise NOT operator
def bitwisenot(x):
    return ~x
n1 = int(input('Enter 1st number : '),10)
print(bitwisenot(n1)) #-5

#bitwise XOR operator
def bitwiseXOR(x,y):
    return x^y
n1 = int(input('Enter 1st number : '),10)
n2 = int(input('Enter 2nd number : '),10)
print(bitwiseXOR(n1,n2)) #1

