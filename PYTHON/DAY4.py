lst1 = list()
lst1.append('apple')
print('lst1 : ',lst1)
lst1.append('orange')
print('lst1 : ',lst1)
lst1.append(['fan','chair'])
print('lst1 : ',lst1)
del lst1[2]
print('lst1 : ',lst1)
lst1.extend(['fan','chair'])
print('lst1 : ',lst1)
lst2 = lst1
print('id of lst2 : ',id(lst2),' and id of lst1 : ',id(lst1))
lst2.append('toy')
print(' lst2 : ',lst2)
print(' lst1 : ',lst1)

lst3 = lst1.copy()
print('id of lst3 : ',id(lst3),' and id of lst3 : ',id(lst1))

lst3.append('toy')
print(' lst3 : ',lst3)
print(' lst1 : ',lst1)

print(lst3.count('toy'))

lst1.clear()
print(lst1)

print(lst3.index('fan'))

lst3.insert(2,'school')
print(lst3)

lst3.insert(0,'holy')
print(lst3)

lst3.insert(-1,'marker') # this will not insert in last index
#but insert in 2nd last index .use append to insert in last index

print(lst3)

print(len(lst3))

lst3.insert(30,'don') # if we write a index which is greater than
#the length  of list then it will insert in any index after lsat index
print(lst3)

print(lst3.pop())
print(lst3)

y =  lst3.pop(4)
print('y : ',y)

print(lst3.pop(-1))
print(lst3)


lst3.remove('school')
print(lst3)

lst3.reverse()
print(lst3)

lst4 = lst3.copy()
lst4.sort()
print(lst4)

lst4.sort(reverse = True)
print(lst4)

for i in range(1,6,1):
    print('*'*i)


