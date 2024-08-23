res = lambda arg1 ,arg2 : arg1 + arg2

print("value of total : ", res(10,20))
print("value of total : ", res(39,20))

#We can create anonymous functions ,Known as lambda functions.
#It allows you to write very short functions.
f = lambda x : 2 * x
print(f(3))

#A return statement is never used in a lambda function,
#it always returns something.A lambda functions may contain if statements:
f1 = lambda x : x>10 
print(f1(12))
print(f1(2))

#map(function,iterable). It applies a function to every item in the iterable.
list1 = [1,2,3,4,5]
squarelist = list(map(lambda x : x*x , list1))
print("Map : ", squarelist)
#A lambda function is not a statement,it is an expression.
#Lambda functions do not support a block of statements.

#filter(function,iterable) creates a new list from
#the elements for which the function returns True.
List2 = [1,2,3,4,5,6,7,8,9,10]
even1 = list(filter(lambda x : x%2==0,List2))
print("Filter : ",even1)